class BankAccount:
    
    def __init__(self,account_number,account_name,account_type,balance):
        self.transactions = []
        self.account_number = account_number
        self.account_name = account_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        self.transactions.append({f" type: deposit,\n name: {self.account_name},\n balance: {self.balance},\n account number: {self.account_name},\n type: {self.account_type}\n"})
        with open("second_file.txt", "w") as file:
            file.write(str(self.transactions))  

    def withdraw(self, amount):
        if amount > self.balance:
            return "withdrawal limit reached"
        self.balance -= amount
        self.transactions.append({f" type: deposit,\n name: {self.account_name},\n balance: {self.balance},\n account number: {self.account_name},\n type: {self.account_type}\n"})
        with open("second_file.txt", "w") as file:
           file.write(str(self.transactions))
        
    def current_balance(self):
        return self.balance
    
    def transaction_history(self):
        with open("second_file.txt", "r") as file2:
            print(file2.readfile())

   
accounts = []   
def main():
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
                account_type = input("account type: ") 
                inital_deposit = int(input("deposit an amount: "))
                account_number = 1223344455
                bank = BankAccount(account_number,account_name,account_type,inital_deposit)
                accounts.append(bank)
                print("account created!")

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
main()