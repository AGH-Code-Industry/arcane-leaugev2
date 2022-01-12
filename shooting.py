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

        self.process = []
        self.bullets = []
        self.player_bullets = []
        self.player_reload = True
        self.i = 0

        self.player = player

        self.process.append(Clock.schedule_interval(self.check_bullets, 1/60))
        Clock.schedule_interval(self.reload, 1/60)


    def minion_shoot(self, position, minion_size):
        eval(f"self.minion_bullet(position, minion_size)")

    def player_shoot(self, position, champion_size):
        eval(f"self.player_bullet(position, champion_size)")

    def check_bullets(self,time_passed):
        for i,bullet in enumerate(self.bullets):
            if (self.player and bullet.pos[0] > 0) or (not self.player and bullet.pos[0] > self.window_sizes[0]):
                self.destroy(i)

    def destroy(self, n):
        if len(self.bullets) > n:
            bullet = self.bullets.pop(n)
            if bullet in self.main_screen.children:
                self.main_screen.remove_widget(bullet)

    def player_destroy(self, n):
        if len(self.player_bullets) > n:
            bullet = self.player_bullets.pop(n)
            if bullet in self.main_screen.children:
                self.main_screen.remove_widget(bullet)

    def reload(self, dt):
        if self.player_reload == False:
            self.i += 1
        if self.i % 60 == 0:
            self.player_reload = True


    def minion_bullet(self, position, minion_size):
        pos = (position[0] + minion_size, position[1] + minion_size / 2)
        duration = ((self.window_sizes[0] - pos[0]) / self.window_sizes[0]) * 5
        self.bullets.append(Image(source="assets/Minions/pocisk_minion.png",
                                  pos=pos,
                                  size=(self.bullet_size, self.bullet_size)))
        minion_shoot = Animation(x = self.window_sizes[0] * 1.05, t="out_sine", duration = duration)

        self.main_screen.add_widget(self.bullets[-1])
        minion_shoot.start(self.bullets[-1])

    def player_bullet(self, position, champion_size):
        pos = (position[0], position[1] + champion_size /8)
        self.player_bullets .append(Image(source="assets/Champion/pocisk_yasuo.png",
                                         pos=pos,
                                         size=(self.bullet_size, self.bullet_size)))
        champion_shoot = Animation(x = -self.bullet_size, t="out_sine", duration = 3)

        self.main_screen.add_widget(self.player_bullets[-1])
        champion_shoot.start(self.player_bullets[-1])

    def stop(self):
        for process in self.process:
            process.cancel()