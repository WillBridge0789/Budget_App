class Category:
    def __init__(self):
        self.name = name
        self.ledger = []
    def withdraw(self, wit_amount, wit_description):
        
        print(f'{self.name} you withdrew ${wit_amount}.')

    def deposit(self, dep_amount, dep_description):
        self.dep_amount = 0
        self.dep_description = ""
    def get_balance(self):
        pass



    # deposit: 
        # accepts an amount and description
        # IF no description is given, it should default to an empty

    # withdraw:
        # accepts an amount and description
        # amount should be stored in ledger as a negative number
        # IF theres not enough funds, nothing happens to the ledger
        # this method should True if withdrawl took place, and False otherwise

    # get_balance
        # returns current_balance of budget based on DEPOSIT's and WITHDRAW's that occured

    # transfer