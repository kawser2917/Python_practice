class Student:
    Roll=""
    Gpa=""
    def __init__(self,roll,gpa):
        self.Roll=roll
        self.Gpa=gpa
    def display(self):
        print(f"Roll={self.Roll}, Gpa={self.Gpa}")

Rahim=Student(101,3.75)
Rahim.display()

Karim=Student(102,3.70)
Karim.display()