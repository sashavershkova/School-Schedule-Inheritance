from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        basic_summary = super().summary()
        transportation_message = "Has" if self.gets_transportation else "Has not"
        return basic_summary + f" {transportation_message} transportation."

