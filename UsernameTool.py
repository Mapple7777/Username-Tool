#Made by mapple 

import os, webbrowser, requests,time,random
from colorama import init, Fore, Back, Style
from urllib.request import urlopen
import json
import threading

def ResetTool():
    while 1:
        Design()
        os.system("pause")

def Design():
    os.system(f"cls && title Roblox Username Tool, Made By Mapple")
    print(f"""
{Fore.LIGHTBLUE_EX}  _____       _     _            {Fore.LIGHTMAGENTA_EX} _    _                                          {Fore.LIGHTBLUE_EX} _______          _ {Fore.LIGHTMAGENTA_EX}           ___  
{Fore.LIGHTBLUE_EX} |  __ \     | |   | |           {Fore.LIGHTMAGENTA_EX}| |  | |                                         {Fore.LIGHTBLUE_EX}|__   __|        | |{Fore.LIGHTMAGENTA_EX}          |__ \ 
{Fore.LIGHTBLUE_EX} | |__) |___ | |__ | | _____  __ {Fore.LIGHTMAGENTA_EX}| |  | |___  ___ _ __ _ __   __ _ _ __ ___   ___ {Fore.LIGHTBLUE_EX}   | | ___   ___ | |{Fore.LIGHTMAGENTA_EX}  __   __    ) |
{Fore.LIGHTBLUE_EX} |  _  // _ \| '_ \| |/ _ \ \/ / {Fore.LIGHTMAGENTA_EX}| |  | / __|/ _ \ '__| '_ \ / _` | '_ ` _ \ / _ \{Fore.LIGHTBLUE_EX}   | |/ _ \ / _ \| |{Fore.LIGHTMAGENTA_EX}  \ \ / /   / /
{Fore.LIGHTBLUE_EX} | | \ \ (_) | |_) | | (_) >  <  {Fore.LIGHTMAGENTA_EX}| |__| \__ \  __/ |  | | | | (_| | | | | | |  __/{Fore.LIGHTBLUE_EX}   | | (_) | (_) | |{Fore.LIGHTMAGENTA_EX}   \ V /   / /_ 
{Fore.LIGHTBLUE_EX} |_|  \_\___/|_.__/|_|\___/_/\_\ {Fore.LIGHTMAGENTA_EX} \____/|___/\___|_|  |_| |_|\__,_|_| |_| |_|\___|{Fore.LIGHTBLUE_EX}   |_|\___/ \___/|_|{Fore.LIGHTMAGENTA_EX}    \_/   |____| 
{Fore.LIGHTBLUE_EX} Made By Mapple
    """)
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}1{Fore.LIGHTWHITE_EX}] Discord Server')
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}2{Fore.LIGHTWHITE_EX}] Check Username')
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}3{Fore.LIGHTWHITE_EX}] Username Sniper')
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}4{Fore.LIGHTWHITE_EX}] User Information')
    print("")

    answer = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}Input{Fore.LIGHTWHITE_EX}]══> ")

    if answer == "1":
        print(f"{Fore.LIGHTWHITE_EX} Opened Discord Link In Browser")
        webbrowser.open_new_tab("https://discord.gg/6WJAdYjdtA")
    
    elif answer == "2":
        print("Opened Check Username")
        user = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}Enter Username{Fore.LIGHTWHITE_EX}]══> ")
        try:
            r = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={user}&request.birthday=01%2F01%2F2000&request.context=Signup").json()
            if r['code'] == 0:
                print(f"{Fore.LIGHTGREEN_EX}Username: " + user + " Is Not Taken")
            else:
                print(f"{Fore.LIGHTRED_EX}Username: " + user + " Is Taken")
        except:
            print(f"{Fore.LIGHTRED_EX}An Error Occured")

    elif answer == "3":
        
        print("Opened Username Sniper")
        length        = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}Length{Fore.LIGHTWHITE_EX}]══> ")
        logtofilebool = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}Log To File? (Y/N){Fore.LIGHTWHITE_EX}]══> ").upper()
        nottakenbool = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}Only Display Not-Taken (Y/N){Fore.LIGHTWHITE_EX}]══> ").upper()
        xthread       = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}Threads{Fore.LIGHTWHITE_EX}]══> ")
        LogFile       = "Not_Taken.txt"
        AllowedChars  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123457890"
        def sniper():
            try: 
                while True:
                    final = ''.join(random.choice(AllowedChars) for x in range(int(length)))
                    r = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={final}&request.birthday=01%2F01%2F2000&request.context=Signup").json()
                    if r['code'] == 0:
                        if logtofilebool == "Y":
                            print(f"{Fore.LIGHTGREEN_EX}Username: " + final + " | Status: Not Taken")
                            with open(LogFile, "a") as f:
                                f.write(final+"\n")
                        elif logtofilebool == "N":
                            print(f"{Fore.LIGHTGREEN_EX}Username: " + final + " | Status: Not Taken")
                    else:
                        if nottakenbool == "N":
                            print(f"{Fore.LIGHTRED_EX}Username: " + final + " | Status: Taken")
            except:
                print(f"{Fore.LIGHTRED_EX}An Error Occured")

        Threads = []

        for i in range(int(xthread)):
            t = threading.Thread(target=sniper)
            t.daemon = True
            Threads.append(t)

        for i in range(int(xthread)):
            Threads[i].start()

        for i in range(int(xthread)):
            Threads[i].join()

    elif answer == "4":
        print("[!] Select Option")
        print("[1] User ID")
        print("[2] Username")
        choice = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}Input{Fore.LIGHTWHITE_EX}]══> ")
        if choice == "1": 
            print("Please User ID")
            uid = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}User ID{Fore.LIGHTWHITE_EX}]══> ")

            r1 = urlopen(f"https://users.roblox.com/v1/users/" + uid)
            d1 = r1.read()
            f = json.loads(d1)

            r2 = urlopen(f"https://users.roblox.com/v1/users/" + uid + "/status")
            d2 = r2.read()
            f2 = json.loads(d2)

            r3 = urlopen(f"https://users.roblox.com/v1/users/" + uid + "/username-history")
            d3 = r3.read()
            f3 = json.loads(d3)

            x1 = str(f['description'])
            x2 = str(f['created'])
            x3 = str(f['isBanned'])
            x4 = str(f['externalAppDisplayName'])
            x5 = str(f['id'])
            x6 = str(f['name'])
            x7 = str(f['displayName'])
            x8 = str(f2['status'])
            print(f"{Fore.LIGHTGREEN_EX}=============< Information >=============")
            print(f"{Fore.LIGHTCYAN_EX}Profile Link: {Fore.LIGHTWHITE_EX}" + f"https://www.roblox.com/users/" + x5 + "/profile")
            print(f"{Fore.LIGHTCYAN_EX}Description: {Fore.LIGHTWHITE_EX}" + x1)
            print(f"{Fore.LIGHTCYAN_EX}Status: {Fore.LIGHTWHITE_EX}" + x8)
            print(f"{Fore.LIGHTCYAN_EX}Created: {Fore.LIGHTWHITE_EX}" + x2)
            print(f"{Fore.LIGHTCYAN_EX}Banned: {Fore.LIGHTWHITE_EX}" + x3)
            print(f"{Fore.LIGHTCYAN_EX}External App Display Name: {Fore.LIGHTWHITE_EX}" + x4)
            print(f"{Fore.LIGHTCYAN_EX}User ID: {Fore.LIGHTWHITE_EX}" + x5)
            print(f"{Fore.LIGHTCYAN_EX}Username: {Fore.LIGHTWHITE_EX}" + x6)
            print(f"{Fore.LIGHTCYAN_EX}Display Name: {Fore.LIGHTWHITE_EX}" + x7)
            print(f"{Fore.LIGHTGREEN_EX}=============< Username History >=============")
            print(f"{Fore.LIGHTWHITE_EX}"+str(f3['data']))
            
        elif choice == "2":
            print("Please Username")
            uname = input(f"{Fore.LIGHTWHITE_EX}╚══[{Fore.LIGHTCYAN_EX}Username{Fore.LIGHTWHITE_EX}]══> ")

            r0 = urlopen(f"https://api.roblox.com/users/get-by-username?username=" + uname)
            d0 = r0.read()
            f0 = json.loads(d0)
            uid = str(f0['Id'])

            r1 = urlopen(f"https://users.roblox.com/v1/users/" + uid)
            d1 = r1.read()
            f = json.loads(d1)

            r2 = urlopen(f"https://users.roblox.com/v1/users/" + uid + "/status")
            d2 = r2.read()
            f2 = json.loads(d2)

            r3 = urlopen(f"https://users.roblox.com/v1/users/" + uid + "/username-history")
            d3 = r3.read()
            f3 = json.loads(d3)

            x1 = str(f['description'])
            x2 = str(f['created'])
            x3 = str(f['isBanned'])
            x4 = str(f['externalAppDisplayName'])
            x5 = str(f['id'])
            x6 = str(f['name'])
            x7 = str(f['displayName'])
            x8 = str(f2['status'])
            print(f"{Fore.LIGHTGREEN_EX}=============< Information >=============")
            print(f"{Fore.LIGHTCYAN_EX}Profile Link: {Fore.LIGHTWHITE_EX}" + f"https://www.roblox.com/users/" + x5 + "/profile")
            print(f"{Fore.LIGHTCYAN_EX}Description: {Fore.LIGHTWHITE_EX}" + x1)
            print(f"{Fore.LIGHTCYAN_EX}Status: {Fore.LIGHTWHITE_EX}" + x8)
            print(f"{Fore.LIGHTCYAN_EX}Created: {Fore.LIGHTWHITE_EX}" + x2)
            print(f"{Fore.LIGHTCYAN_EX}Banned: {Fore.LIGHTWHITE_EX}" + x3)
            print(f"{Fore.LIGHTCYAN_EX}External App Display Name: {Fore.LIGHTWHITE_EX}" + x4)
            print(f"{Fore.LIGHTCYAN_EX}User ID: {Fore.LIGHTWHITE_EX}" + x5)
            print(f"{Fore.LIGHTCYAN_EX}Username: {Fore.LIGHTWHITE_EX}" + x6)
            print(f"{Fore.LIGHTCYAN_EX}Display Name: {Fore.LIGHTWHITE_EX}" + x7)
            print(f"{Fore.LIGHTGREEN_EX}=============< Username History >=============")
            print(f"{Fore.LIGHTWHITE_EX}"+str(f3['data']))

    else:
        print("")
        Design()

ResetTool()
