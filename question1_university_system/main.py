from faculty import Professor, TA, Lecturer
from student import Student, UndergraduateStudent, SecureStudentRecord
from person import Person, Staff

# Demonstration
# Create objects

prof = Professor("Dr. Smith", 50, "F101", "Physics")
ug_student = UndergraduateStudent("Alice", 20, "S1001", 2)
ta = TA("Bob", 28, "F102", "Math 101")

# Call methods to demonstrate inheritance
prof.display_info()       # From Person
prof.faculty_info()       # From Faculty
prof.professor_info()     # From Professor

ug_student.display_info() # From Person
ug_student.student_info() # From Student
ug_student.undergrad_info() # From UndergraduateStudent

ta.display_info()         # From Person
ta.faculty_info()         # From Faculty
ta.ta_info()              # From TA

#Enhanced student class

s1 = UndergraduateStudent("Alice", 20, "S123", 2)
s1.enroll_course("Math101")
s1.enroll_course("History201")

s1.set_grade("Math101", "A")
s1.set_grade("History201", "B+")

print("GPA:", s1.calculate_gpa())  # → GPA: 3.65
print("Status:", s1.get_academic_status())  # → Dean's List

# SecureStudentRecord

secure_s1 = SecureStudentRecord("S789", "Charlie", 21)

# Set age and GPA with validation
secure_s1.set_age(22)
secure_s1.set_gpa(3.9)

# Enroll in courses
secure_s1.enroll_course("CS101")
secure_s1.enroll_course("Math202")

print("----- Secure Student Record -----")
print("ID:", secure_s1.get_student_id())
print("Name:", secure_s1.get_name())
print("Age:", secure_s1.get_age())
print("GPA:", secure_s1.get_gpa())
print("Courses:", secure_s1.get_courses())

# Drop a course
secure_s1.drop_course("Math202")
print("Updated Record:", secure_s1.student_info())

# Demonstrating polymorphism
people = [
    Person("Generic Person", 40),
    Staff("Alice", 35, "S001"),
    Student("Bob", 20, "ST123"),
    TA("Charlie", 45, "T001", "Mathematics")
]

for person in people:
    person.display_info()
    print("Responsibilities:", person.get_responsibilities())
    print("-" * 40)

faculty_members = [
    Professor("Dr. Smith", 50, "F001", "Physics"),
    Lecturer("Dr. Johnson", 40, "F002", "Computer Science"),
    TA("Alice", 25, "F003", "Mathematics")
]

for member in faculty_members:
    member.display_info()
    member.faculty_info()
    print("Workload:", member.calculate_workload())
    print("-" * 40)

# Course registration system

from department import Department, Course

cs_dept = Department("Computer Science")

cs101 = Course("CS101", max_students=2)
cs102 = Course("CS102", max_students=2, prerequisites=[cs101])

cs_dept.add_course(cs101)
cs_dept.add_course(cs102)

cs_dept.department_info()

cs101.course_info()
cs102.course_info()
