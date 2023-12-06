class Bankaccount:
    def __init__(self,balance) -> None:
        self.balance = balance

    def get_balance(self):
        print("Your Balance: ", self.balance)

    def widraw(self):
        self.widraw = int(input("Enter widrawl ammount: "))
        

    def deposit(self):
        self.deposit = int(input("enter depositing ammount: "))
        

    def get_new_balance(self):
        if a == 1:
            print("New ammount: ", self.balance - self.widraw)
        elif a==2:
            print("New ammount: ", self.balance + self.deposit)
        else:
            print("Not valid entry")

# a_widraw = int(input("Enter widrawal amount: "))
# a_deposit = int(input("Enter depositing amount: "))
bnkacc = Bankaccount(10000)

a = int(input("Enter (1:widraw), (2:deposit): "))
        
if a == 1:
    bnkacc.widraw()
elif a == 2:
    bnkacc.deposit()
else:
    print("Not valid entry")

bnkacc.get_balance() 

bnkacc.get_new_balance()