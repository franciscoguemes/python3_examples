#!/usr/bin/env python3

# ###############################################################################
# IMPORTANT NOTE:
# 	This script only works properly if either you include the Python Shebang 
#	at the beginning of the script or you execute the script using the Python
#	interpreter in the command line: python3 my_script.py
#	In any other case the coloring will not work properly.
#
#################################################################################

#
# You can see a very good explanation on the colored text in this video:
#	https://www.youtube.com/watch?v=u51Zjlnui4Y
#

import colorama
from colorama import Fore, Back, Style


#Initialize the color. Uncomment this line if you execute this script in Windows.
#colorama.init()

#In Mac and Linux the previous line is not necessary unless you want to use the
# autoreset property which basically resets the color automatically
#colorama.init(autoreset)


print('\033[31m' + 'some red text')
print('All the text after the special format character is also red')
print('\033[39m')  #This is the reset style character.

print(Fore.RED + 'another red text. Same as the previous one')
print('\033[39m')
print('normal text after red text')

print(Fore.RED + 'another red text.')
print(Fore.RESET)
print('Color has been reset using the Fore.RESET')


#From here on I will use autoreset so I do not need to manually reset the formatting.
colorama.init(autoreset=True)

print(Back.CYAN + 'normal text with cyan background')
print(Style.BRIGHT + 'BRIGHT')
print(Fore.RED + Back.GREEN + "red text on green background")


print(f"{Style.DIM}{Back.BLUE}{Fore.BLACK}Text created with an F-String")


'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
