class CLient:
    name: str
    phoneNumber: int
    age: int

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_phoneNumber(self):
        return self.phoneNumber
    
    def set_phoeNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def __eq__(self, obj):
        if not isinstance(obj, CLient):
            return False
        return (self.age == obj.age and self.name == obj.name and self.phoneNumber == obj.phoneNumber)
