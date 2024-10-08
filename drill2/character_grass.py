from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    x = 0
    while (x< 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x+2
        delay(0.01)

    y = 90
    while(y<560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y+2
        delay(0.01)

    while (x>60):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 560)
        x = x-2
        delay(0.01)

    while (y>100):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(0,y)
        y = y-2
        delay(0.01)

    while(y>600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        x = x+math.cos(x/360*2*math.pi)
        y = y+math.sin(y/360*2*math.pi)
        delay(0.01)
        
    
close_canvas()
