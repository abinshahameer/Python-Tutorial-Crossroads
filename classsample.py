class MySampleClass:
    year = 2020

    def hello(self, n):
        self.name = n
        print("hello " + n)

    def printname(self):
        print(self.name)

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
        print('hello' + self.name + str(self.age) + self.place)

    def addage(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("year " + str(MySampleClass.year))
        print("name" + self.name)
        print("age" + str(self.age))
        print("place" + self.place)


x = MySampleClass("suku", 21, "delhi")
y = MySampleClass("chanddran", 21, "kollam")
name = "abinshah"
x.hello(name)
x.printname()
y.hello("heloo")
MySampleClass.year = MySampleClass.year + 1
x.display()
y.display()
