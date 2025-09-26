# Course class

class Course:
    def __init__(self, name, max_students=30, prerequisites=None):
        self.name = name
        self.max_students = max_students
        self.prerequisites = prerequisites if prerequisites else []
        self.enrolled_students = []
        self.faculty = None

    def course_info(self):
        faculty_name = self.faculty.name if self.faculty else "TBA"
        print(f"Course: {self.name}, Faculty: {faculty_name}, Enrolled: {len(self.enrolled_students)}/{self.max_students}")

# Department class

class Department:
    def __init__(self, name):
        self.name = name
        self.faculty_list = []
        self.course_list = []
        self.student_list = []

    def add_faculty(self, faculty):
        self.faculty_list.append(faculty)

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def assign_faculty_to_course(self, faculty, course):
        if course not in self.course_list:
            raise ValueError(f"{course.name} not in department")
        if faculty not in self.faculty_list:
            raise ValueError(f"{faculty.name} not in department")
        faculty.assign_course(course)
        course.faculty = faculty
        print(f"{faculty.name} assigned to {course.name}")

    def department_info(self):
        print(f"Department: {self.name}")
        print("Faculty:", [f.name for f in self.faculty_list])
        print("Courses:", [c.name for c in self.course_list])
        print("Students:", [s.name for s in self.student_list])
