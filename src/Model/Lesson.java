
package Model;

public class Lesson {
    private String mode;
    private Type lessonType;

    public Lesson(String mode, Type lessonType) {
        this.mode = mode;
        this.lessonType = lessonType;
    }

    public String getMode() {
        return mode;
    }

    public Type getLessonType() {
        return lessonType;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public void setLessonType(Type lessonType) {
        this.lessonType = lessonType;
    }

    public boolean equals(Lesson aLesson) {
        return this.lessonType == aLesson.lessonType && this.mode == aLesson.mode;
    }
}