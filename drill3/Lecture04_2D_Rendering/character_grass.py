from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.1)

def run_circle():
    print('circle')

    r, cx, cy = 300, 800//2, 600/2
    for deg in range(0, 360, 3):
        theta = math.radians(deg)
        x =  r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.1)

def run_top():
    print('top')
    for x in range(0,800, 10):
        draw_boy(x, 550)

def run_right():
    print('right')
    for y in range(550, 0, -10):
        draw_boy(790, y)

def run_bottom():
    print('bottom')
    for x in range(790, 0, -10):
        draw_boy(x, 30)

def run_left():
    print('left')
    for y in range(0, 550, 10):
        draw_boy(10, y)
    
def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_bottom_triangle():
    print('triangle bottom')
    for x in range(0, 790, 30):
          draw_boy(x,30)

    pass

def run_right_triangle():
    print('triangle right')
    x = 790
    y = 30
    while y<550:
        x = x-8
        y = y+10
        draw_boy(x,y)

def run_left_triangle():
    print('triangle left')
    x = 420
    y = 550
    while y>30:
        x = x-8
        y = y-10
        draw_boy(x,y)
    
          
def run_triangle():
    print('triangle')
    run_bottom_triangle()
    run_right_triangle()
    run_left_triangle()
    
while True:
    run_circle()
    run_rectangle()
    run_triangle()
    
# fill here

close_canvas()
