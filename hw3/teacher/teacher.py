from hw3.courses_owner import CoursesOwner


class Teacher(CoursesOwner):
    def __init__(self, name: str, surname: str, age: int) -> None:
        super().__init__(name, surname, age)