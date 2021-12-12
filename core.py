import settings
import time
from shutil import get_terminal_size
from hooks import Hooks

import keyboard


class Core:
    __fps = 5
    screen_size = None
    screen = None

    hooks = Hooks()
    modules = []
    state = {
        'game_size': None,
        'game_mode': None,
    }

    def __init__(self):
        keyboard.on_press(lambda btn: self.hooks.call('button_pressed', btn), suppress=False)
        self.__load_modules()
        self.modules[0].activate()
        self.__start_main_cycle()

    def __change_status(self, status):
        self.state['status'] = status

    def __load_modules(self):
        for moduleClass in settings.MODULES:
            self.modules.append(moduleClass(self))

    def change_screen_size(self, screen_size):
        self.screen_size = screen_size
        self.clear_screen()

    def clear_screen(self):
        self.screen = [[' ' for y in range(self.screen_size)] for x in range(self.screen_size)]

    @property
    def __screen_size_full(self):
        return self.screen_size + 2

    def __clear(self):
        self.clear_screen()
        print("\n" * get_terminal_size().lines, end='')

    def __draw(self):
        print('#' * self.__screen_size_full)
        for y in range(self.screen_size):
            print('#' + ''.join(self.screen[y]) + '#')
        print('#' * self.__screen_size_full)

    def __start_main_cycle(self):
        self.hooks.call('pre_main_cycle', self)
        while True:
            self.__clear()
            self.hooks.call('pre_draw', self.screen, self.screen_size)
            self.__draw()
            self.hooks.call('after_draw')
            time.sleep(1 / self.__fps)
