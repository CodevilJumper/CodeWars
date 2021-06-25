from turtle import *

clear()
reset()

squares = 4
sides = 4

for square in range(1, squares + 1):
    for side in range(1, sides + 1):
        forward(20 * square)
        left(90)
    penup()
    forward(20 * square)
    left(90)
    forward(20 * square)
    right(90)
    pendown()

done()

print("The program has finished drawing")

