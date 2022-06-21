class Person:
    def __init__(self, first_name, last_name, age, male):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.male = male

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


p1 = Person('ahmed', 'shaaikh', '24', True)
print(p1.get_full_name)