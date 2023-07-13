import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SLEEP_TIME = 0.1
SLEEP_DECREASE = 0.9

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(key='Up', fun=player.move)

game_is_on = True


while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()

    if player.is_crossed():
        SLEEP_TIME *= SLEEP_DECREASE
