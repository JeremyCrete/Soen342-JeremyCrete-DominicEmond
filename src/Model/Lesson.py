class Lesson:
    def __init__(self, mode, lesson_type):
        self.mode = mode  
        self.lesson_type = lesson_type  

    def get_mode(self):
        return self.mode

    def get_lesson_type(self):
        return self.lesson_type

    def set_mode(self, mode):
        self.mode = mode

    def set_lesson_type(self, lesson_type):
        self.lesson_type = lesson_type

    def __eq__(self, other):
        if isinstance(other, Lesson):
            return self.lesson_type == other.lesson_type and self.mode == other.mode
        return False
