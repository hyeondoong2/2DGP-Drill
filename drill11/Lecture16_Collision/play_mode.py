import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    global balls
    balls = [Ball(random.randint(100,1500), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    zombies = Zombie()
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    # 충돌 정보 등록
    game_world.add_collision_pair('boy:ball', boy, None)  # 소년과 공 충돌 그룹 설정
    game_world.add_collision_pair('boy:zombie', boy, None)  # 소년과 좀비 충돌 그룹 설정

    for zombie in zombies:
        game_world.add_collision_pair('zombie:ball', zombie, None)
        game_world.add_collision_pair('boy:zombie', None, zombie)

    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)  # 공 추가

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

    # fill here


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

