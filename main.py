import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SLEEP_TIME = 0.1
N_CARS = 15
CARS_X_RANGE = (-300, 300)
CARS_Y_RANGE = (-250, 250)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.create_cars(n_cars=N_CARS, x_range=CARS_X_RANGE, y_range=CARS_Y_RANGE)

screen.listen()
screen.onkey(key='Up', fun=player.move)

game_is_on = True


while game_is_on:
    time.sleep(SLEEP_TIME)
    car_manager.move_cars(x_semi_width=300)

    if player.is_crossed():
        scoreboard.add_score()
        car_manager.speed_increase()

    if car_manager.hit_object(player.pos()):
        game_is_on = False
        scoreboard.game_over()

    screen.update()

screen.exitonclick()
