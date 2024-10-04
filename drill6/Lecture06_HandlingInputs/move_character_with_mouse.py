from pico2d import *
import random

# fill here
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

frame_x = frame_y = 0
running = True
back_x, back_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
arrow_x, arrow_y = random.randint(0, TUK_WIDTH), random. randint(0, TUK_HEIGHT)
x, y = back_x, back_y
t = 0

def rand_arrow():
    global arrow_x, arrow_y
    global back_x, back_y
    global t

    arrow_x, arrow_y = random.randint(0, TUK_WIDTH), random. randint(0, TUK_HEIGHT)
    back_x, back_y = x, y
    t = 0
    
    pass

def run_character():
    global x, y
    global t
    
    t += 0.03

    x = (1 - t) * back_x  + t * arrow_x
    y = (1 - t) * back_y  + t * arrow_y

    if t > 1.0:
       # print('random')
        rand_arrow()
    pass
    

def handle_events():
    global running
    
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            
    pass


while running:
    run_character()
    clear_canvas()
    # fill here
    if (arrow_x < x) :
        frame_y  = 0
    elif (arrow_x > x):
        frame_y = 1
        
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
    hand_arrow.draw(arrow_x, arrow_y)
    
    update_canvas()
    handle_events()
    frame_x = (frame_x + 1) % 8
    delay(0.05)

close_canvas()




