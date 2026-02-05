class Employee:
    company = "Visa"
    eCode = 120

class FreeLancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, FreeLancer):
    name = "Harsha"

p = Programmer()
p.upgradeLevel()
#print(p.level)
print(p.company)#print visa because we write first employee because of that
