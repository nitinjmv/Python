class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_string(self):
        return f"Your name is {self.name} & age is {self.age}"

e1 = Employee("Nitin", 40)
print(e1)
print(e1.to_string())