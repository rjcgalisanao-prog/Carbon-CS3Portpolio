class dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}")

dog1 = dog("Herb", 3, "Husky")
dog2 = dog("Max", 5, "Golden Retriever")

dog1.bark()
dog1.display_info()
dog2.bark()
dog2.display_info()