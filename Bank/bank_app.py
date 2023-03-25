#Create a class for the back account
class BankAccount:
    #initializing the class object attributes
    def __init__(self, account_holder_name: str, account_number: str, balance: float = 0.0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    #Perform the deposit
    def deposit(self, amount: float):
        if amount <= 0:
            print("Invalid amount. Amount must be greater than zero.\n")
            print("99. Home")
            print("0. Exit\n")
            getChoiceField()
        else:
            self.balance += amount
            print(f"Deposit of {amount:.2f} Rwf was successful. New balance is {self.balance:.2f} Rwf.\n")
            print("99. Home")
            print("0. Exit\n")
            getChoiceField()

    #Withdraw operation
    def withdraw(self, amount: float):
        if amount <= 0:
            print("Invalid amount. Amount must be greater than zero.\n")
            print("99. Home")
            print("0. Exit\n")
            getChoiceField()
        elif amount > self.balance:
            print("Withdrawal failed. Insufficient balance.\n")
            print("99. Home")
            print("0. Exit\n")
            getChoiceField()
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount:.2f} Rwf was successful. New balance is {self.balance:.2f} Rwf.\n")
            print("99. Home")
            print("0. Exit\n")
            getChoiceField()

    #Check balance operation
    def check_balance(self):
        print(f"Current balance for {self.account_holder_name} is {self.balance:.2f} Rwf.\n")
        print("99. Home")
        print("0. Exit\n")
        getChoiceField()

#Store all created accounts
accounts = {}

#Display the choice selection field
def getChoiceField():
    global choice
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid character found, only numbers are allowed.")
        getChoiceField()

#Creating the account        
def create_account():
    print("=== Create Account ===")
    account_holder_name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Account already exists.\n")
        print("99. Home")
        print("0. Exit\n")
        getChoiceField()
    else:
        accounts[account_number] = BankAccount(account_holder_name, account_number)
        print("Account created successfully.\n")
        print("99. Home")
        print("0. Exit\n")
        getChoiceField()

#Deposit form
def deposit():
    print("=== Deposit ===")
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.\n")
        print("99. Home")
        print("0. Exit\n")
        getChoiceField()
    else:
        amount = float(input("Enter amount to deposit: "))
        accounts[account_number].deposit(amount)

#Withdraw form
def withdraw():
    print("=== Withdraw ===")
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        print("99. Home")
        print("0. Exit\n")
        getChoiceField()
    else:
        amount = float(input("Enter amount to withdraw: "))
        accounts[account_number].withdraw(amount)

#Check Balance form
def check_balance():
    print("=== Check Balance ===")
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        print("99. Home")
        print("0. Exit\n")
        getChoiceField()
    else:
        accounts[account_number].check_balance()

#System home page
def home():
    print("\n\nWelcome to our Banking System\n")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("0. Exit\n")
    getChoiceField()


while True:
    if 'choice' in locals():
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 0:
            print("You are about to leave the System.")
            print("Are you sure you want to leave?")
            print("1. Yes")
            print("0. No")
            decision = input("Enter your choice: ")
            if decision == '1':
                print("Bye...\nThank you for using our Banking System.")
                break
            elif decision == '0':
                home()
            else:
                print("Invalid selection.")
                home()
        elif choice == 99:
            home()
        else:
            print("Invalid choice. Please enter a valid choice.")
            print("99. Home")
            print("0. Exit\n")
            choice = int(input("Enter your choice: "))
    else:
        home()
