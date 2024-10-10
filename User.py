import json

class User:
    def __init__(self, username, password, data):
        self.username = username
        self.password = password
        self.data = data
        
    @classmethod
    def create(person):
        u = str(input("Enter username: "))
        p = str(input("Enter password: "))
        d = []
        return person(u, p, d)
    def getPassword(self):
        return self.password
    
    def getUsername(self):
        return self.username
    
    def getData(self):
        return self.data
    
    def addData(self):
        newItem = str(input("Enter your item: "))
        print("Added: " + newItem)
        dataList = self.data
        dataList.append(newItem)
        
    def deleteData(self):
        dataList = self.data
        if (len(dataList) > 0):
            print("\nCurrent items:")
            for n in range(len(dataList)):
                print(str(n+1) + ") " + dataList[n])
                
            exitChoice = len(dataList)+1
            print("\n" + str(exitChoice)+ ") Exit")
            
            while True:
                try:
                    choice = int(input("\nDelete: "))
                    if (choice > 0 and choice < len(dataList)+1):
                        print("Deleted item: " + dataList[choice-1])
                        dataList.pop(choice-1)
                        break
                    elif (choice == exitChoice):
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid ID, try again")
        else:
            print("\nNo items to delete")
    
def compareUsername(name, arr):
    new = True
    if (len(arr) > 0):
        for n in range(0, len(arr)-1):
            if (name == arr[n].getUsername()):
                new = False
    return new

def updateJson(users):
    userList = []
    for n in range(len(users)):
        userJson = {
            "username": users[n].getUsername(),
            "password": users[n].getPassword(),
            "data": users[n].getData()
        }
        userList.append(userJson)
        
    with open("users.json", "w") as outfile:
        json.dump(userList, outfile, indent = 4)
        
def loadJson(filename):
    users = []
    try:
        with open(filename, "r") as infile:
            jsonList = json.load(infile)
        if isinstance(jsonList, list):
            for userData in jsonList:
                user = User(
                    username=userData["username"],
                    password = userData["password"],
                    data = userData["data"]
                )
                users.append(user)
    except json.JSONDecodeError and FileNotFoundError:
        with open(filename, "w") as outfile:
            json.dump([], outfile)
    return users