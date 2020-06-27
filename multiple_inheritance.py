class First:
    def displayfirst(self):
        print("hai")


class Second:
    def displaysecond(self):
        print("hello")


class Third(First, Second):
    def display_third(self):
        print("third")


x = Third()
x.display_third()
x.displayfirst()
print(Third.mro())

# if same method name first will work first ie when the time it finds no other will be excecuted
# method resolution order
