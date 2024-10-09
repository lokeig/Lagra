from User import *
from menu import *

users = [User("admin", "1234", ["Milk", "Bread"])]
userID = None

while True: 
    userID = loginScreen(users)
    mainScreen(userID, users)
            
