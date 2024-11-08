package Model;

public class Schedule {

    private String startDate;
    private String endDate;

    public Schedule(String endDate, String startDate) {
        this.endDate = endDate;
        this.startDate = startDate;
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

    public boolean equals(Schedule anotherSchedule) {
        return this.startDate.equals(anotherSchedule.startDate) && this.endDate.equals(anotherSchedule.endDate);
    }

}
