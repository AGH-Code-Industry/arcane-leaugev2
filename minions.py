import random

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from shooting import Shoot

frames_per_second = 60.0
minion_size = Window.size[1] * .12

class Minions:

    minions = []

    def __init__(self, main_widget):
        self.main_screen = main_widget


        self.init_minions_list()
        self.window_sizes = Window.size

        # Clock.schedule_once(self.init_single_minion, random.random() * 60)
        Clock.schedule_interval(self.delete_minions, 1/60)

    # def check_minions(self,time_passed):
    #     for i, minion in enumerate(self.minions):
    #         if minion.init_minion() > self.window_sizes[0]:
    #             self.delete_minions(i)

    def init_single_minion(self, dt):
        self.minions.insert(0, Minion(self.main_screen))
        print(len(self.minions))

    def init_minions_list(self):
        for i in range(0, 20):
            Clock.schedule_once(self.init_single_minion, random.random() * 60)

    def delete_minions(self, dt):
        for i, minion in enumerate(self.minions):
            x, y = minion.get_cords()
            if x > self.window_sizes[0]:
                self.minions.pop(i)


class Minion:
    def __init__(self, main_widget):

        self.window_sizes = Window.size
        self.main_screen = main_widget
        self.clocks = []

        self.current_minion_state = "Init"
        self.current_minion_level = None
        self.missile = Shoot(main_widget, False)
        self.init_minion()

        Clock.schedule_once(self.shot, random.random())
        Clock.schedule_interval(self.shot, self.missile.rate)
        Clock.schedule_interval(self.delete_minion, 1/60)

    def init_minion(self):
        self.current_minion_level = random.randint(0, 2)
        startX = - minion_size
        staticY = ((self.current_minion_level + .05) / 3 * self.window_sizes[1])
        borderX = self.window_sizes[0]

        self.this = Image(source = "assets/Minions/minion.png",
                            size = (minion_size, minion_size),
                            pos = (startX, staticY))
        self.main_screen.add_widget(self.this)

        self.animate = Animation(x = borderX + 1, y = staticY,t = "out_quart", duration = 20)
        self.animate.start(self.this)

    def shot(self, time_passed):
        self.missile.shoot(self.this.pos, minion_size)

    def get_cords(self):
        return self.this.pos

    def delete_minion(self, dt):
        x, y = self.get_cords()
        if x > self.window_sizes[0]:
            self.main_screen.remove_widget(self.this)



