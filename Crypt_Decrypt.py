import os
import pyAesCrypt
from colorama import Fore, init


def crypt(filetocrp, password):
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(filetocrp), str(filetocrp) + ".crp", password, bufferSize)
    os.remove(filetocrp)

def decrypt(filetocrp, password):
    bufferSize = 512*1024
    pyAesCrypt.decryptFile(str(filetocrp), str(os.path.splitext(filetocrp)[0]), password, bufferSize)
    os.remove(filetocrp)

init()
print("")
print(Fore.GREEN + "___________________________________________________________________________________________________")
print("")
print(Fore.GREEN + " _   _    _    ____ _  _______ _   _ _____ ____  _        _    _   _ _____  _____ ")
print(Fore.GREEN + "| | | |  / \  / ___| |/ /_   _| | | | ____|  _ \| |      / \  | \ | | ____||_   _|")
print(Fore.GREEN + "| |_| | / _ \| |   | ' /  | | | |_| |  _| | |_) | |     / _ \ |  \| |  _|    | |  ")
print(Fore.GREEN + "|  _  |/ ___ \ |___| . \  | | |  _  | |___|  __/| |___ / ___ \| |\  | |___   | |  ")
print(Fore.GREEN + "|_| |_/_/   \_\____|_|\_\ |_| |_| |_|_____|_|   |_____/_/   \_\_| \_|_____|  |_|  ")
print("")
print("___________________________________________________________________________________________________")

print("")
print(Fore.GREEN + "1:Crypt")
print("")
print(Fore.GREEN + "2:DeCrypt")
print("")

choice = int(input("Enter Number: "))

while 1 == 1:
    if choice == 1:
        fileto = input("Path/to/file: ")
        password = input("Input Pass: ")
        crypt(fileto, password)

    if choice == 2:
        fileto = input("Path/to/file: ")
        password = input("Input Pass: ")
        decrypt(fileto, password)