# In Python there is only one logical type: booleans
# A boolean can only take two value: True or False (Capitalized)
# Booleans are built-in data type in Python

# import subprocess module
import subprocess as sp

import pynput
from pynput.keyboard import Key,Controller
keyboard = Controller()

import time

import random

# import colorama module
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


print()
print(135 * "-")
boolValue = input("Note: If you type True correctly into the console, Python echoes it back to you: " + Fore.RED + Style.BRIGHT)
True
False
if boolValue != str(True):
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "NameError: name " + Fore.WHITE + Back.RED + Style.BRIGHT + (boolValue) + Fore.WHITE + Back.BLACK + Style.BRIGHT + " is not defined")
    print()
else:
    print(Fore.WHITE + Back.RED + Style.BRIGHT + boolValue)
    print()
print(135 * "-")

boolValue2 = input("Type False correctly into the console, Python echoes it back to you: " + Fore.RED + Style.BRIGHT)   
if boolValue2 != str(False):
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "NameError: name " + Fore.WHITE + Back.RED + Style.BRIGHT + (boolValue2) + Fore.WHITE + Back.BLACK + Style.BRIGHT + " is not defined")
    print()
else:
    print(Fore.WHITE + Back.RED + Style.BRIGHT + boolValue2)
    print()
print(135 * "-")
# equal "=" sign assigns value to variable
VARa = 300 
VARb = 335

# dbl "==" equal sign compares 2 variables
VARa == VARb 
print("VARa == VARb")
print(Fore.RED + Style.BRIGHT + str(VARa == VARb))
print()
print(135 * "-")
# the not equal "!=" operator tests if 2 variables are different
VARa != VARb 
print("VARa != VARb")
print(Fore.RED + Style.BRIGHT + str(VARa != VARb))
print()
print(135 * "-")
# You can also test to see if a number is larger than the other
VARa > VARb
print("VARa > VARb")
print(Fore.RED + Style.BRIGHT + str(VARa > VARb))
print()
print(135 * "-")
# You can also test to see if a number is lesser than the other 
VARa < VARb
print("VARa < VARb")
print(Fore.RED + Style.BRIGHT + str(VARa < VARb))
print()
print(135 * "-")
# You can convert numbers to boolean by passing values to the booleans constructors
# In python numbers are converted to True except for zero; 0 is converted to False
bool(41581)
print("bool(41581)")
print(Fore.RED + Style.BRIGHT + str(bool(41581)))
bool(-34)
print("bool(-34)")
print(Fore.RED + Style.BRIGHT + str(bool(-34)))
bool(0) 
print("bool(0)")
print(Back.RED + Fore.WHITE + Style.BRIGHT + str(bool(0)))
print()
print(135 * "-")
# you can convert string to booleans
# In Python strings are converted to true except the empty string ""; the empty string "" is converted to false
bool("Python")
print("""bool("Python")""")
print(Fore.RED + Style.BRIGHT + str(bool("Python")))
bool(" ")
print("""bool(" ")""")
print(Fore.RED + Style.BRIGHT + str(bool(" ")))
bool("")
print("""bool("")""")
print(Back.RED + Fore.WHITE + Style.BRIGHT + str(bool("")))
print()
print(135 * "-")

# You can convert booleans to string
str(True)
print(Fore.GREEN + Style.BRIGHT + "str(True)")
print(str(True))
print(type(str(True)))
str(False)
print(Fore.GREEN + Style.BRIGHT + "str(False)")
print(str(False))
print(type(str(False)))
print()
print(135 * "-")

# You can convert booleans to integers
# if you convert True to an integer you get 1
# if you convert false to an integer you get 0
int(True)
print(Fore.GREEN + Style.BRIGHT + "int(True)")
print(int(True))

int(False)
print(Fore.GREEN + Style.BRIGHT + "int(False)")
print(int(False))
print()
print(135 * "-")

# Arithmetic operations: Python treats True as 1 and False as 0
25 + True
print("25 + True")
print(Fore.GREEN + Style.BRIGHT + str(25 + True))
25 * 0
print("25 * False")
print(Fore.GREEN + Style.BRIGHT + str(25*0))

# name program to open
programname = "Notepad.exe"

# now open 
sp.Popen(programname)

time.sleep(1)
sentence = """This is a short tutorial on BOOLEANS in Python\n
\nKey Takeaways:
\nA boolean can only take two value: True or False (Capitalized)
\nYou can use logical operators to compare booleans
\nYou can convert numbers to boolean by passing values to the booleans constructors
\nYou can convert booleans to string
\nyou can convert string to booleans
\nYou can convert booleans to integers
\nIn Arithmetic operations: Python treats True as 1 and False as 0
\n\n-[S3]RGE"""

for c in sentence:
    keyboard.press(c)
    keyboard.release(c)
    delay = random.uniform(0,0.2)
    time.sleep(0.1)
