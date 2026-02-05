class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):#all part of person come here
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathinh...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        print("I am a Programmer so I am breathing++...")

p = Person()
p.takeBreath()
#print(p.company)# throws an error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)

