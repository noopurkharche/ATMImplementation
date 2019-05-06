# ATMImplementation
ATM Implementation in python

Programing Language Used?
 Python

How the Program is Structured?
 The program contains two classes (Account and Transaction). Account class represents an account with properties as pin, balance, accountnumber etc and method such as 
 getbalance (view the account balance), withdraw (withdraw money from account) and deposit (deposit money to account). Transaction class conatins properties such as 
 transaction id, amount , date and type of transaction. Each intance of transaction will represent transaction of the account. An account can have number of 
 transactions such as deposit and withdrawal.

What does the program do?
 The program will initially generate account data to operate upon. The pin to account will be 2212 and then in the increment of 10.(eg 2212,2222,2232 etc.)
 The program will generate twenty accounts with amount randomly between 50 to 2000 and pin as mentioned above. After generation of the accounts it asks the user to 
 enter the pin. When the user enteers the pin and if it is correct then it shows the list of operations to perform such as view balance, withdraw, deposit and 
 statement. Based on the user selection the program performs the given operation. After the given operation is performed the program again asks the user to enter pin.
 This goes on forever.
 
How to run the program?
 Just type in the following command in your python console
 
 python atmCode.py
  
