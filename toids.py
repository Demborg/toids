#! /usr/bin/env python3
import turtle
from random import randint
from typing import Sequence, Tuple
from time import sleep


def create_random_turtle() -> turtle.Turtle:
    t = turtle.Turtle()
    t.penup()
    t.setposition(randint(-100, 100), randint(-100, 100))
    t.setheading(randint(0, 360))
    return t


def visible_from(boid: turtle.Turtle, other: turtle.Turtle) -> bool:
    return abs(boid.towards(other) - boid.heading()) < 90

def mean(flock: Sequence[turtle.Turtle]) -> Tuple[float, float]:
    x = sum(b.xcor() for b in flock) / len(flock)
    y = sum(b.ycor() for b in flock) / len(flock)
    return x, y

def step(flock: Sequence[turtle.Turtle]) -> None:
    for boid in flock:
        visible = [b for b in flock if visible_from(boid, b) and b != boid]
        if len(visible):
            mean_visible = mean(visible)
            boid.left(boid.towards(mean_visible) - boid.heading())
        boid.forward(10)


def main():
    # Setup
    turtle.delay(0)

    n = 30
    flock = [create_random_turtle() for _ in range(n)]

    while True:
        step(flock)
        sleep(0.01)

    turtle.done()

if __name__ == "__main__":
    main()
