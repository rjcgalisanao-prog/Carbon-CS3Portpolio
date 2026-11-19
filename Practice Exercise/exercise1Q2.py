class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = 0
        self.set_age(age)

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

s1 = Student("Mary Grace", -1)

print(s1.get_name())
print(s1.get_age())