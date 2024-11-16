class admin:
    def __init__(self, username, password):
        self.password = password
        self.username = username

    def get_username(self):
        return self.username
    
    def set_username(self, username):
         self.username = username

    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password

    def __eq__(self, obj):
        return self.username == obj.username and self.password == obj.password