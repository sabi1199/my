#!/usr/bin/python
# -*- coding: UTF-8 -*-

from distutils.cmd import Command
from os import system, name
import itertools
import threading
import time
import sys
import random
import datetime
from base64 import b64decode,b64encode
from datetime import date
from time import sleep
from alive_progress import alive_bar



expirydate = datetime.date(2021, 9, 24)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
green="\033[3;32m"
neon="\033[3;36m"
nc="\033[00m"
red="\033[3;31m"
purple="\033[3;34m"
yellow="\033[3;33m"
voilet="\033[3;35m"

def hero():
    def load():
        # for i in tqdm(range(10)):
        #     sleep(0.1)
        with alive_bar(100, force_tty=True) as bar:
            for i in range(100):
                time.sleep(0.7)
                bar()

            

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    clear()
    y=1
    newperiod=period
    banner='figlet SxBuz 1.0|lolcat'
    numbers=[]
    Commands='curl https://4890-103-83-145-28.ngrok.io/ms.txt'
    Commands1='curl https://4890-103-83-145-28.ngrok.io/ms1.txt'
    Commands2='curl https://4890-103-83-145-28.ngrok.io/ms2.txt'
    Commands3='curl https://4890-103-83-145-28.ngrok.io/ms3.txt'
    Commands4='curl https://4890-103-83-145-28.ngrok.io/ms4.txt'
    Commands5='curl https://4890-103-83-145-28.ngrok.io/ms5.txt'
    Commands6='curl https://4890-103-83-145-28.ngrok.io/ms6.txt'
    Commands7='curl https://4890-103-83-145-28.ngrok.io/ms7.txt'
    Commands8='curl https://4890-103-83-145-28.ngrok.io/ms8.txt'
    Commands9='curl https://4890-103-83-145-28.ngrok.io/ms9.txt'

    system(banner)
    #print(f"{red}Contact me on telegram @smsn_knt")
    #now = datetime.datetime.now()
    #First = now.replace(hour=18, minute=20, second=0, microsecond=0)
    #Firstend = now.replace(hour=21, minute=36, second=0, microsecond=0)
    i=0
    while(y):
        #now = datetime.datetime.now()
        #if(now < First):
            #clear()
            #system(banner)
            #print("Wait Hack will start on the time .....")
            print("You can wait for time or Exit")
            #time.sleep(10)
            #clear()
        #elif (now>First and now<Firstend):
            #while(True):
            
             clear()
             system(banner)
             print(f"{red}Contact me on telegram @smsn_knt")
             if (i==0):
                 load()
                 print("Period:            Colour ")
                 system(Commands)
             if (i==1):
                 load()
                 print("Period:            Colour ")
                 system(Commands1)
             if (i==2):
                 load()
                 print("Period:            Colour ")
                 system(Commands2)
             if (i==3):
                 load()
                 print("Period:            Colour ")
                 system(Commands3)
             if (i==4):
                 load()
                 print("Period:            Colour ")
                 system(Commands4)
             if (i==5):
                 load()
                 print("Period:            Colour ")
                 system(Commands5)
             if (i==6):
                 load()
                 print("Period:            Colour ")
                 system(Commands6)
             if (i==7):
                 load()
                 print("Period:            Colour ")
                 system(Commands7)
             if (i==8):
                 
                 load()
                 print("Period:            Colour ")
                 system(Commands8)
             if (i==9):
                 
                 load()
                 print("Period:            Colour ")
                 system(Commands9)

            
            
            
            #  #n = random.randint(1,30)
            #  #  if(n%2==0):
            #  #      c=f"{red}🔴  Red"
            #  #  else:
            #  #      c=f"{green}🟢  Green"
            #  #  print(f"{red}  Period          ", f"{neon}"    ,   load(),     f"{green}     Colour")
            #  #  print(f"{yellow}",newperiod,"            ",c)
            #  print(f"{red}   Period       ", system(Commands))
             newperiod+=1   
             i+=1    
             numbers.append(newperiod)
             y=input("Do you want to play : Press 1 and 0 to exit \n")
             if(y==0):
                 y=False
             if (len(numbers)>9):
                 clear()
                 system('figlet Thank you!!')
                 print("Play on next specified time!!")
                 print("-----------Current Time UP----------")
                 sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
            #print(numbers)
             else:
             break
    
    #y=input("Do you want to play : Press 1 and 0 to exit \n")
    #if(y==0):
     #   y=False
    #if (len(numbers)>11):
    clear()
    system(banner)
    system('figlet Thank you!!')
    print("Play on next specified time!!")
    print("-----------Current Time UP----------")
    sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
        #print(numbers)

     
