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
