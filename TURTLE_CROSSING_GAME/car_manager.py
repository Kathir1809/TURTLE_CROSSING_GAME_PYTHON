COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        self.cars = []
        self.movement = STARTING_MOVE_DISTANCE


    def create_cars(self):
        choice = random.randint(1,6)
        if choice == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(1,2)
            car.penup()
            random_y = random.randint(-250,250)
            car.goto(300,random_y)
            self.cars.append(car)

    def move(self):
        for ca in self.cars:
            ca.backward(self.movement)


    def incre(self):
        self.movement += MOVE_INCREMENT

