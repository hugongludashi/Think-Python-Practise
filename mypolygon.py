from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob


    
def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

        
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
      

def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, n, length, angle)
        
import math

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
   arc_length = 2 * math.pi * r * angle/360
   n = int(arc_length / 3) + 1
   step_length = arc_length / n
   step_angle = float(angle / n)

   polyline(t, n, step_length, step_angle)

bob.delay = 0.01

arc(bob, 50, 180)

    



        
wait_for_user()
