class MySampleClass:
    def hello(self, n):
        self.name = n
        print("hello " + n)

    def printname(self):
        print(self.name)

    def __init__(self):
        print('hello')


x = MySampleClass()
y = MySampleClass()
name = "abinshah"
x.hello(name)
x.printname()
y.hello("heloo")
