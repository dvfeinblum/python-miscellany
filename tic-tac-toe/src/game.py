from random import randint


class Game:
    def __init__(self, player_first: bool = True):
        self.player_first = player_first
        if self.player_first:
            self.player = 'X'
            self.cpu = 'O'
            self.is_player_turn = True
        else:
            self.player = 'O'
            self.cpu = 'X'
            self.is_player_turn = False
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.is_complete = False
        self.move_count = 0

    def _print_board(self):
        for row in self.board:
            print(''.join(row))

    def _calculate_cpu_move(self):
        x, y = (1, 1) if self.move_count < 2 else (randint(0, 2), randint(0, 2))
        if self.board[y][x] == '-':
            self.board[y][x] = self.cpu
        else:
            self._calculate_cpu_move()
        self.is_player_turn = True

    def _player_move(self, move: tuple):
        [x, y] = move
        if x > 2 or y > 2:
            self._player_move(eval(input('Invalid move! Remember that x and y must be less than 2.')))
        if self.board[y][x] == '-':
            self.board[y][x] = self.player
        else:
            self._player_move(eval(input('That square is already taken! Try another one:')))
        self.is_player_turn = False

    def _check_game(self):
        player_won_diagonal = [[], []]
        cpu_won_diagonal = [[], []]
        for i in range(3):
            player_won_down = []
            cpu_won_down = []

            # Checks for across
            if self.board[i] == [self.player]*3:
                return 'Player'
            elif self.board[i] == [self.cpu]*3:
                return 'CPU'

            # Checks for down
            for j in range(3):
                player_won_down.append(self.board[j][i] == self.player)
                cpu_won_down.append(self.board[j][i] == self.cpu)
            if all(player_won_down):
                return 'Player'
            elif all(cpu_won_down):
                return 'CPU'

            # Checks diagonal
            player_won_diagonal[0].append(self.board[i][i] == self.player)
            player_won_diagonal[1].append(self.board[i][2-i] == self.player)
            cpu_won_diagonal[0].append(self.board[i][i] == self.cpu)
            cpu_won_diagonal[1].append(self.board[i][2-i] == self.cpu)

        if all(player_won_diagonal[0]) or all(player_won_diagonal[1]):
            return 'Player'
        elif all(cpu_won_diagonal[0] or all(cpu_won_diagonal[1])):
            return 'CPU'

    def play_turn(self):
        if self.move_count >= 9:
            self.is_complete = True
            print('Looks like we have a draw!')
            return
        if self.is_player_turn:
            self._player_move(eval(input("Enter a move! Positions should be of the form (x,y).")))
        else:
            print('CPU is making a move.')
            self._calculate_cpu_move()
        self.move_count += 1
        self._print_board()
        game_state = self._check_game()
        if game_state:
            print(f'We have a winner! {game_state} has won.')
            self.is_complete = True


def start_game():
    game = Game(randint == 0)
    print('Starting a new game!')
    while not game.is_complete:
        game.play_turn()
    if input('Would you like to play again (y,n)?').lower() == 'y':
        start_game()
    else:
        exit()
