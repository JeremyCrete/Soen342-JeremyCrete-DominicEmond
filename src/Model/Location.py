class Location:
    def __init__(self, name, city, address, capacity, venue):
        self.name = name
        self.city = city
        self.address = address
        self.capacity = capacity
        self.venue = venue
    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_address(self):
        return self.address

    def get_capacity(self):
        return self.capacity

    def get_venue(self):
        return self.venue

    def set_name(self, name):
        self.name = name

    def set_city(self, city):
        self.city = city

    def set_address(self, address):
        self.address = address

    def set_capacity(self, capacity):
        self.capacity = capacity

    def set_venue(self, venue):
        self.venue = venue

    def __eq__(self, other):
        if isinstance(other, Location):
            return (self.name == other.name and
                    self.address == other.address and
                    self.city == other.city and
                    self.venue == other.venue and
                    self.capacity == other.capacity)
        return False

    def __str__(self):
        return (f"Location(name={self.name}, city={self.city}, address={self.address}, "
                f"capacity={self.capacity}, venue={self.venue})")
