# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username1 = username
#         self.text = text
#         self.likes = likes


# c = Comment("nasimrjb", "I like neuroscience", 123)
# print(c.username1)

###########################################################################
class BankAccount():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, num1):
        self.balance += num1
        print(self.balance)

    def withdraw(self, num2):
        self.balance -= num2
        print(self.balance)


a = BankAccount("Darcy")
print(a.owner)
print(a.balance)
a.deposit(10)
a.withdraw(3)
print(a.balance)

#####################################################
