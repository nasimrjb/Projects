# import os
# print(os.getcwd())
# new_directory = r"D:\OneDrive\Studies\Projects\Projects"
# os.chdir(new_directory)
# print(os.getcwd())

#############################################################################

# file = open(r'D:\OneDrive\Studies\Projects\Projects\short.txt', 'r')
# or

# file = open('intro.txt')
# x = file.read()
# print(x)


##############################################################################

with open('intro.txt') as f:
    data = f.read()
print(data)
print(f.closed)


##############################################################################
