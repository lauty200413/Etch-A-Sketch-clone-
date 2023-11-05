from turtle import Turtle, Screen


my_screen = Screen()
merki = Turtle()


def move_forwards():
    merki.forward(10)


def move_backwards():
    merki.forward(-10)


def turn_clockwise():
    new_heading = merki.heading() + 10
    merki.setheading(new_heading)


def turn_counter_clockwise():
    new_heading = merki.heading() - 10
    merki.setheading(new_heading)


def clear():
    merki.goto(0, 0)
    merki.setheading(0)
    merki.clear()


my_screen.listen()
my_screen.onkeypress(key="w", fun=move_forwards)
my_screen.onkeypress(key="s", fun=move_backwards)
my_screen.onkeypress(key="a", fun=turn_counter_clockwise)
my_screen.onkeypress(key="d", fun=turn_clockwise)
my_screen.onkeypress(key="space", fun=clear)


my_screen.exitonclick()
