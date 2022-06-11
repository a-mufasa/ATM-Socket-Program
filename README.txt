ATM Socket Program:

The program has a client and server file where the client takes user input for which request we will use. On the server, the client starts with $100
and runs the code corresponding to the selected action/request (deposit, withdraw, check balance, or close client). When depositing, you can add a
positive integer amount to your balance. When withdrawing, you can remove a positive integer amount from your balance as long as it is not greater than 
your current balance. 

To run the program follow the steps below:
1. Navigate to the correct location of the 2 files
2. Run "python3 server.py"
3. Open a new terminal and run "python3 client.py"
4. Follow the prompts on the terminal (to start, input a number 1-4 to select which action/request you'd like to do)

To see the persistance of the server, you can select '4' to close the client connection after modifying your balance and then run "python3 client.py"
again and your balance will be saved from the previous connection (you can test this by checking the balance). 

Notes (these don't affect proper functionality of code or grading): 
Line 28 of server.py makes it so that if you kill the server.py execution using ctrl+c, you can run it again without opening a new terminal in turing.
- Reference: https://stackoverflow.com/questions/27360218/how-to-close-socket-connection-on-ctrl-c-in-a-python-programme
- This will not save your modifications to the balance as the server socket was killed. 
- Also, if you kill the server without closing the client, you will get a broken pipe error unless you kill that client and re-run "python3 client.py".
