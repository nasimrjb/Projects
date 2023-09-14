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
