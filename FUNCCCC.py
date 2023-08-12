# def speak_pig():
#     print('oink')


# speak_pig()


# Define a function called generate_evens
# # It should return a list of even numbers between 1 and 50(not including 50)
# def generate_events():
#     return [i for i in range(0, 50) if i % 2 == 0]


# print(generate_events())


# def yell(strng):
#     print(strng.upper() + "!")


# strr = input()
# yell(strr)


# # Without adding any new lines of code, make count_dollar_signs work as intended
# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == '$':
#             count += 1
#     return count
# print(count_dollar_signs(input()))
# def speak(animal="dog"):
#     if animal == "pig":
#         return "oink"
#     elif animal == "duck":
#         return "quack"
#     elif animal == "cat":
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     else:
#         return "?"


# print(speak(input()))


def spik(animal="dog"):
    dictt = {"dog": "bark", "pig": "oink", "duck": "quack", "cat": "meow"}
    return dictt.get(animal)


print(spik(input()))
