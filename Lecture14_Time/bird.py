import random

from pico2d import *

import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIMER_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    image = None

    def __init__(self, velocity=1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = random.randint(200, 1400), random.randint(520, 540), velocity
        self.frame = 0
        self.action = 0
        self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) % 5 * 180, int(self.frame) // 5 * 188, 150, 150, self.x, self.y, 50,
                                 50)
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) % 5 * 180, int(self.frame) // 5 * 188, 150, 150, 0, 'h',
                                           self.x, self.y,
                                           50, 50)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if self.dir == 1:
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
            if self.x >= 1400:
                self.dir = -1
        if self.dir == -1:
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
            if self.x <= 200:
                self.dir = 1
