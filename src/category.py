class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.amount = 0
        self.description = ""

    def deposit(self, transaction, description):
        if description == None:
            description = ""
        self.amount += transaction
        print(self.amount)
        self.ledger.append({'Amount': transaction, 'Description': description})
        print(self.ledger)

    def withdrawal(self, transaction, description):
        if transaction > self.amount:
            print('Transaction Denied')
        elif transaction <= self.amount:
            self.amount -= transaction
            print(self.amount)
        self.ledger.append({'Amount': -abs(transaction), 'Description': description})
        print(self.ledger)

    def get_balance(self):
        print(self.amount)
        

    def transfer(self, transaction, name):
        if transaction > name.amount:
            print('Transaction STILL Denied')
        elif transaction <= name.amount:
            name.amount += transaction
        if transaction > self.amount:
            print('Feel broke yet?')
        elif transaction <= self.amount:
            self.amount -= transaction
        print(f'${transaction}.00 has been transfered to {self.amount}')
        print(f'${initial_deposit.amount}.00 initial deposit amount after transfer')
        print(f'${name.amount}.00')

        pass

    def check_funds(self):
        pass

    def __str__(self):
        pass


initial_deposit = Category('Intial Deposit')
rent = Category('Rent')

initial_deposit.deposit(5000, 'Deposit')
initial_deposit.withdrawal(2500, 'Withdrawal')
initial_deposit.get_balance()
initial_deposit.transfer(1250, rent)



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
    