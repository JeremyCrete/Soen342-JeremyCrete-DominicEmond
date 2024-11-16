class Instructor:
    def __init__(self, name, phone_number, start_date, end_date, specialization):
        self.name = name
        self.phone_number = phone_number
        self.start_date = start_date
        self.end_date = end_date
        self.specialization = specialization

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, specialization):
        self.specialization = specialization

    def __eq__(self, other):
        if isinstance(other, Instructor):
            return (self.name == other.name and 
                    self.phone_number == other.phone_number and 
                    self.start_date == other.start_date and 
                    self.end_date == other.end_date and 
                    self.specialization == other.specialization)
        return False
