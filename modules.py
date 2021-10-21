# the backbone of the code is here
import requests, json
from credentials import *
from datetime import datetime
from presets import *
from os import system
from time import time

base_url = "https://v1.nocodeapi.com/"+user_name+"/cx/"+api

def get_one(lst):
  system("clear")
  url =  base_url+"/rates?source="+base+"&target="+lst
  response = requests.get(url)
  x = response.json()
  a = json.dumps(x)
  print(f"{RED}==============================================")
  print(f"{VIOLET}Current base currency is{CYAN}: {x['source']}")
  print(f"{VIOLET}Current date{CYAN}:             {x['date']}")
  print(f"{VIOLET}Value of {RED}1{base} {VIOLET}in {RED}{lst}{CYAN}:    {x['rates']}")
  print(f"{RED}==============================================")
  print()
  print()
  print()
  print()
  current_time = datetime.now()
  b = open(f"rates/singlerate-{current_time}.txt","w")
  b.write(a)
  print(f"{VIOLET}=================================================================================")
  print(f"{HIGHLIGHT}The Current rate is saved in {CYAN}rates/\'singlerate-{current_time}.txt\' {YELLOW}file{END}")
  print(f"{VIOLET}=================================================================================")

def get_all():
  system("clear")
  url =  base_url+"/rates?source="+base
  response = requests.get(url)
  x = response.json()
  a = json.dumps(x)
  current_time = datetime.now()
  b = open(f"rates/allrates-{current_time}.txt","w")
  b.write(a)
  print()
  print(f"{VIOLET}=======================================================================================")
  print(f"{HIGHLIGHT}The Current rates have been save to {CYAN}rates/\'allrates-{current_time}.txt\' {YELLOW}file{END}")
  print(f"{VIOLET}=======================================================================================")

def get_selected():
  system("clear")
  url =  base_url+"/rates?source="+base+"&target="+target
  response = requests.get(url)
  x = response.json()
  a = json.dumps(x)
  current_time = datetime.now()
  b = open(f"rates/selectedrates-{current_time}.txt","w")
  b.write(a)
  print()
  print(f"{VIOLET}============================================================================================")
  print(f"{HIGHLIGHT}The Current Selected rates have been save to {CYAN}rates/\'selectedrates-{current_time}.txt\' {YELLOW}file{END}")
  print(f"{VIOLET}============================================================================================")

def convert(amt,frm,to):
  url = base_url+"/rates/convert?amount="+amt+"&from="+frm+"&to="+to
  response = requests.get(url)
  x = response.json()
  print(f"{RED}======================================================")
  print(f"{VIOLET}Converting {CYAN}{amt}{frm} {VIOLET}to {CYAN}{to}")
  print(f"{VIOLET}Currently {CYAN}1{frm} = {x['info']['rate']}{to}")
  print()
  print(f"{HIGHLIGHT}{x['text']}{END}")
  print(f"{RED}======================================================")


def symbol():
  system("clear")
  url = base_url+"/symbols"
  response = requests.get(url)
  x = response.json()
  a = json.dumps(x)
  current_time = datetime.now()
  b = open(f"symbols.txt","w")
  b.write(a)
  print()
  print(f"{VIOLET}==============================================================================")
  print(f"{HIGHLIGHT}The Current Symbols have been save to {CYAN}symbols.txt {YELLOW}file{END}")
  print(f"{VIOLET}==============================================================================")

def ping():
  system("clear")
  start_time = time()
  url =  base_url+"/rates?source="+base
  response = requests.get(url)
  x = response.json()
  a = json.dumps(x)
  print(f"{RED}---------------- %s seconds -------------------" % (time() - start_time))

