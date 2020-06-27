class BaseClass:
    def __init__(self):
        print("Baseinit")

    def setname(self, name):
        print("base class set name")
        self.name = name


class subClass(BaseClass):
    def __init__(self):
        # BaseClass.__init__(self)    #to work base class init
        super().__init__()  # standard way to call init
        print("subclassinit")  # constructor override

    def setname(self, name):
        print("sub class set name")  # method overide
        # self.name = name
        super(subClass, self).setname()

    def welcome(self):
        print("welcome")

    def displayname(self):
        print("name " + self.name)


# x = BaseClass()

y = subClass()

y.welcome()
y.setname("sukumar")
y.displayname()
