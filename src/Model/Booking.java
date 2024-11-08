package Model;

public class Booking {

    private int bookingId;

    public Booking(int bookingId) {
        this.bookingId = bookingId;
    }

    public int getBookingId() {
        return bookingId;
    }

    public void setBookingId(int bookingId) {
        this.bookingId = bookingId;
    }

    public boolean equals(Booking aBooking) {
        return this.bookingId == aBooking.bookingId;
    }
}