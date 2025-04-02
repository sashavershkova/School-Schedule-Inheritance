from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        basic_summary = super().summary()
        transportation_message = "gets" if self.gets_transportation else "does not get"
        return basic_summary + f" {self.name} {transportation_message} transportation."

