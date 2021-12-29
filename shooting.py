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

        self.minion_bullets = []

        self.player = player
        self.player_bullets = []

        Clock.schedule_interval(self.check_bullets, 1/60)


    def minion_shoot(self, position, minion_size):
        eval(f"self.minion_bullet(position, minion_size)")

    def player_shoot(self, position, champion_size):
        eval(f"self.player_bullet(position, champion_size)")

    def check_bullets(self,time_passed):
        for i,bullet in enumerate(self.minion_bullets):
            if (self.player and bullet.pos[0] > 0) or (not self.player and bullet.pos[0] > self.window_sizes[0]):
                self.destroy(i)

    def destroy(self, n):
        if len(self.minion_bullets) > n:
            bullet = self.minion_bullets.pop(n)
            if bullet in self.main_screen.children:
                self.main_screen.remove_widget(bullet)


    def minion_bullet(self, position, minion_size):
        pos = (position[0] + minion_size, position[1] + minion_size / 2)
        duration = ((self.window_sizes[0] - pos[0]) / self.window_sizes[0]) * 5
        self.minion_bullets.append(Image(source="assets/Minions/bullet.png",
                                  pos=pos,
                                  size=(self.bullet_size, self.bullet_size)))
        minion_shoot = Animation(x = self.window_sizes[0], t="out_sine", duration = duration)

        self.main_screen.add_widget(self.minion_bullets[-1])
        minion_shoot.start(self.minion_bullets[-1])

    def player_bullet(self, position, champion_size):
        pos = (position[0], position[1] + champion_size / 2)
        self.player_bullets.append(Image(source="assets/Minions/bullet.png",
                                         pos=pos,
                                         size=(self.bullet_size, self.bullet_size)))
        champion_shoot = Animation(x = -self.bullet_size, t="out_sine", duration = 3)

        self.main_screen.add_widget(self.player_bullets[-1])
        champion_shoot.start(self.player_bullets[-1])
