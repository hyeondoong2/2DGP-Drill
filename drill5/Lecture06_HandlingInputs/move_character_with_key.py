from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
SPRITE_WIDTH, SPRITE_HEIGHT = 1200, 1040

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite_image.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame_x = 0
frame_y = 0
dir_x = 0
dir_y = 0

def handle_events():
    global running
    global dir_x, dir_y
    global up, down, left, right
    global frame_y

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
         # KeyDown   
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
               #print('right')
               frame_y = 0
               dir_x = 1
               dir_y = 0
            elif event.key == SDLK_LEFT:
                frame_y = 2
                dir_x = -1
                dir_y = 0
            elif event.key == SDLK_UP:
                frame_y = 1
                dir_y = 1
                dir_x = 0
            elif event.key == SDLK_DOWN:
                frame_y = 3
                dir_y = -1
                dir_x = 0
            elif event.key == SDLK_ESCAPE:
                dir_running = False
        # KeyUp
        #elif event.type == SDL_KEYUP:

# fill here

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2 , TUK_HEIGHT // 2 )
    
    character.clip_draw(frame_x * SPRITE_WIDTH // 10, frame_y * SPRITE_HEIGHT // 8, SPRITE_WIDTH // 10, SPRITE_HEIGHT // 8, x, y)
    update_canvas()

    if y < 0 + 20:
        dir_y = 0
    elif y > TUK_HEIGHT - 20:
        dir_y = 0
    elif x < 0 + 20:
        dir_x = 0
    elif x > TUK_WIDTH - 20:
        dir_x = 0
    
    handle_events()
    
    frame_x = (frame_x + 1) % 10
    #frame_y = (frame_y + 1) % 10
    x += dir_x * 10
    y += dir_y * 8
    
    delay (0.05)

close_canvas()
