import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_play(self):
        print("Play Time")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Night")
        self.gladness += 3

    def to_eat(self):
        print("Its time to food")
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print("SUN STRIKE!!....")
            print("u die")
            self.alive = False
        elif self.gladness <=0:
             print("Depression...lox")
             self.alive = False
        elif self.progress > 5:
            print("Excellent")
            self.elive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")

    def life(self, day):
        day = f"Day {day} of {self.name} life"
        print(f"{day:=^30}")
        life_cube = random.randint(1, 3)
        if life_cube == 1:
            self.to_play()
        if life_cube == 2:
            self.to_sleep()
        if life_cube == 3:
            self.to_eat()
        self.end_of_day()
        self.is_alive()


Boris = Student(name="Boris")

for day in range(365):
    if grigoriy.alive == False:
        break
    grigoriy.life(day)