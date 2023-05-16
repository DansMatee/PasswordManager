###################################################
###################################################
######                                       ######
######       DigiCore Password Manager       ######
######        Author: Daniel Americo         ######
######      Development Date: 26/09/2022     ######
######                                       ######
###################################################
###################################################

import getpass, json, os, subprocess
from time import sleep
from os.path import exists

def cls(): # Helper function to clear the console
    os.system('cls' if os.name=='nt' else 'clear')

def addSpace(): # Helper function to add an extra space to the console
    print('')

def copy2clip(txt):
    subprocess.run("clip", universal_newlines=True, input=txt)

def splashScreen(): # Creates a splash screen to display a Logo and Copyright
    print(f"  _____  _       _  _____                 _______          __")
    print(f" |  __ \(_)     (_)/ ____|               |  __ \ \        / /")
    print(f" | |  | |_  __ _ _| |     ___  _ __ ___  | |__) \ \  /\  / / ")
    print(f" | |  | | |/ _` | | |    / _ \| '__/ _ \ |  ___/ \ \/  \/ /  ")
    print(f" | |__| | | (_| | | |___| (_) | | |  __/ | |      \  /\  /   ")
    print(f" |_____/|_|\__, |_|\_____\___/|_|  \___| |_|       \/  \/    ")
    print(f"            __/ |                                            ")
    print(f"           |___/                                             ")
    print(f"Created by Apps2U 2022©")

def startScreen(): # Loads information for the user to operate the program
    splashScreen()
    addSpace()
    print(f"Welcome to DigiCore Password Manager, use the following commands to interact with the program.")
    addSpace()
    print("[a]dd password | [v]iew all passwords | [q]uit")
    

def checkFile(): # Checking if the passwords.json file exists, and if not creates it and populates it with the table parenthesis []
    if not exists("passwords.json"):
        with open("passwords.json", "w") as f:
            json.dump([], f)

def addPass(): # Adding a new password
    addSpace()
    username = input("[*] Username: ")
    if not username: # Check if username is empty
        print("Username can't be empty!")
        addPass() # Goes back to the beginning of the function
    password = getpass.getpass("[*] Password: ")
    if not password: # Check if password is empty
        print("Password can't be empty!")
        addPass() # Goes back to the beginning of the function
    source = input("[*] Site/Resource Name: ")
    print("Added Credentials! Returning home...") 

    obj = { # Creates a dictionary object to parse with json
        "username": username,
        "password": password,
        "source": source
    }

    with open("passwords.json", 'r') as f: # Opens the passwords.json file with read permissions (r) and loads its contents into the data variable
        data = json.load(f)
    data.append(obj) # Inserts the created dictionary object into the data variable
    with open("passwords.json", 'w') as f: # Opens the passwords.json file with write permissions (w) and dumps the new contents of the data variable into the file
        json.dump(data, f)
    sleep(1.5)
    main()

def selectPass(data, index):
    cls()
    splashScreen()
    print("Username".center(30) + "|" + "Password".center(30) + "|" + "Source".center(30)) # Adds headings with spacing to the console
    print(data[index]['username'].center(30) + "|" + data[index]['password'].center(30) + "|" + data[index]['source'].center(30))
    print("Copy [u]sername | Copy [p]assword | Copy [s]ource | [b]ack to menu")

    while True:
        controlVar = input("[*] Action: ")
        if controlVar == 'u':
            copy2clip(data[index]['username'])
            continue
        elif controlVar == 'p':
            copy2clip(data[index]['password'])
            continue
        elif controlVar == 's':
            copy2clip(data[index]['source'])
            continue
        elif controlVar == 'b':
            getPasses()
            break
        else:
            print("Not a valid argument!")



def deletePass(index): # Deletes a password in the specified index
    with open("passwords.json", 'r') as f: # Opens the passwords.json file with read permissions (r) and loads its contents into the data variable
        data = json.load(f)
    data.pop(index) # Pops (deletes) the specified index from the contents 
    with open("passwords.json", 'w') as f: # Opens the passwords.json file with write permissions (w) and dumps the new contents of the data variable into the file
        json.dump(data, f)
    main()


def getPasses(): # Displays all passwords that have been added
    cls()
    splashScreen()
    with open("passwords.json", 'r') as f: # Opens the passwords.json file with read permissions (r) and loads its contents into the data variable
        data = json.load(f)
    
    print("Entry ID".center(30) + "|" + "Username".center(30) + "|" + "Source".center(30)) # Adds headings with spacing to the console

    lid = 0 # Sets the list index to 0

    for item in data: # Loops through the contents of data, and gets each individual item
        user = item['username']
        pw = item['password']
        src = item['source']
        #print(f'{user:10} | {pw:20}')
        print(str(lid).center(30) + "|" + user.center(30) + "|" + src.center(30)) # Prints the individual item and seperates its contents into the categories
        lid = lid + 1 # increments the list index by 1 to have a correct index
    
    addSpace()
    print("[s]elect entry | [d]elete entry | [b]ack to menu")

    while True:
        controlVar = input("[*] Action: ")
        if controlVar == 's':
            selPassId = int(input("[*] Entry ID: "))
            if selPassId > lid - 1: # Checks if the id the user has entered exists in the list index
                print("Not a valid index!")
                continue
            else:
                selectPass(data, selPassId)
                break
        elif controlVar == 'd':
            delPassId = int(input("[*] Entry ID: "))
            if delPassId > lid - 1: # Checks if the id the user has entered exists in the list index
                print("Not a valid index!")
                continue
            else:
                deletePass(delPassId) # Sends the id to the delete function to be deleted
                break      
        elif controlVar == 'b':
            main()
            break
        else:
            print("Not a valid argument!")

def main():
    cls()
    checkFile()
    startScreen()

    while True:
        controlVar = input()
        if controlVar == 'a':
            addPass()
            break
        elif controlVar == 'v':
            getPasses()
            break
        elif controlVar == 'q':
            quit()
        else:
            print("Not a valid argument!")

main()

# Reviewed by [Daniel Americo | 27/09/2022]
# Completed 27/09/2022
# Final version number: 1.0

# This program is created for DigiCore as a password manager. Users can view, add and delete passwords that they have saved.
# The script can be ran by [py app.py] and requires no cmd args to work properly. All in program commands are shown to the user on the correct page.
# A help menu should be implemented to give an overview over all commands, and a manual page should also be created to give the user an in program explanation.

