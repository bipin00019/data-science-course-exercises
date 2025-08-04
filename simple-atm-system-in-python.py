import json
import os

def register():
    username = input("Enter user name : ")
    pin = int(input("Enter pin : "))
    confirm_pin = int(input("Confirm pin : "))

    if pin == confirm_pin:
        print("Looking for:", os.path.abspath("atm_system_credentials.txt"))
        try:
            file = open("atm_system_credentials.txt", 'r')
            content = file.read()
            file.close()
        except FileNotFoundError:
            content = ""

        credentials = content.split("-")
        for i in credentials :
            if i != "":
                dict_credentials = json.loads(i)
                if username in dict_credentials :
                    print("Username already exist. Try using unique username")
                    return

        file = open("atm_system_credentials.txt", 'a')
        dict_credentials = {username : pin}
        json_credentials = json.dumps(dict_credentials)
        file.write(json_credentials + "-")
        file.close()

        file = open("balance.txt", "a")
        dict_balance = {username : 0}
        json_balance = json.dumps(dict_balance)
        file.write(json_balance + "-")
        file.close()

        print("Registration successfull")
    else : 
        print("Pin didn't match")           
        
def withdraw(username):
    file = open("balance.txt",'r')
    content = file.read()
    file.close()
    
    balance_data = content.split("-")
    new_content = ""

    for i in balance_data:
        if i != "":
            dict_balance = json.loads(i)
            if username in dict_balance :
                amount = int(input("Enter amount to deposit : "))
                dict_balance[username] -= amount
                print(f"Withdrew : {amount}")
            new_content += json.dumps(dict_balance) + "-"

    file= open("balance.txt", "w")
    file.write(new_content)
    file.close

def deposit(username) :
    file = open("balance.txt",'r')
    content = file.read()
    file.close()
    
    balance_data = content.split("-")
    new_content = ""

    for i in balance_data:
        if i != "":
            dict_balance = json.loads(i)
            if username in dict_balance :
                amount = int(input("Enter amount to deposit : "))
                dict_balance[username] += amount
                print(f"Deposited : {amount}")
            new_content += json.dumps(dict_balance) + "-"

    file= open("balance.txt", "w")
    file.write(new_content)
    file.close

def view_balance(username):
    file = open("balance.txt",'r')
    content = file.read()
    file.close()
    
    balance_data = content.split("-")
    
    for i in balance_data :
        if i != "":
            dict_balance = json.loads(i)
            if username in dict_balance :
                print(f"Your balance : {dict_balance[username]}")
                return dict_balance[username]

def login():
    username = input("Enter user name : ")
    pin = int(input("Enter pin : "))

    try:
        file = open("atm_system_credentials.txt", 'r')
        content = file.read()
        file.close()
    except FileNotFoundError:
        print("File not found")
        return False

    credentials = content.split("-")

    for i in credentials:
        if i != "":
            dict_credentials = json.loads(i)
            if username in dict_credentials and dict_credentials[username] == pin :
                print("Login successful")
                while True :
                    try : 
                        user_choice = int(input("Enter \n1 to deposit : \n2 to withdraw : \n3 to view balance \n4 to logout : \n"))
                        match user_choice:
                            case 1:
                                deposit(username)
                            case 2 :
                                withdraw(username)
                            case 3 :
                                view_balance(username)
                            case 4 : 
                                print("Logged out")
                                break
                            case _:
                                print("Invalid input")
                    except ValueError :
                        print("Please enter number")
                return
    print("Invalid credential")
while True :
    user_input = input("Press l to login, r to register and e to exit :").lower().strip()
    match user_input:
        case 'l' :
            login()
        case 'r' :
            register()
        case 'e' :
            print("Bye....Thankyou")
            break
        case _:
            print("Invalid input.")
