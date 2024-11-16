class Offering:
    def __init__(self, is_full, is_group_offering, lesson_type):
        self.is_full = is_full
        self.is_group_offering = is_group_offering
        self.lesson_type = lesson_type

    def is_full(self):
        return self.is_full

    def is_group_offering(self):
        return self.is_group_offering

    def get_lesson_type(self):
        return self.lesson_type

    def set_full(self, is_full):
        self.is_full = is_full

    def set_group_offering(self, is_group_offering):
        self.is_group_offering = is_group_offering

    def set_lesson_type(self, lesson_type):
        self.lesson_type = lesson_type

    def __eq__(self, other):
        if isinstance(other, Offering):
            return (self.is_full == other.is_full and
                    self.is_group_offering == other.is_group_offering and
                    self.lesson_type == other.lesson_type)
        return False

    def __str__(self):
        return (f"Offering(is_full={self.is_full}, is_group_offering={self.is_group_offering}, "
                f"lesson_type={self.lesson_type})")
