from shutil import get_terminal_size
from utils import print_text
from modules.base import BaseModule
import settings


class MainMenu(BaseModule):
    stage = 1

    def activate(self, hooks=None):
        super().activate(hooks=[
            ['pre_draw', 'DrawEndMenu', self.main_menu_draw],
            ['button_pressed', 'MainMenuButton', self.handle_button]
        ])
        row = get_terminal_size().lines - 3
        col = get_terminal_size().columns - 2
        lowest_size = row < col and row or col
        self.core.change_screen_size(lowest_size)

    def deactivate(self):
        super().deactivate()
        self.core.modules[1].activate()

    def handle_button(self, btn):
        try:
            index = int(btn.name) - 1
        except ValueError:
            return

        if index in range(0, 3):
            if self.stage == 1:
                self.core.state['game_size'] = settings.AVAILABLE_GAME_SIZES[index]
                self.stage += 1
            elif self.stage == 2:
                self.core.state['game_mode'] = settings.AVAILABLE_GAME_MODES[index]
                self.deactivate()

    @staticmethod
    def draw_select_size(screen, size):
        print_text(screen, size / 2, size * 0.3, 'Выберите размер:', center=True)
        print_text(screen, size / 2, size * 0.3 + 2, '1:  3 x 3', center=True)
        print_text(screen, size / 2, size * 0.3 + 3, '2:  4 x 4', center=True)
        print_text(screen, size / 2, size * 0.3 + 4, '3:  5 x 5', center=True)

    @staticmethod
    def draw_select_mode(screen, size):
        print_text(screen, size / 2, size * 0.3, 'Выберите режим:', center=True)
        print_text(screen, size / 2, size * 0.3 + 2, '1:  Игрок против игрока', center=True)
        print_text(screen, size / 2, size * 0.3 + 3, '2:  Игрок против бота', center=True)
        print_text(screen, size / 2, size * 0.3 + 4, '3:  Бот против бота', center=True)

    def main_menu_draw(self, screen, size):
        print_text(screen, size / 2, 1, 'Главное меню:', center=True)
        print_text(screen, size / 2, 2, '(управление цифрами)', center=True)
        if self.stage == 1:
            self.draw_select_size(screen, size)
        elif self.stage == 2:
            self.draw_select_mode(screen, size)

