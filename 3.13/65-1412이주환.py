class Dog:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind
    def bark(self):
        print(f"{self.name} 멍멍")
    def sit(self):
        print(f"{self.name} 앉아")
    
my_dog = Dog("뽀삐", 3, "푸들")
my_dog.bark()
my_dog.sit()

my_dog2 = Dog("바둑이", 5, "진돗개")
my_dog2.bark()
my_dog2.sit()