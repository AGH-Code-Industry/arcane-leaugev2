from kivy import Config, platform
from kivy.uix.widget import Widget

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.stencilview import StencilView

from champion import Champion
from minions import Minion, Minions


class CanvasContext(StencilView):
    pass


class MainWidget(Widget):
    pass

class ArcadeLeaugeApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down = self.on_keyboard_down)
            self._keyboard.bind(on_key_up = self.on_keyboard_up)

    def build(self):
        self.main_widget = MainWidget()
        self.minons = Minions(self.main_widget)
        self.champion = Champion(self.main_widget, self)


        Clock.schedule_interval(lambda dt: print(f"[\033[92mINFO\033[0m   ] [FPS         ] {str(Clock.get_fps())}"), 1)

        return self.main_widget

    def is_desktop(self):
        if platform in ["linux", "win", "macosx"]:
            return True
        else:
            return False

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "spacebar":
            self.champion.shot()
            print("space")
        elif keycode[1] == "up":
            if self.champion.current_level < 2:
                self.champion.current_level += 1
                self.champion.move()
        elif keycode[1] == "down":
            if self.champion.current_level > 0:
                self.champion.current_level -= 1
                self.champion.move()
        return True

    def on_keyboard_up(self, keyboard, keycode):
        return True


if __name__ == '__main__':
    ArcadeLeaugeApp().run()