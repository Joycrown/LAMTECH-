class Budget:
    def __init__(self, category):
        self.category = category
        self.balance = 1000


    def withdrawal (self,amount ):
        if amount <= self.balance :
            self.balance -= amount
        else:
            print('insufficient funds')
            return

    def transfer (self,amount):
       pass

    def deposit(self, amount):
        self.balance += amount
        return

    def getbalance(self):
       return self.balance






food= Budget('food')
food.withdrawal(5000)
print(food .getbalance())
#clothing = Budget('clothing')
#clothing.withdrawal(2000)
#print(clothing. getbalance())
#food= Budget('food')
#food.transfer(2000,clothing)
#print(clothing.getbalance())
