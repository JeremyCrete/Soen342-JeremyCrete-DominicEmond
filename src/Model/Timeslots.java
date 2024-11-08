package Model;

public class Timeslots {

	private String startTime;
	private String endTime;

	public Timeslots(String startTime, String endTime) {

		this.startTime = startTime;
		this.endTime = endTime;
	}

	public String getStartTime() {
		return startTime;
	}

	public void setStartTime(String startTime) {
		this.startTime = startTime;
	}

	public String getEndTime() {
		return endTime;
	}

	public void setEndTime(String endTime) {
		this.endTime = endTime;
	}

	public boolean equals(Timeslots aTimeslot) {
		return this.startTime.equals(aTimeslot.startTime) &&
				this.endTime.equals(aTimeslot.endTime);
	}

}
