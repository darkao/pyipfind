#Author: Darkao
#Website IP Finder
import socket

def bul():
    global adres
    ip = socket.gethostbyname(adres)
    print ip


def bann():
    print"""
  _____  _____    ______  _____  _   _  _____   ______  _____  
 |_   _||  __ \  |  ____||_   _|| \ | ||  __ \ |  ____||  __ \ 
   | |  | |__) | | |__     | |  |  \| || |  | || |__   | |__) |
   | |  |  ___/  |  __|    | |  | . ` || |  | ||  __|  |  _  / 
  _| |_ | |      | |      _| |_ | |\  || |__| || |____ | | \ \ 
 |_____||_|      |_|     |_____||_| \_||_____/ |______||_|  \_\
                                                               
    """                                                           
bann()

while(True):
    
    adres = raw_input("Site adresi giriniz: ")
    
    bul()
    
    a = raw_input("Please tap enter...")
    
    if a == "":
        break
