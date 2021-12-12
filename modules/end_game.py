from shutil import get_terminal_size
from utils import print_text
from modules.base import BaseModule


class EndGame(BaseModule):
    def activate(self, hooks=None):
        super().activate(hooks=[
            ['pre_draw', 'DrawEndMenu', self.end_menu_draw],
        ])
        row = get_terminal_size().lines - 3
        col = get_terminal_size().columns - 2
        lowest_size = row < col and row or col
        self.core.change_screen_size(lowest_size)

    def end_menu_draw(self, screen, size):
        print_text(screen, size / 2, 1, 'Конец игры!', center=True)
        print_text(screen, size / 2, 2, f'Игрок {self.core.state["winner"]} победил!', center=True)
