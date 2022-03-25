# Object Oriented programming(OOP)

# Object Oriented programming(OOP) is a programming paradigm
# that relies on the concept of classes and objects.
# It is used to structure a software program into simple,
# reusable pieces of code blueprints(usually called classes),
# which are used to create individual instances of objects.
# usable code blueprints/classes which can be used to create individual instances of objects
# An object is simply a collection of data/variables and methods/function.


# * variables use [snake_case]

# * classes use [PascalCase]


class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

    def set_hair(self, person_hair):
        self.hair = person_hair

    def get_hair(self):
        print(self.hair)
