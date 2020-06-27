class First:
    def displayfirst(self):
        print("hai")


class Second(First):
    def displaysecond(self):
        print("hello")


class Third(Second):
    def display_third(self):
        print("third")


x = Third()
x.display_third()
x.displayfirst()
