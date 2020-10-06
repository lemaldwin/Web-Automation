
class Account():
    def __init__(self):
        self.username="hydro_gorgo"
        self.password="Gorgo0330"
    
    def setPassword(self, password):
        self.password = password

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def getUsername(self):
        return self.username
    
    def saveAccount(self):
        #write account to a text file or database
        pass

