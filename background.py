from kivy.core.window import Window
from kivy.uix.image import Image


class Background:
    def __init__(self, main_widget):

        self.window_sizes = Window.size
        self.main_screen = main_widget

        self.background = Image(source = "assets/Background/background.png",
                                size = (self.window_sizes[0], self.window_sizes[1]),
                                pos = (0, 0))


        self.main_screen.add_widget(self.background)