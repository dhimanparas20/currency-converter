from modules import *
from os import system
from time import sleep
from presets import *

system("clear")
print (VIOLET+"#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print (RED+"#------------------==================================================---------------------#")
print ("#------------------"+HIGHLIGHT+"| WELCOME TO COMPILING SCRIPTS BY MST PRODUCTIONS|"+END+RED+"---------------------#")
print ("#------------------==================================================---------------------#")
print (VIOLET+"#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#----------------------------------------------------------------------"+HIGHLIGHT+CYAN+"BY: Paras Dhiman --#"+END)
print ()
sleep(2)

print (RED+"------------------------------------------------")
print (VIOLET+"            Choose your Choice                  ")
print (RED+"------------------------------------------------")
print (GREEN+"0: Save my API and prefrences")
print ("1: Convert Currency")
print ("2: Get all Currency Rates")
print ("3: Get Currency rates of saved countries")
print ("4: Get Currency rate of a single country")
print ("5: Show Country Symbols")
print ("6: Check ping (response time)")
print ("69: Exit"+END)
print (RED+"================================================")
inp = int(input(f"{CYAN}Enter your choice {YELLOW}:"))
print (RED+"================================================")
print()

if inp == 0:
  system("python3 gen_credentials.py")
  print()
  input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
  loop()

if inp == 1:
  system("clear")
  print (RED+"======================================================")
  amt = input(f"{YELLOW}Enter the amount you want to convert{CYAN}: ")
  frm = input(f"{YELLOW}Enter the currency from which you want to convert{CYAN}: ")
  to =  input(f"{YELLOW}Enter the currency to which you want to convert{CYAN}: ")
  print (RED+"======================================================")
  convert(amt,frm,to)
  print()
  input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
  loop()

if inp == 2:
  get_all()
  print()
  input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
  loop()

if inp == 3:
  get_selected()
  print()
  input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
  loop()

if inp == 4:
  print (RED+"=========================================================")
  inpu = input(f"{CYAN}Enter the country code you want to see rate of{VIOLET}:")
  print (RED+"=========================================================")
  get_one(inpu)
  print()
  input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
  loop()

if inp == 5:
  symbol()
  print()
  input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
  loop()

if inp == 6:
  ping()
  print()
  input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
  loop()  

if inp == 69:
  exit()
