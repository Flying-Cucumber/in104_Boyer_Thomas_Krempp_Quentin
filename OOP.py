from time import time, sleep

class Animals:

    def __init__(self, name):
        self.alive = True
        self.hungry = False
        self.name = name
        self.last_meal_time = time()

    def is_hungry(self):
        t = time()
        if t - self.last_meal_time > 6:
            self.hungry = True
        return self.hungry
    
    def is_alive(self):
        t = time()
        if t - self.last_meal_time > 12:
            self.alive = False
        return self.alive

    def feed(self):
        if self.is_alive():
            print("Yummy! " + str(self.name) + " is fed and happy! \n")
            if self.is_hungry():
                print("He was really hungry \n")
                self.hungry = False
            else:
                print("Even if he wasn't hungry \n")
            self.last_meal_time = time()
        else:
            print(str(self.name) + " is already dead! \n")

class Cat(Animals):

    def __init__(self, name):
        Animals.__init__(self, name)
        self.number_of_lives = 9

    def is_alive(self):
        Animals.is_alive(self)
        if (not self.alive) and (self.number_of_lives > 0):
            self.alive = True
            self.number_of_lives -= 1
            self.last_meal_time = time()
        return self.alive

    def pat_on_the_back(self):
        print("purr! =^.^= \n")

class Dog(Animals):

    def __init__(self, name):
        Animals.__init__(self, name)
        self.date_of_birth = time()

    def age(self):
        age = int(7 * (time() - self.date_of_birth))
        print(str(self.name) + " is " + str(age // 60) + " minutes and " + str(age % 60) + " secondes old (in human age)\n")

    def presentation(self):
        print("My name is " + str(self.name) + " and I'm a good doggo! \n")

def run():
    cat_1 = Cat("Garfield")
    dog_1 = Dog("Dagobert")
    cat_1.feed()
    dog_1.feed()
    cat_1.pat_on_the_back()
    dog_1.presentation()
    sleep(10)
    cat_1.feed()
    sleep(3)
    dog_1.feed()