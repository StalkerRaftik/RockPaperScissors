from utils import sum_vect, get_opposite_vect
from modules.base import BaseModule


class RockPaperScissors(BaseModule):
    player = 1
    game_map = None
    current_input_pos = [0, 0]
    input_char = 'X'

    def activate(self, hooks=None):
        super().activate(hooks=[
            ['pre_draw', 'DrawGame', self.draw_game],
            ['button_pressed', 'HandleGameButton', self.handle_button]
        ])
        size = self.core.state['game_size']
        self.core.change_screen_size(size)
        self.game_map = [[' ' for y in range(size)] for x in range(size)]

    def deactivate(self):
        super().deactivate()
        self.core.modules[2].activate()

    def change_player(self):
        if self.player == 1:
            self.player = 2
            self.input_char = 'O'
        else:
            self.player = 1
            self.input_char = 'X'

    def is_out_of_map(self, coords):
        return coords[0] < 0 or coords[1] < 0 or coords[0] >= len(self.game_map) or coords[1] >= len(self.game_map)

    def handle_button(self, btn):
        pos = self.current_input_pos
        new_pos = pos
        if btn.name == 'up':
            new_pos = sum_vect(pos, [-1, 0])
        elif btn.name == 'down':
            new_pos = sum_vect(pos, [1, 0])
        elif btn.name == 'left':
            new_pos = sum_vect(pos, [0, -1])
        elif btn.name == 'right':
            new_pos = sum_vect(pos, [0, 1])
        if pos != new_pos:
            if not self.is_out_of_map(new_pos):
                self.current_input_pos = new_pos
            return

        if btn.name == 'enter':
            if self.game_map[pos[0]][pos[1]] == ' ':
                self.game_map[pos[0]][pos[1]] = self.input_char
                if self.is_player_won(pos):
                    self.core.state['winner'] = self.player
                    self.deactivate()
                self.change_player()

    def is_player_won(self, new_input):
        map = self.game_map
        possible_win_vectors = ([1, 0], [0, 1], [1, 1])
        score_to_win = self.core.state['game_size']
        for win_vect in possible_win_vectors:
            # a bit silly logic, because we're counting new input value twice
            score = -1
            for vect in [win_vect, get_opposite_vect(win_vect)]:
                mover = new_input
                mover_val = map[mover[0]][mover[1]]
                while mover_val == self.input_char:
                    score += 1
                    mover = sum_vect(mover, vect)
                    if self.is_out_of_map(mover):
                        break
                    mover_val = map[mover[0]][mover[1]]
            if score == score_to_win:
                return True
        return False

    def draw_game(self, screen, size):
        size = len(screen)
        for y in range(size):
            for x in range(size):
                screen[y][x] = self.game_map[y][x]
        input_pos = self.current_input_pos
        screen[input_pos[0]][input_pos[1]] = self.input_char
