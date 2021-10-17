import requests
import colorama
import os
from colorama import init, Fore
from time import sleep
import os.path
init()
os.system('cls' if os.name == 'nt' else 'clear')
colorama.init(autoreset=True)

os.system("title Fortnite Info Grabber! /\ Developed by - xdFNLeaks")
# VERSION INFO API
response = requests.get('https://benbot.app/api/v1/status')
version = response.json()['currentCdnVersion']
versionNum = response.json()['currentFortniteVersionNumber']
pakCount = response.json()['totalPakCount']
dynamCount = response.json()['dynamicPakCount']
allPakFiles = response.json()['allPakFiles']
# AES INFO API
response = requests.get('https://benbot.app/api/v1/aes')
versionAES = response.json()['version']
mainKey = response.json()['mainKey']
dynamAES = response.json()['dynamicKeys']

def menu():
        print(f"{Fore.LIGHTCYAN_EX}Welcome to Fortnite Info Grabber!\nCreated by xdFNLeaks\n{Fore.RED}[!] THIS TOOL CANNOT POST TO TWITTER, MAY ADD IN FUTURE\nYou are able to copy & paste any of the info provided using this tool.\nJust dont copy the code! {Fore.LIGHTCYAN_EX}Enjoy!\nEnter a number to get started!\n{Fore.RESET}\n [{Fore.LIGHTYELLOW_EX}1{Fore.RESET}] = {Fore.LIGHTBLUE_EX}Show Version Info{Fore.RESET}\n [{Fore.LIGHTYELLOW_EX}2{Fore.RESET}] = {Fore.LIGHTBLUE_EX}Show AES Info{Fore.RESET}\n [{Fore.LIGHTYELLOW_EX}3{Fore.RESET}] = {Fore.LIGHTBLUE_EX}Search for Any Cosmetic!")
menu()

option = int(input(f"{Fore.LIGHTRED_EX}\nEnter Number: {Fore.RESET}"))

if option == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTGREEN_EX}Current Fortnite Version:\n\n{Fore.LIGHTCYAN_EX}{version}\n\n{Fore.LIGHTCYAN_EX}v{versionNum}0{Fore.LIGHTGREEN_EX}\nTotal Pak Count: {Fore.LIGHTCYAN_EX}{pakCount}\n\n{Fore.LIGHTGREEN_EX}Dynamic Pak Count: {Fore.LIGHTCYAN_EX}{dynamCount}\n{Fore.LIGHTGREEN_EX}All Pak Files Detected: \n\n{Fore.LIGHTCYAN_EX}{allPakFiles}")
        print(f"{Fore.LIGHTGREEN_EX}Done!{Fore.RED}\nFEEL FREE TO COPY & PASTE!")
        exit()
        
elif option == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTGREEN_EX}Current Fortnite Version: \n{Fore.LIGHTCYAN_EX}{versionAES}\n{Fore.LIGHTCYAN_EX}v{versionNum}0\n{Fore.LIGHTGREEN_EX}Main AES Key: \n{Fore.LIGHTCYAN_EX}{mainKey}\n\n{Fore.LIGHTGREEN_EX}Dynamic AES Keys: \n{Fore.LIGHTCYAN_EX}{dynamAES}")
        print(f"{Fore.LIGHTGREEN_EX}Done!{Fore.RED}\nFEEL FREE TO COPY & PASTE!")
        exit()
elif option == 3:
        cosmetic = input(f"Cosmetic Name Please? [>] ")
        response = requests.get(f'https://benbot.app/api/v1/cosmetics/br/search?name={cosmetic}')
        CosmeticID = response.json()['id']
        path = response.json()['path']
        icon = response.json()['icons']['icon']
        name = response.json()['name']
        desc = response.json()['description']
        cosmeticTYPE = response.json()['shortDescription']
        rarity = response.json()['rarity']
        set = response.json()['set']
        setDesc = response.json()['setText']
        gameplayTags = response.json()['gameplayTags']
        variants = response.json()['variants']
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTYELLOW_EX}Cosmetic Name: {Fore.RESET}{name}\n{Fore.LIGHTYELLOW_EX}Cosmetic Description: {Fore.RESET}{desc}\n{Fore.LIGHTYELLOW_EX}Cosmetic ID: {Fore.RESET}{CosmeticID}\n\n{Fore.LIGHTYELLOW_EX}Cosmetic Path: {Fore.RESET}{path}\n\n{Fore.LIGHTYELLOW_EX}Icon URL: {Fore.RESET}{icon}\n\n{Fore.LIGHTYELLOW_EX}Type: {Fore.RESET}{cosmeticTYPE}\n{Fore.LIGHTYELLOW_EX}Rarity: {Fore.RESET}{rarity}\n{Fore.LIGHTYELLOW_EX}Set: {Fore.RESET}{set}\n{Fore.LIGHTYELLOW_EX}Set Description: {Fore.RESET}{setDesc}\n\n{Fore.LIGHTYELLOW_EX}Variants: {Fore.RESET}{variants}\n\n\n{Fore.LIGHTYELLOW_EX}gameplayTags:\n {Fore.LIGHTCYAN_EX}{gameplayTags}\n\n{Fore.LIGHTGREEN_EX}Done!")
        