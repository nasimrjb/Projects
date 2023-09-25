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

# with open('story.txt') as f:
#     data = f.read()
# print(data)
# print(f.closed)


##############################################################################
# with open('story.txt', 'w') as file:
#     file.write("writing is great.\n")

#############################################################################
# def copy(name, new_name):
#     with open(name, 'r', encoding='utf-8') as f:
#         x = f.read()
#     with open(new_name, 'w', encoding='utf-8') as j:
#         for i in x[::-1]:
#             j.write(i)


# copy('alice.txt', 'alicee.txt')


#########################################################################################
def statistics(name):
    count = 0
    with open(name, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.count(" ")
        lines = text.count("\n")
        for i in text:
            count += 1

        print(lines)
        print(words)
        print(count)


statistics("alice.txt")
