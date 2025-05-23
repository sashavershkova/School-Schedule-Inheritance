from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

# we have one default parameter - gets_transportation
def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)

    assert ellis.gets_transportation == False

def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Math"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    result = ellis.summary()

    assert result == "Ellis is a junior enrolled in 2 classes: Painting, Math. Ellis gets transportation."

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Math"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=False)
    result = ellis.summary()

    assert result == "Ellis is a junior enrolled in 2 classes: Painting, Math. Ellis does not get transportation."
