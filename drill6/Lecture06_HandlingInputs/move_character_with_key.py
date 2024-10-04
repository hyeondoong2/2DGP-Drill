from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('walking_sheet.png')

def handle_events():
    global running, dir_x, dir_y

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

            # fill here


running = True
x = 1842 // 2
y = 2400//2
frame_x = 0
frame_y = 0
dir_x = 0
dir_y = 0

# fill here
while running:
    clear_canvas()
    background.draw()
    character.clip_draw(frame_x * 460, frame_y * 550, 100, x, y)
    update_canvas()
    handle_events()
    frame_x = (frame_x + 1) % 4
    frame_y = (frame_y + 1) % 4
    x += dir_x * 5
    y += dir_y * 5
    delay (0.05)

close_canvas()
