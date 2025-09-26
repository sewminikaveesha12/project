from person import Person

# Faculty class
# Inherited from Person
class Faculty(Person):
    def __init__(self, name, age, faculty_id):
        super().__init__(name, age)
        self.faculty_id = faculty_id
    
    def faculty_info(self):
        print(f"Faculty ID: {self.faculty_id}")

    def calculate_workload(self):
        return "General faculty workload."

# Professor class
# Inherited from Faculty
class Professor(Faculty):
    def __init__(self, name, age, faculty_id, subject):
        super().__init__(name, age, faculty_id)
        self.subject = subject
    
    def professor_info(self):
        print(f"Professor of {self.subject}")

    def calculate_workload(self):
        return f"Teaching advanced {self.subject} courses, supervising research, publishing papers."

# Lecturer class
# Inherited from Faculty

class Lecturer(Faculty):
    def __init__(self, name, age, faculty_id, department):
        super().__init__(name, age, faculty_id)
        self.department = department
    
    def lecturer_info(self):
        print(f"Lecturer in {self.department} department")

    def calculate_workload(self):
        return f"Conducting lectures, preparing course material, grading in {self.department}."

# TA (Teaching Assistant) class
# Inherited from Faculty

class TA(Faculty):
    def __init__(self, name, age, faculty_id, course):
        super().__init__(name, age, faculty_id)
        self.course = course
    
    def ta_info(self):
        print(f"Teaching Assistant for {self.course}")

    def calculate_workload(self):
        return f"Assisting in {self.course} labs, grading assignments, holding office hours."