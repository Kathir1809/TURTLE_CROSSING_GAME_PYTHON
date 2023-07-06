import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
p = Player()

cars = CarManager()
sc = Scoreboard()
screen.listen()
screen.onkey(p.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move()

    for caar in cars.cars:
        if caar.distance(p) < 20:
            game_is_on = False
            sc.game_over()

    if p.ycor() > 280:
        p.starting_pos()
        cars.incre()
        sc.score_update()






screen.exitonclick()

