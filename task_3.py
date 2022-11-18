from turtle import *
from random import randint

speed("fast")

STEP = 50
MOUNT = [0, 20, 40, 80, 130, 250, 130, 70, 40, 20, 0, 30, 70, 130, 260, 130, 60, 30, 0]

for i in range(len(MOUNT)):
    goto(i * STEP, MOUNT[i] + randint(-30, 30))

exitonclick()
