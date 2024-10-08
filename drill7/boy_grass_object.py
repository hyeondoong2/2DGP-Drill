from logging import setLogRecordFactory

from pico2d import *

import random
# Game object class here

class Grass:
    # 생성자를 이용해서 객체의 초기 상태를 정의
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass

    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    pass

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(20, 800), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 60:
            self.y -= random.randint(3, 10)

    def draw(self):
        self.image.draw(self.x, self.y)

    pass

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(20, 800), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 60:
            self.y -= random.randint(3, 10)

    def draw(self):
        self.image.draw(self.x, self.y)

    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    for o in world:
        o.update()

    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()
    pass

def reset_world():  # 초기화 하는 함수
    global running
    global grass
    global team
    global world
    global smallball
    global bigball

    running = True
    world = []

    grass = Grass() # Grass 클래스를 이용해서 grass 객체 생성
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team # 리스트끼리 더함

    smallball = [SmallBall() for i in range(10)]
    world += smallball

    bigball = [BigBall() for i in range(10)]
    world += bigball


open_canvas()
reset_world()
running = True
# initialization code

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.06)
# finalization code

close_canvas()
