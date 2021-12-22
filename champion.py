from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Ellipse
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from minions import Minion, Minions
from shooting import Shoot

frames_per_second = 60.0
champion_size = Window.size[1] * .2

class Champion(Widget):
    def __init__(self, main_widget, app, **kwargs):
        super().__init__(**kwargs)

        self.window_sizes = Window.size
        self.main_screen = main_widget
        self.app = app
        self.clocks = []

        self.current_level = 1

        self.champion = Image(source = "assets/Champion/new2.png",
                                size = (champion_size, champion_size),
                                pos = (self.window_sizes[0] * .9 , (self.current_level + .05) / 3 * self.window_sizes[1]))

        self.main_screen.add_widget(self.champion)

        Clock.schedule_interval(self.collide_bullet, 1/60)

    def move(self):
        self.champion.pos = (self.window_sizes[0] * .9,
                             (self.current_level + .05) / 3 * self.window_sizes[1] )

    def collide_bullet(self, dt):
        for minion in Minions.minions:
            for i, bullet in enumerate(minion.missile.bullets):
                if bullet.collide_widget(self.champion):
                    minion.missile.destroy(i)
                    break
