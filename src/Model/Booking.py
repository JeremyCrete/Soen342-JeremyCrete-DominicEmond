class Booking:
    def __init__(self, bookingid):
        self.bookingid = bookingid

    def bookingid(self):
        return self.bookingid

    def bookingid(self, bookingid):
        self.bookingid = bookingid

    def __eq__(self, obj):
        if isinstance(obj, Booking):
            return self.bookingid == obj.bookingid
        return False