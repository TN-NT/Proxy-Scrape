# Author : NAOY-TIAGZ
# Discord : NAOY#0001 </> TIAGZ#0001
# Github : https://github.com/NAOYY ... https://github.com/tn-nt
#module
from urllib.request import Request, urlopen
from base64 import b64decode
import requests
import urllib
import ctypes
import webbrowser
import os 
import shlex
import time
import json
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()
#module début du script

os.system('cls')
print(Fore.RED + 'Checking for new updates...')
time.sleep(3)
version = "https://pastebin.com/raw/puBjLeyn"
actuel_version = 0.1
r = requests.get(version)
texte = r.text

if texte != str(actuel_version):
    print(Fore.YELLOW + "La version ",actuel_version, "n'est pas à jour!")
    print(Fore.CYAN + 'Fermeture dans 5 seconds')
    time.sleep(2)
    webbrowser.open('https://discord.gg/EYVyCqb4Qg')
    time.sleep(3)
    exit()


os.system('cls')
time.sleep(1) # Sleep for 3 seconds

print(Fore.YELLOW + "La version ",actuel_version, "est à jour! merci d'utiliser ce tools...")
print(Fore.CYAN + 'WELCOME TO THE NSI SCRAPER ITS A PROXY SCRAPER USED API KEY MADE BY NAOY#0001 AND </> TIAGZ-UHQ#0001') 
print(Fore.YELLOW + "Version",actuel_version)
time.sleep(1) # Sleep for 3 seconds
os.system('cls')

def get_proxies(type_proxy):
    r = requests.get(url + type_proxy)
    r2 = requests.get(url2 + type_proxy)

    text = r.text
    text2 = r2.text
    text = text.replace("\n","")
    text2 = text2.replace("\n","")

    # EXPORT PROXYS
    with open (f"./output/{type_proxy}.txt","w") as f:
        f.write(text)
        f.write(text2)


    lines = 0
    with open(f'./output/{type_proxy}.txt', 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()
            print('Scraped {} '.format(lines) + 'proxies.')
    

# Proxysscrape
url = "https://api.proxyscrape.com?request=getproxies&proxytype="
# Proxyslist
url2 = "https://www.proxy-list.download/api/v1/get?type="
# ProxyScrape2


print("                                                                                      ╔═══════════════╗ ")
print("                                                                                         Version",actuel_version)
print("                                                                                      ╚═══════════════╝ ")                                                                                                                                                                                
                                                                                        

print("""
		██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗███████╗ ██████╗██████╗  █████╗ ██████╗ 
		██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗
		██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████╗██║     ██████╔╝███████║██████╔╝
		██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ 
		██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ███████║╚██████╗██║  ██║██║  ██║██║     
		╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     
		                                                                                  
		 █████╗ ██████╗ ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗    
		██╔══██╗██╔══██╗██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗   
		███████║██████╔╝██║    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝   
		██╔══██║██╔═══╝ ██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗   
		██║  ██║██║     ██║    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║   
		╚═╝  ╚═╝╚═╝     ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   
                                                                                  
""")
type_proxy = input("                [http] - [https] - [socks4] - [socks5]:   Made by NAOY#0001 and </> TIAGZ-UHQ#0001\n\n\n\n >> ")


#HTTP
if type_proxy == "http" or type_proxy.lower() == "http":
    get_proxies("http")


#HTTPS
elif type_proxy == "https" or type_proxy.lower() == "https":
    get_proxies("https")


#SOCKS4
elif type_proxy == "socks4" or type_proxy.lower() == "socks4":
    get_proxies("socks4")


#SOCKS5
elif type_proxy == "SOCKS5" or type_proxy.lower() == "socks5":
    get_proxies("socks5")
