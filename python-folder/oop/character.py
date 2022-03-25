class Character():
    def __init__(self, real_name, superhero_name):
        self.real_name = real_name
        self.superhero_name = superhero_name

    def set_power(self, superhero_power):
        self.power = superhero_power

    def get_power(self):
        print(
            f"The secret indentity of {self.real_name} is {self.superhero_name} and the supper power is {self.power}")
