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
        