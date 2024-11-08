package Model;

public class Offering {
    private boolean isFull;
    private boolean isGroupOffering;
    private Type lessonType;

    public Offering(boolean isFull, boolean isGroupOffering, Type lessonType) {
        this.isFull = isFull;
        this.isGroupOffering = isGroupOffering;
        this.lessonType = lessonType;
    }

    public boolean isFull() {
        return isFull;
    }

    public boolean isGroupOffering() {
        return isGroupOffering;
    }

    public Type getLessonType() {
        return lessonType;
    }

    public void setFull(boolean full) {
        isFull = full;
    }

    public void setGroupOffering(boolean groupOffering) {
        isGroupOffering = groupOffering;
    }

    public void setLessonType(Type lessonType) {
        this.lessonType = lessonType;
    }

    public boolean equals(Offering aOffering) {
        return this.isFull == aOffering.isFull && this.isGroupOffering == aOffering.isGroupOffering &&
                this.lessonType == aOffering.lessonType;
    }
}