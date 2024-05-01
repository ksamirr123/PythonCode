#ABSTRACTION : in which we only display important feature rather than showing all the things
# EXAMPLE:
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False

    def start(self):
        self.acc = True
        self.cluth = True
        print("Car started")

c1 = car()
c1.start()     


##ENCAPSULATION : WRAPPING OF DATA & FUNCTION IN A SINGLE UNIT(OBJECT).

#PRACTICE QUESTION
class Account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc

    def debit(self,amount):
        self.bal-=amount
        print("the amount is debited :",amount)    
    def credit(self,amount):
        self.bal+=amount
        print("the amount is credited :",amount)

    def  get_value(self):
        return self.bal   

c1 = Account(1000000,12345678)
print(c1.bal)
print(c1.acc)
c1.debit(5000)
c1.credit(230000000)
