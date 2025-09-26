# Base class : Person
class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Polymorphic method to be overridden
    def get_responsibilities(self):
        return "General responsibilities."

# Staff class
# Inherited from Person
class Staff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id
    
    def staff_info(self):
        print(f"Staff ID: {self.staff_id}")

    def get_responsibilities(self):
        return "Manage administrative and academic tasks."

# Teacher class
# Inherited from Staff class

class Teacher(Staff):
    def __init__(self, name, age, staff_id, subject):
        super().__init__(name, age, staff_id)
        self.subject = subject

    def get_responsibilities(self):
        return f"Teach {self.subject} and support students."



