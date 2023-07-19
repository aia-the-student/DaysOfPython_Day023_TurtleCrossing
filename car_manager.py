from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.move_delta = STARTING_MOVE_DISTANCE

    def create_cars(self, n_cars, x_range, y_range):
        for _ in range(n_cars):
            new_car = Turtle()
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            x = random.randrange(x_range[0], x_range[1])
            y = random.randrange(y_range[0], y_range[1])
            new_car.setpos(x=x, y=y)
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            self.car_list.append(new_car)

    def move_cars(self, x_semi_width):
        for car in self.car_list:
            car.forward(self.move_delta)
            x = car.xcor()
            y = car.ycor()
            if abs(x) > x_semi_width:
                car.setpos(x=x_semi_width, y=y)

    def speed_increase(self):
        self.move_delta += MOVE_INCREMENT

    def hit_object(self, object_pos):
        is_hit = False
        n_cars = len(self.car_list)
        i = 0
        while (not is_hit) & (i < n_cars):
            if self.car_list[i].distance(object_pos) < 20:
                is_hit = True
            i += 1
        return is_hit
