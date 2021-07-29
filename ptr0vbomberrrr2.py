import requests, random, datetime, sys, time, os

from termcolor import colored
from modules import start

def bomber():
    os.system("cd bombers && python3 bomber.py")

def creator():
    print(start.creator)
    input()
    main()

def update():
    os.system("cd modules && python3 update.py")

def exit():
    os.system("clear")
    print('Пока-Пока!...)')
    sys.exit()

def main():
    os.system('clear')
    print(start.banner)
    print(start.menu)
    num_menu = input("iisus> ")
    if num_menu == "":
       main()
    if num_menu == "1":
        bomber()
    if num_menu == "2":
        creator()
    if num_menu == "3":
        update()
    if num_menu == "4":
        exit()
main()
