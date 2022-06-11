import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect(('localhost', 2000))
        
        while (clientSocket):
            choice = input('1: Deposit\n2: Withdraw\n3: Check Balance\n4: Close Client Connection\n\nInput a number (1-4): ')
            print('-----------------------')
            if choice == '1':
                w_amount = input('How much would you like to deposit?\n')
                msg = f'{choice} {w_amount}'
            elif choice == '2':
                d_amount = input('How much would you like to withdraw?\n')
                msg = f'{choice} {d_amount}'
            elif choice == '3':
                msg = f'{choice} '
            elif choice == '4':
                msg = f'{choice} '
            else:
                print('Please enter a valid choice (1-4)')
                continue
            
            clientSocket.send(msg.encode())
            data = clientSocket.recv(1024)
            if data.decode() == 'Exiting Client':
                print(data.decode(), '\n')
                break
            else:
                print(data.decode(), '\n')

if __name__ == '__main__':
    main()
