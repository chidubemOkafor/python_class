class BankAccount:
    
    def __init__(self,account_number,account_name,account_type,balance):
        self.account_number = account_number
        self.account_name = account_name
        self.account_type = account_type
        self.balance = balance

        self.transactions_file = f"{self.account_name}.txt"

    def deposit(self,amount):
        self.balance += amount

        self.add_transactions(f"Deposied: {amount}\n")
   
    def add_transactions(self,message):
        with open(self.transactions_file, "a") as file:
            file.write(str(message))

    def withdraw(self, amount):
        if amount > self.balance:
            return "withdrawal limit reached"
        self.balance -= amount
        self.add_transactions(f"withdraw: {amount}\n")
              
    def current_balance(self):
        return self.balance
    
    def transaction_history(self):
        with open(self.transactions_file, "r") as file2:
            result = file2.read()
            return result
         
def main():
        accounts = [] 
        while True:
            print("select an option")
            print("1. create an account")
            print("2. deposit funds to your account")
            print("3. withdraw funds from your account")
            print("4. get balance")
            print("5. transaction history")
            print()
            response = int(input(""))

            if response == 1:
                account_name = input("name: ")

                print("select an account type")
                print("1. savings")
                print("2. current")
                print("3. student")
                print()
                account_response = int(input(""))
                if account_response == 1:
                    account_type = "savings"
                elif account_response == 2:
                    account_type = "current"
                elif account_response == 3:
                    account_type = "student"

                inital_deposit = int(input("deposit an amount: "))
                account_number = 1223344455
                bank = BankAccount(account_number,account_name,account_type,inital_deposit)
                accounts.append(bank)
                print(f"account created! your account number is {account_number}")

            elif response == 2:
                name = input("enter account name: ")
                for account in accounts: 
                    if name == account.account_name:
                        deposit_amount = int(input("amount to deposit: "))
                        account.deposit(deposit_amount)
                        balance = account.current_balance()
                        print(f"your balance is {balance}")
                        break
                else:
                    print("account does not exist")

            elif response == 3:
                name = input("enter your name: ")
                for account in accounts:
                    if name == account.account_name:
                        withdraw_amount = int(input("amount to withdraw: "))
                        print(account.withdraw(withdraw_amount))
                        balance = account.current_balance()
                        print(f"your balance is {balance}")
                        break
                else:
                    print("account does not exist")

            elif response == 4:
                name = input("enter your name: ")
                for account in accounts:
                    if name == account.account_name:
                        print(account.current_balance())
            
            elif response == 5:
                name = input("enter your name: ")
                for account in accounts:
                    if name == account.account_name:
                        print(account.transaction_history())
            else:
                print("nothing")

main()