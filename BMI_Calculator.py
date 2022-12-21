import colorama

from colorama import Fore, Back, Style
colorama.init()

weight = int(input("Please Enter Your Weight : "));
height = float(input("Please Enter Your Height : "));
x = weight/float(height*height);

print("body mass index ==> ",x)
if x < 18.5:
    print(Fore.RED+'Underweight')
if x>=18.5 and x<25:
    print(Fore.GREEN+"Normal")
if x >= 25 and x < 30:
   print(Fore.RED+'Overweight')
if x >= 30:
   print(Fore.RED+'Obesity')