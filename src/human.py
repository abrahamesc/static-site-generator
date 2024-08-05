class Human():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f'This is {self.name}, age is {self.age} and gender is {self.gender}'

    def multiply_age_10(self):
        raise NotImplementedError

class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age, None)

    def multiply_age_10(self):
        return self.age * 10





