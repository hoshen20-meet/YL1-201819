from turtle import*

class Ball(Turtle):
         def __init__(self,x,y,dx,dy,r,color):
                  Turtle.__init__(self)
                  self.penup()
                  self.shape("circle")
                  self.x = x
                  self.y = y
                  self.goto(x,y)
                  self.dx = dx
                  self.dy = dy
                  self.r = r
                  self.color(color)
                  self.shapesize(self.r/10)
         def Move(self,width,height):
                  current_x = self.position()[0]
                  new_x = (current_x + self.dx)
                  current_y = self.position()[1]
                  new_y = current_y + self.dy
                  right_side_ball = new_x + self.r
                  left_side_ball = new_x - self.r
                  top_side_ball = new_y + self.r
                  bottom_side_ball = new_y - self.r
                  self.goto(new_x,new_y)
                  if right_side_ball >= width or left_side_ball <= -width:
                           self.dx = -self.dx
                  elif top_side_ball >= height or bottom_side_ball <= -height:
                           self.dy = -self.dy
         def new_ball(self,x,y,dx,dy,r,color):
                  
                  self.x = x
                  self.y = y
                  
                  self.dx = dx
                  self.dy = dy
                  self.r = r
                  self.color(color)
                  self.shapesize(self.r/10)
                  self.penup()
                  self.shape("circle")
                  self.goto(x,y)

                         
                           
                  
         
                  
                  
