
class Account():
    def __init__(self):
        self.username="useryouremail/usernamehere"
        self.password="password here"
    
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

