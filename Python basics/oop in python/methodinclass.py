class Student:
    Roll =""
    Gpa=""

    def set_value(self,Roll ,Gpa):
        self.Roll=Roll
        self.Gpa=Gpa
    def display(self):
        print(f"Roll={self.Roll}, Gpa={self.Gpa}")

Rahim=Student()
Rahim.set_value(101,3.75)
Rahim.display()

Karim=Student()
Karim.set_value(102,3.70)
Karim.display()