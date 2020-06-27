class sample:
    def set_name(self, name):
        self.name = name

    def __add__(self, other):
        name = self.name + " " + other.name
        return name


firstname = sample()
secondname = sample()
firstname.set_name("abinshah")
secondname.set_name("ameer")
fullname = firstname + secondname
print(fullname)
