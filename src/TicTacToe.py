import copy
import pygame
import random

class TicTacToe:

    def __init__(self, playing_computer=False):
        self.game_board = [0] * 9
        self.moves = [0] * 9
        self.curr_player = random.choice([1, 2])
        self.playing_computer = playing_computer
        if self.playing_computer:
            self.computer_player = 1 if self.curr_player == 2 else 2

    def process_move(self, move, player):
        '''Returns:
        1 if player 1 (X) wins
        2 if player 2 (O) wins
        0 if draw
        -1 if game not over
        '''

        self.moves[move] = 1
        self.game_board[move] = player

        if self.is_over(self.game_board):
            return player

        if all(x == 1 for x in self.moves):
            return 0

        if not self.playing_computer:
            self.change_curr_player()

        return -1

    def is_over(self, board):
        win_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]

        for pos in win_pos:
            if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] \
                    and board[pos[0]] != 0:
                return True
        return False

    def check_valid_move(self, move):
        return self.moves[move] != 1

    def change_curr_player(self):
        self.curr_player = 1 if self.curr_player == 2 else 2

    def update_board(self):
        images = {1 : 'x.png', 2 : 'o.png'}
        board_images = []
        for i in range(9):
            if self.moves[i] == 1:
                image = pygame.image.load(images[self.game_board[i]])
                board_images.append(image)
            else:
                board_images.append(None)
        return board_images

    def win_available(self, player):
        for i in range(len(self.game_board)):
            if self.moves[i] == 0:
                dup_board = copy.copy(self.game_board)
                dup_board[i] = player
                if self.is_over(dup_board):
                    return i
        return -1

    def computer_move(self):

        win_strat = self.win_available(self.computer_player)
        if win_strat != -1:
            return win_strat

        block = self.win_available(self.curr_player)
        if block != -1:
            return block

        two_sides = [[1, 3, 0], [1, 5, 2], [3, 7, 6], [5, 7, 8]]
        for side in two_sides:
            if self.game_board[side[0]] == self.curr_player and self.game_board[side[1]] == self.curr_player:
                if self.moves[side[2]] == 0:
                    return side[2]

        if self.moves[4] == 0:
            return 4

        possible_corners = [corner for corner in [0, 2, 6, 8] if self.moves[corner] == 0]
        if len(possible_corners) > 0:
            return random.choice(possible_corners)

        return random.choice([i for i in range(len(self.moves)) if self.moves[i] == 0])
