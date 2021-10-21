# code to accept and save user's API and some  prefrences
from presets import *
from time import *
from os import system

system("clear")
sleep(1)
print(f"{VIOLET}=========================================================================================================")
# Taking the input
usr_name = input(f"{CYAN}Enter your username{GREEN}: ")
api = input(f"{CYAN}Enter your api{GREEN}: ")
base = input(f"{CYAN}Enter your base currency in capital letters {YELLOW}(default is USD){GREEN}: ")
lst = input(f"{CYAN}Enter the name of Targetted currencies in capital letters followed by commas {YELLOW}','{GREEN}: ")
print(f"{VIOLET}========================================================================================================={END}")
comment = "Your API and prefrences are saved here"

# writing the inputs to another python file
x = open("credentials.py", "w")
x.write(f"{comment}\n\nuser_name = '{usr_name}'\napi = '{api}'\nbase = '{base}'\ntarget = '{lst}'")
x.close()

