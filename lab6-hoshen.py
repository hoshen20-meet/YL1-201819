from turtle import*
import random
import math
class ball(Turtle):
    def __init_(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape('circle')
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)




ball1 = ball(20,'black',30)
ball2 = ball(25,'blue',40)


def check_collision(ball1,ball2):
    x1=ball1.pos()[0]
    x2=ball2.pos()[0]
    y1=ball1.pos()[1]
    y2=ball2.pos()[1]
    if ball1.radius + ball2.radius >= math.sqrt(math.pow((x2-x1),2)+ math.pow((y2-y1),2)):
        print('collision!')

mainloop()
