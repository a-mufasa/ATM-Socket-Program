#Name: Ahmed Moustafa
#UARK ID: 010853047

import socket

class Bank:
    def __init__(self):
        self.balance = 100
    
    def check_balance(self):
        return str(self.balance)
    
    def deposit(self, amount):
        amount = int(amount)                             
        self.balance += amount
        return f'You successfully deposited ${amount}'
    
    def withdraw(self, amount):
        amount = int(amount)
        if amount > self.balance:
            return f'You lack the funds to withdraw ${amount}'
        else:
            self.balance -= amount
            return f'You successfully withdrew ${amount}'

def main():
    user_acct = Bank()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #allows re-run of server.py w/o needing new terminal (in turing)
        print("Socket created")
        serverSocket.bind(('localhost', 2000))
        serverSocket.listen()
        while True: #server socket is persistent along multiple clients
            connectionSocket, addr = serverSocket.accept()
            data = None
            with connectionSocket:
                print ('Connection from', addr )
                while connectionSocket: #allows multiple requests per client connection
                    data = connectionSocket.recv(1024).decode().split(' ')
                    msg = ''
                    if data[0] == '1': #DEPOSIT
                        if data[1].isnumeric():
                            msg = user_acct.deposit(data[1])
                        else:
                            msg = 'Enter a valid amount to deposit (a positive integer)'
                    elif data[0] == '2': #WITHDRAW
                        if data[1].isnumeric():
                            msg = user_acct.withdraw(data[1])
                        else:
                            msg = 'Enter a valid amount to withdraw (a positive integer)'
                    elif data[0] == '3': #CHECK BALANCE
                        msg = f'Your current balance is ${user_acct.check_balance()}'
                    elif data[0] == '4': #CLOSE CLIENT
                        msg = 'Exiting Client'
                        connectionSocket.send(msg.encode())
                        break
                    connectionSocket.send(msg.encode())
                print ('Disconnected from', addr )
        
if __name__ == '__main__':
    main()