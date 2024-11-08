package Model;

import java.util.Arrays;

public class Instructor {

    private String name;
    private String phoneNumber;
    private String startDate;
    private String endDate;
    private String[] specialization;

    public Instructor(String name, String phoneNumber, String endDate, String startDate, String[] specialization) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.endDate = endDate;
        this.startDate = startDate;
        this.specialization = specialization;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getStartDate() {
        return startDate;
    }

    public void setStartDate(String startDate) {
        this.startDate = startDate;
    }

    public String getEndDate() {
        return endDate;
    }

    public void setEndDate(String endDate) {
        this.endDate = endDate;
    }

    public String[] getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String[] specialization) {
        this.specialization = specialization;
    }

    public boolean equals(Instructor anotherInstructor) {
        return this.name.equals(anotherInstructor.name) && this.phoneNumber.equals(anotherInstructor.phoneNumber) &&
                Arrays.equals(this.specialization, anotherInstructor.specialization) &&
                this.startDate.equals(anotherInstructor.startDate) && this.endDate.equals(anotherInstructor.endDate);
    }

}
