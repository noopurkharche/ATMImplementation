###########################################################
# Name: Noopur A. Kharche
# Description : Automatic Teller Machine implementation
###########################################################

from datetime import date
import random
from os import system, name

# this class is used for accounts
class Account:
    # Construct an Account object
    def __init__(self, id, balance, dailyLimit, pin):
        self.accountNumber = id
        self.balance = balance
        self.dailyLimit = dailyLimit
        self.pin = pin
        self.lastTransactionDate = None
        self.transaction = []
        self.withdrawalLimit = 500

    def getId(self):
        return self.id

    # this method returns the current balance for the particular account
    def getBalance(self):
        return self.balance

    # this method is used to withdraw amount from the account
    # and also checks if amount is within daily withdrawal limit
    # it also creates a record for transaction
    def withdraw(self, amount):
        self.lastTransactionDate = str(date.today())
        self.withdrawalLimit = self.withdrawalLimit - float(amount)
        if self.withdrawalLimit >= 0:
            self.balance -= amount
            currentTransaction = Transaction(random.randrange(50, 2000), str(date.today()), 'Withdraw', amount)
            self.transaction.append(currentTransaction)
        else:
            print("withdraw Limit exceeded")

    # this method is used to deposit the amount into the account
    # it also creates a record for transaction
    def deposit(self, amount):
        self.balance += amount
        currentTransaction = Transaction(random.randrange(50, 2000), str(date.today()), 'Deposit', amount)
        self.transaction.append(currentTransaction)


# this class is used to keep track of transactions on the accounts
class Transaction:
    def __init__(self, id, date, type, amount):
        self.id = id
        self.date = date
        self.type = type
        self.amount = amount


# this method is used to generate data
def generateData():
    # Creating accounts
    accountsList = [];
    pin = 2212
    for i in range(1, 20):
        account = Account(i, random.randrange(50, 2000), 500, pin)
        accountsList.append(account)
        pin = pin + 10
    return accountsList


# this method is used to display the menu (list of possible operations)
def displayMenu():
    print("-----------Options------------")
    print("1. View Account Balance")
    print("2. Withdraw Cash")
    print("3. Make a Deposit")
    print("4. Print Statement")

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
       _ = system('cls')  
def main():
    # generate data to operate upon
    existingAccountList = generateData()

    # loop forever
    while True:
        clear()
        enteredPin = 0
        try:
           enteredPin = int(input("Enter the pin : "))
        except:
           print("Invalid Input!!")
           continue
        currentAccount = None
        
        # check if pin entered is correct (Enter a pin to Identify a unique customer)
        for account in existingAccountList:
            if enteredPin == account.pin:
                currentAccount = account
                break

        # if pin is invalid re-enter the pin
        if currentAccount == None:
            print("Invalid Pin")
            continue

        # display the menu
        displayMenu()
        selection = 0
        try:
           selection = input("Please make a selection : ")
        except:
           print("invalid selection!")
           continue

        selection = str(selection)
        if selection != '1' and selection != '2' and selection != '3' and selection != '4':
           print("Invalid Selection!!")
           continue
		   
        # do the following based on the section
        # display account balance if selected 1
        if selection == '1':
            print("The Account Balance is : " + str(currentAccount.getBalance()))
            try:
               key = input("press number key to continue....")
            except:
               continue

        # withdraw money if selected 2
        if selection == '2':
            withdrawAmount = float(input("Enter the amount you want to withdraw : "))
            currentBalance = currentAccount.getBalance()
            print("Balance before withdrawal : " + str(currentBalance))
            if currentBalance > float(withdrawAmount):
                if currentAccount.lastTransactionDate == 'None' or currentAccount.lastTransactionDate != str(
                        date.today()):
                    currentAccount.withdrawalLimit = 500
                currentAccount.withdraw(withdrawAmount)
                print("Balance after withdrawal: " + str(currentAccount.getBalance()))
                try:
                   key = input("press number key to continue....")
                except:
                   continue
            else:
                print("Insufficient Funds!!")
                try:
                   key = input("press number key to continue....")
                except:
                   continue
        # deposit money if selected 3
        if selection == '3':
            amount = float(input("Please enter the amount you want to deposit: "))
            print("Account Balance before Deposit : " + str(currentAccount.getBalance()))
            currentAccount.deposit(amount)
            print("Account Balance After Deposit : " + str(currentAccount.getBalance()))
            try:
               key = input("press number key to continue....")
            except:
               continue

        # display transaction statement if selected 4
        if selection == '4':
            print("------------Account Summary (Statement)-----------------")
            print("Date -------- Type ---------- Amount")
            for item in currentAccount.transaction:
                print(str(item.date) + "  " + str(item.type) + "  " + str(item.amount))
            print("---------------------------------------Total Amount " + str(currentAccount.getBalance()))
            print("--------------------------------------------------------")
            try:
               key = input("press number key to continue....")
            except:
               continue
		   

if __name__ == '__main__':
    main()
