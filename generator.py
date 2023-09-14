# def week():
#     weekdays = ['Monday', 'Tuesday', 'Wednesday',
#                 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     for i in weekdays:
#         yield i


# next(week())
# print(next(week()))


###############################################################
# def yes_or_no():
#     answer = "yes"
#     while True:
#         yield answer
#         answer = "no" if answer == "yes" else "yes"


###############################################################


# def make_song(num=99, fruit="soda"):
#     try:
#         while num >= 0:
#             if num == 1:
#                 yield f"only 1 bottle of {fruit} left!"
#             elif num == 0:
#                 yield "No more left!"
#             else:
#                 yield f"{num} bottles of {fruit} on the wall"
#             num -= 1
#     except:
#         yield "StopIteration"


# kombucha_song = make_song(5, "kombucha")
# print(next(kombucha_song))  # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '5 bottles of kombucha on the wall.'

# # next(kombucha_song)  # '4 bottles of kombucha on the wall.'
# # next(kombucha_song)  # '3 bottles of kombucha on the wall.'
# # next(kombucha_song)  # '2 bottles of kombucha on the wall.'
# # next(kombucha_song)  # 'Only 1 bottle of kombucha left!'
# # next(kombucha_song)  # 'No more kombucha!'
# # next(kombucha_song)  # StopIteration


# default_song = make_song()
# for i in next(default_song):
#     print(next(default_song))  # '99 bottles of soda on the wall.'


######################################################################
def get_multiples(num=1, count=10):
    sum = num
    for i in range(count):
        yield sum
        sum += num


evens = get_multiples(2, 3)
print(next(evens))  # 2
print(next(evens))  # 2
print(next(evens))  # 2


default_multiples = get_multiples()
print(list(default_multiples))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#####################################################################
def get_unlimited_multiples(num=1):
    sum = num
    while True:
        yield sum
        sum += num


sevens = get_unlimited_multiples(7)


a = [next(sevens) for i in range(15)]
print(a)
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
print([next(ones) for i in range(20)])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

###################################################################
