class BankAccount:
    # constructor
    def __init__(self):
        self.__amount = 0

    # accessor/getter function for the __amount attribute
    def getAmount(self):
        return "${:.2f}".format(self.__amount)

    # mutator/setter function for the __amount attribute
    def setAmount(self, amount):
        # make sure the amount is a floating point number or integer first.
        # if not then don't do anything
        if isinstance(amount, float) or isinstance(amount, int):
            # check if the number is positive, you can't have negative bank account (lol)
            if amount >= 0:
                # store the amount as a float
                self.__amount = float(amount)


philsAccount = BankAccount()
philsAccount.setAmount(0)
print(philsAccount.getAmount())

philsAccount.setAmount(100.09129391239921)
print(philsAccount.getAmount())

philsAccount.setAmount(-1.0)
print(philsAccount.getAmount())

philsAccount.setAmount('abcd')
print(philsAccount.getAmount())
