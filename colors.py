from colorama import init
from termcolor import colored
import pyfiglet
# # help(termcolor)
# print(colored('Hello, World!', 'red', 'on_magenta', ['blink']))

colorr = input("what color do you want? ")
text = input("what do you wanna print? ")

msg = pyfiglet.figlet_format(text)
print(colored(msg, color="green"))
