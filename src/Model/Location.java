package Model;

public class Location {

    private String name;
    private String city;
    private String address;
    private int capacity;
    private VenueType venue;

    public Location(String name, String city, String address, int capacity, VenueType venue) {
        this.name = name;
        this.city = city;
        this.address = address;
        this.capacity = capacity;
        this.venue = venue;
    }

    public String getName() {
        return name;
    }

    public String getCity() {
        return city;
    }

    public String getAddress() {
        return address;
    }

    public int getCapacity() {
        return capacity;
    }

    public VenueType getVenue() {
        return venue;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public void setVenue(VenueType venue) {
        this.venue = venue;
    }

    public boolean equals(Location aLocation) {
        return this.name.equals(aLocation.name) && this.address.equals(aLocation.address) &&
                this.city.equals(aLocation.city) && this.venue.equals(aLocation.venue) &&
                this.capacity == aLocation.capacity;
    }
}