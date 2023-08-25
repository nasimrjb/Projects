# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username1 = username
#         self.text = text
#         self.likes = likes


# c = Comment("nasimrjb", "I like neuroscience", 123)
# print(c.username1)

###########################################################################
# class BankAccount():
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0.0

#     def deposit(self, num1):
#         self.balance += num1
#         print(self.balance)

#     def withdraw(self, num2):
#         self.balance -= num2
#         print(self.balance)


# a = BankAccount("Darcy")
# print(a.owner)
# print(a.balance)
# a.deposit(10)
# a.withdraw(3)
# print(a.balance)

#####################################################
class Chicken:
    total_eggs = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        print(self.eggs)


c1 = Chicken("Alice", "partridge")
c2 = Chicken("Ashley", "Hanaee")
print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
c2.lay_egg()
c2.lay_egg()
print(Chicken.total_eggs)

########################################################
