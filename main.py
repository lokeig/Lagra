from User import *
from menu import *

users = loadJson("users.json")
userID = None

while True: 
    userID = loginScreen(users)
    mainScreen(userID, users)