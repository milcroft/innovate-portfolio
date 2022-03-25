from person import Person

liam = Person("Liam", "30", "6'7")
liam.set_hair("brown and curly")

print(liam.height)

jordan = Person("jordan", "30", "5'7")
jordan.set_hair("blonde and straight")

print(
    f"The innovate instructor is called {jordan.name} and he is {jordan.age} years old and his height is {jordan.height}")

print(f"Liam's hair is {liam.hair} but Jordans is {jordan.hair}")

liam.get_hair()
jordan.get_hair()
