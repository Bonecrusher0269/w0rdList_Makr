import itertools
import os
from colorama import *
import pyfiglet
from time import sleep
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()

def ascii(text):
    result = pyfiglet.figlet_format(text)
    print(result)

def clear():

  os.system("cls || clear")

clear()

print(Fore.RED)

print("   *******************************************************************")

ascii("  w0rdList_Makr")

print("  Thanks for downloading! I am in no way responsible for how you use this :)")

print(Fore.MAGENTA)

print("\n  Beginning string ex [tp******] / Enter = ''\n")

beg = str(input("  Add a beginning string : "))

clear()

print(Fore.RED)

print("   *******************************************************************")

ascii("  w0rdList_Makr")

print(Fore.MAGENTA)

print("\n  Ending string ex [******tp] / Enter = ''\n")

end = str(input("  Add an ending string : "))

clear()

print(Fore.RED)

print("   *******************************************************************")

ascii("  w0rdList_Makr")

print(Fore.MAGENTA)

minN = int(input("\n  Enter MIN amount of characters long : "))

maxX = int(input("\n  Enter MAX amount of characters long : "))

clear()

print(Fore.RED)

print("   *******************************************************************")

ascii("  w0rdList_Makr")

print(Fore.MAGENTA)

print("\n  [ 1 ] Use alphabet")
print("  [ 2 ] Use numbers 0-9")
print("  [ 3 ] Use alphabet and Use numbers 0-9")
print("  [ 4 ] Use custom character set\n")

i = 1

while i == 1:

    choice = input("  Select an option : ")

    if choice == "1":

        chars = "abcdefghikjlmnopqrstuvwxyz"
        i = 0

    elif choice == "2":

        chars = "0123456789"
        i = 0

    elif choice == "3":

        chars = "abcdefghikjlmnopqrstuvwxyz0123456789"
        i = 0

    elif choice == "4":

        chars = str(input("\n  Select characters to include : "))
        i = 0

    else:

        print("\n  [ Error ] Enter a valid option \n")

clear()

print(Fore.RED)

print("   *******************************************************************")

ascii("  w0rdList_Makr")

print(Fore.MAGENTA)

loc = filedialog.askdirectory()

name = str(input("\n  Enter name of file : "))

file = open(str(loc) + "/" + name + ".txt", "w")

if minN == maxX:

  num = minN

  for xs in itertools.product("".join(set(chars)), repeat=num):
    print("  " + beg + ''.join(xs) + end)
    file.write(beg + ''.join(xs) + end + "\n")

else:

  while minN < maxX + 1:

    for xs in itertools.product("".join(set(chars)), repeat=minN):
      print("  " + beg + ''.join(xs) + end)
      file.write(beg + ''.join(xs) + end + "\n")
    minN += 1

file.close()

print(Fore.RED)

print("\n   *******************************************************************")

ascii("  Done")

while True:

    sleep(2.0)
    break
