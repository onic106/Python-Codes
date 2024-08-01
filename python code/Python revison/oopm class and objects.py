class Person:
  name = "Onic"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Onic"
a.occupation = "Accountant"

b.name = "Onic"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()