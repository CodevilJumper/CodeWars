from turtle import *

clear()
reset()

gloves1 = 10
gloves2 = 8
gloves3 = 3
gloves4 = 5

total = gloves1 + gloves2 + gloves3 + gloves4

gloves = [10, 8, 3, 5]

# draw x axis

goto(80, 0)

# draw y axis
goto(0, 0)
goto(0, 100)

# go back to zero

goto(0, 0)

for index in range(len(gloves)):
    goto(20 + (20*index), gloves[index]*10)
    




