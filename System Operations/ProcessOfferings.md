## System Operation #1:
`NewLessonToOffer(lessonType, mode);`
### Operation Contract:
`NewLessonToOffer`
### Cross Reference:
Use Case - Process Offerings
### Pre Conditions:
- The Diffrent lessons must be defined
- `mode` has to be one of the accepted lesson modes
### Postconditions: 
- If `lessonType` is invalid then a invalidLeasson message will be returned
- If `lessonType` is valid then it will specify the location of the lesson

## System Operation #2:
`findLocation(location);`

### Operation Contract:
`findLocation`

### Cross Reference:
Use Case - Process Offerings

### Preconditions:
- `location` must be a valid and existing location within the system.

### Postconditions:
- If `location` is at maximum capacity, a `LocationMaxedOut` message will be returned.
- If `location` is available, the available time slots for the location are provided.

## System Operation #3:
`SpecificTime(Schedule);`

### Operation Contract:
`SpecificTime`

### Cross Reference:
Use Case - Process Offerings

### Preconditions:
- `Schedule` must contain a valid format for time slots and dates.
- The location for the lesson must be available at the specified time in the schedule.

### Postconditions:
- The system records the specific schedule and time slots for the lesson.
- A confirmation message is sent to indicate the time slots have been successfully scheduled.

## System Operation #4:
`searchLessons();`

### Operation Contract:
`searchLessons`

### Cross Reference:
Use Case - Process Offerings

### Preconditions:
- The instructor must be logged into the system and have the necessary privileges to search for lessons.

### Postconditions:
- If no lessons are available, a `No Lesson Available` message will be returned.
- If lessons are available, the system provides a list of lessons and their schedules.

## System Operation #5:
`setInstructor(i);`

### Operation Contract:
`setInstructor`

### Cross Reference:
Use Case - Process Offerings

### Preconditions:
- The instructor `i` must be registered and have the appropriate credentials for the lesson type.

### Postconditions:
- The instructor is assigned to the specified lesson.
- A confirmation message is sent, indicating that the instructor has been successfully set for the lesson.
 
