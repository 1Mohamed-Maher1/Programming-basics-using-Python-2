from turtle import *
import random

colors = ['red', 'black', 'blue', 'green']
color(colors[random.randint(0, 3)], colors[random.randint(0, 3)])
begin_fill()
# counter = 0
while True: #counter < 10
    forward(200)
    left(170)
    #counter += 1
    if abs(pos()) < 1:
        break
end_fill()
done()
