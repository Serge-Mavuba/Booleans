# In Python there is only one logical type: booleans
# A boolean can only take two value: True or False
# Booleans are buitl-in data type in Python

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print()
boolValue = input("Note: If you type True correctly into the console, Python echoes it back to you: " + Fore.RED + Style.BRIGHT)
True
False
if boolValue != str(True):
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "NameError: name " + Fore.WHITE + Back.RED + Style.BRIGHT + (boolValue) + Fore.WHITE + Back.BLACK + Style.BRIGHT + " is not defined")
    print()
else:
    print(Fore.WHITE + Back.RED + Style.BRIGHT + boolValue)
    print()

boolValue2 = input("Type False correctly into the console, Python echoes it back to you: " + Fore.RED + Style.BRIGHT)   
if boolValue2 != str(False):
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "NameError: name " + Fore.WHITE + Back.RED + Style.BRIGHT + (boolValue2) + Fore.WHITE + Back.BLACK + Style.BRIGHT + " is not defined")
    print()
else:
    print(Fore.WHITE + Back.RED + Style.BRIGHT + boolValue2)
    print()

# equal "=" sign assigns value to variable
VARa = 300 
VARb = 335

# dbl "==" equal sign compare
VARa == VARb 
print("VARa == VARb")
print(VARa == VARb)
print()

# the not equal "!=" operator tests if 2 variables are different
VARa != VARb 
print("VARa != VARb")
print(VARa != VARb)
print()

# You can also test to see if a number is larger than the other
VARa > VARb
print("VARa > VARb")
print(VARa > VARb)
print()

# You can also test to see if a number is lesser than the other 
VARa < VARb
print("VARa < VARb")
print(VARa < VARb)
print()