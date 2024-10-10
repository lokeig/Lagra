from User import *
import json

def start():
    print("\nOptions")
    print("What do you want to do\n")
    print("1) Create account")
    print("2) Login\n")
    
def loggedInScreen():
    print("\nOptions:")
    print("1) Logout")
    print("2) Add object")
    print("3) Remove object")
    print("4) See objects\n")
    
def login(arr):
    nameInput = input("\nUsername: ")
    passInput = input("Password: ") 
    print("") #Ny rad
    
    s = None
    for n in range(len(arr)):
        if (nameInput == arr[n].getUsername() and passInput == arr[n].getPassword()):
            s = n
    return s

def loginScreen(users):
    userID = None
    while True:
        start()
        choice = input("Choice: ")      
        if (choice == "1"):
            newUser = User.create()
            if (compareUsername(newUser.getUsername(), users)):
                users.append(newUser)
                userID = len(users)-1
                updateJson(users)
                break
            else:
                print("Username already taken")
        elif (choice == "2"):
            userID = login(users)
            if (userID != None):
                print("Login Success.\nWelcome " + str(users[userID].getUsername()))
                break
            else:
                print("Invalid username or password")
        else:
            print("Invalid input")   
    return (userID)
    
def mainScreen(userID, users):
    while True:
        loggedInScreen()
        choice = input("Choice: ")
        currentUser = users[userID]
        if (choice == "1"):
            break
            
        elif (choice == "2"):
            currentUser.addData()
            updateJson(users)
            
        elif (choice == "3"):
            currentUser.deleteData()
            updateJson(users)
        
        elif (choice == "4"):
            allItems = ""
            if (len(currentUser.getData()) > 0):
                for n in range(len(currentUser.getData())):
                    if (n != 0):
                        allItems += (", ")
                    allItems += currentUser.getData()[n]
                print("Current objects: " + allItems)
            else:
                print("You have no items")