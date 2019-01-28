import turtle
import time
import random
import math
from ball import Ball

global running
running = True
turtle.colormode(1)

turtle.tracer(0)
turtle.hideturtle()
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2


number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100

minimum_ball_dx = -5
maximum_ball_dx = 5

minimum_ball_dy = -5
maximum_ball_dy = 5

BALLS = []
for i in range(number_of_balls):
         x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
         y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
         dx = random.randint(minimum_ball_dx , maximum_ball_dx)
         while (dx == 0):
                  dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                   
         dy = random.randint(minimum_ball_dy , maximum_ball_dy)
         while (dy == 0):
                  dy = random.randint(minimum_ball_dy , maximum_ball_dy)
         r = random.randint(minimum_ball_radius , maximum_ball_radius)
         color = (random.random(), random.random(), random.random())
         ball = Ball(x,y,dx,dy,r,color)
         BALLS.append(ball)


         
def random_values():
         x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
         y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
         dx = random.randint(minimum_ball_dx , maximum_ball_dx)
         while (dx == 0):
                  dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                   
         dy = random.randint(minimum_ball_dy , maximum_ball_dy)
         while (dy == 0):
                  dy = random.randint(minimum_ball_dy , maximum_ball_dy)
         radius = random.randint(minimum_ball_radius , maximum_ball_radius)
         
         color = (random.random(), random.random(), random.random())

         return([x, y, dx, dy, radius, color])
ran = random_values()
my_ball = Ball(ran[0], ran[1],ran[2],ran[3],ran[4],ran[5])



def move_all_balls():
         for i in BALLS:
                  i.Move(screen_width,screen_height)
                  
def Collide(ball_a,ball_b):
         if ball_a == ball_b:
                  return False
        
         d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+(math.pow(ball_a.ycor()-ball_b.ycor(),2)))
         if d <= ball_a.r + ball_b.r:
                  return True
         else:
                  return False

def check_all_balls_collision():
         all_balls = []
         all_balls.append(my_ball)
         global running
         for ball in BALLS:
                  all_balls.append(ball)

         for ball_a in all_balls:
                  for ball_b in all_balls:
                           if Collide(ball_a,ball_b):
                                    r1 = ball_a.r
                                    r2 = ball_b.r
        
                                    x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
                                    y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
                                    dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                                    while (dx == 0):
                                             dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                                              
                                    dy = random.randint(minimum_ball_dy , maximum_ball_dy)
                                    while (dy == 0):
                                             dy = random.randint(minimum_ball_dy , maximum_ball_dy)
                                    radius = random.randint(minimum_ball_radius , maximum_ball_radius)
                                    color = (random.random(), random.random(), random.random())

                                    if r1 < r2:
                                             ball_a.new_ball(x,y,dx,dy,radius,color)
                                             ball_b.r += 1
                                             ball_b.shapesize(ball_b.r/10)
                                             if my_ball == ball_a:
                                                      running = False
                                                      turtle.write('you failed',move=False,align='center',font=('Ariel',60,'normal'))
                                                      break
                                             if r2 < r1:
                                                      ball_b.new_ball(x,y,dx,dy,radius,color)
                                                      ball_a.r += 1
                                                      ball_a.shapesize(ball_a.r/10)
                                    
                                   
                                    



def movearound():
         x_coordinate =  turtle.getcanvas().winfo_pointerx() - screen_width * 2
         y_coordinate = screen_height * 1.4 - turtle.getcanvas().winfo_pointery()
         my_ball.goto(x_coordinate,y_coordinate)
         my_ball.x = x_coordinate
         my_ball.y = y_coordinate

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2


def play():
         global running
         running = True

         while running == True:
                  screen_width = turtle.getcanvas().winfo_width()/2
                  screen_height = turtle.getcanvas().winfo_height()/2
                  movearound()
                  move_all_balls()
                  check_all_balls_collision()
                  turtle.update()
                  time.sleep(.1)
                  if my_ball.r >= 150:
                           turtle.color('blue')
                           turtle.write('you won!',move=False, align='center',font=('Ariel',60,'normal'))
                           running == False
                           break
                  if Collide(my_ball,ball) and my_ball.r < ball.r:
                           turtle.color('red')
                           turtle.write('you failed!',move=False, align='center',font=('Ariel',60,'normal'))
                           running == False
                           break
                  if ball.r >= 150:
                           turtle.color('red')
                           turtle.write('you failed!',move=False,align='center',font=('Ariel',60,'normal'))
                           running == False
                           break
         answer = input('would you like to restart?')
         if answer == 'yes':
                  running = True
                  for i in BALLS:

                           x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
                           y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
                           dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                           while (dx == 0):
                                    dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                                              
                           dy = random.randint(minimum_ball_dy , maximum_ball_dy)
                           while (dy == 0):
                                    dy = random.randint(minimum_ball_dy , maximum_ball_dy)
                           r = random.randint(minimum_ball_radius , maximum_ball_radius)
                           color = (random.random(), random.random(), random.random())
                           i.new_ball(x,y,dx,dy,r,color)
                  my_ball.new_ball(x,y,dx,dy,r,color)
                  turtle.clear()
                  
                  play()
                  
         else:
                  quit()


play()





         
turtle.mainloop()
 
         
         
         

                           
                                    

         
                  


                  
                  
                  
