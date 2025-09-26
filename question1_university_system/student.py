from person import Person

#Student class
#Inherited from person

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = {}  
    
    def student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled Courses: {list(self.courses.keys())}")

    def get_responsibilities(self):
        return "Attend classes, complete assignments, and study."

    # Enroll in a new course
    def enroll_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None  # No grade yet
            print(f"{self.name} has enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    # Drop an existing course
    def drop_course(self, course_name):
        if course_name in self.courses:
            del self.courses[course_name]
            print(f"{self.name} has dropped {course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    # Update grade for a course
    def set_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Grade updated for {course_name}: {grade}")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    # GPA Calculation (assume 4.0 scale)
    def calculate_gpa(self):
        graded_courses = {c: g for c, g in self.courses.items() if g is not None}
        if not graded_courses:
            print("No grades available to calculate GPA.")
            return 0.0

        grade_points = {
            "A": 4.0, "A-": 3.7,
            "B+": 3.3, "B": 3.0, "B-": 2.7,
            "C+": 2.3, "C": 2.0, "C-": 1.7,
            "D+": 1.3, "D": 1.0,
            "F": 0.0
        }

        total_points = sum(grade_points.get(grade, 0) for grade in graded_courses.values())
        gpa = total_points / len(graded_courses)
        return round(gpa, 2)

    # Academic Status
    def get_academic_status(self):
        gpa = self.calculate_gpa()
        if gpa == 0:
            return "No Status (No grades yet)"
        elif gpa >= 3.7:
            return "Dean's List"
        elif gpa >= 2.0:
            return "Good Standing"
        else:
            return "Probation"


# Undergraduate Student class
# Inherited from Student class

class UndergraduateStudent(Student):
    def __init__(self, name, age, student_id, year):
        super().__init__(name, age, student_id)
        self.year = year
    
    def undergrad_info(self):
        print(f"Undergraduate Year: {self.year}")


# Graduate Student class
# Inherited from Student class

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic
    
    def graduate_info(self):
        print(f"Graduate Research Topic: {self.research_topic}")


# SecureStudentRecord (Encapsulation + Validation)

class SecureStudentRecord:
    def __init__(self, student_id, name, age):
        self.__student_id = student_id   # private
        self.__name = name               # private
        self.__age = age                 # private
        self.__gpa = 0.0                 # private
        self.__courses = []              # private list of enrolled courses
        self.__max_courses = 6           # enrollment limit

    # Getter methods
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gpa(self):
        return self.__gpa

    def get_courses(self):
        return list(self.__courses)  # return a copy for safety

    # Setter methods with validation
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer.")

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = round(gpa, 2)
        else:
            raise ValueError("GPA must be between 0.0 and 4.0.")

    # Course management with integrity checks
    def enroll_course(self, course_name):
        if len(self.__courses) >= self.__max_courses:
            raise ValueError("Enrollment limit reached. Cannot enroll in more than 6 courses.")
        if course_name not in self.__courses:
            self.__courses.append(course_name)
        else:
            raise ValueError(f"Already enrolled in {course_name}.")

    def drop_course(self, course_name):
        if course_name in self.__courses:
            self.__courses.remove(course_name)
        else:
            raise ValueError(f"Cannot drop {course_name} — not enrolled.")

    # Representation
    def student_info(self):
        return {
            "ID": self.__student_id,
            "Name": self.__name,
            "Age": self.__age,
            "GPA": self.__gpa,
            "Courses": self.__courses
        } 