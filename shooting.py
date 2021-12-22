from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image


class Shoot:
    def __init__(self, main_widget, player = True):
        self.window_sizes = Window.size

        self.speed = 5
        self.rate = 3
        self.bullet_size = self.window_sizes[0] * .04

        self.main_screen = main_widget

        self.bullets = []

        self.player = player

        Clock.schedule_interval(self.check_bullets, 1/60)


    def shoot(self, position, ship_size):
        eval(f"self.bullet(position, ship_size)")

    def check_bullets(self,time_passed):
        for i,bullet in enumerate(self.bullets):
            if (self.player and bullet.pos[0] > 0) or (not self.player and bullet.pos[0] > self.window_sizes[0]):
                self.destroy(i)

    def destroy(self, n):
        if len(self.bullets) > n:
            bullet = self.bullets.pop(n)
            if bullet in self.main_screen.children:
                self.main_screen.remove_widget(bullet)


    def bullet(self, position, ship_size):


        pos = (position[0] + ship_size, position[1] + ship_size / 2)
        duration = ((self.window_sizes[0] - pos[0]) / self.window_sizes[0]) * 5
        self.bullets.append(Image(source="assets/Minions/bullet.png",
                                  pos=pos,
                                  size=(self.bullet_size, self.bullet_size)))
        shoot = Animation(x = self.window_sizes[0], t="out_sine", duration = duration)

        self.main_screen.add_widget(self.bullets[-1])
        shoot.start(self.bullets[-1])
