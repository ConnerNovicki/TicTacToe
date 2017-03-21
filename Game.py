import time

import pygame

from TicTacToe import TicTacToe

def initiate_game():
    size = 600, 600
    gameDisplay = pygame.display.set_mode(size)
    pygame.display.set_caption('tic-tac-toe')
    clock = pygame.time.Clock()
    bg = pygame.image.load("tic-tac-toe.png")
    return size, gameDisplay, clock, bg


def get_move(size, x, y):
    width, height = size
    if x < (width / 3):
        x_pos = 0
    elif x < (2 * width / 3):
        x_pos = 1
    else:
        x_pos = 2

    if y < (height / 3):
        y_pos = 0
    elif y < (2 * height / 3):
        y_pos = 1
    else:
        y_pos = 2

    return y_pos * 3 + x_pos


def check_game_status(game_status, board_images):
    dict = {0 : 'It\'s a Draw', 1: 'X wins', 2 : 'O wins'}
    display_board_images(board_images)
    time.sleep(.25)
    if game_status in range(3):
        message_display(dict[game_status], (width/2, height/2))
        time.sleep(2)
        main_menu()


def display_board_images(board_images):
    for i, image in enumerate(board_images):
        position = ((i % 3) * 200 + 20, i // 3 * 200 + 20)
        gameDisplay.blit(image, position) if image else None
    pygame.display.update()


def game_loop(v_comp):
    game = TicTacToe(playing_computer=v_comp)
    board_images = []
    game_status = -1
    while True:
        gameDisplay.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                move = get_move(size, x, y)
                if not game.check_valid_move(move):
                    break
                game_status = game.process_move(move, game.curr_player)
                board_images = game.update_board()
                check_game_status(game_status, board_images)
                if game.playing_computer:
                    display_board_images(board_images)
                    comp_move = game.computer_move()
                    game_status = game.process_move(comp_move, game.computer_player)
                    board_images = game.update_board()
                    check_game_status(game_status, board_images)
        display_board_images(board_images)
        clock.tick(10)


def text_objects(text, font, color=(0,0,0)):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text, point, fontsize=90):
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf',fontsize)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (point)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def main_menu():
    color1, color2 = black, black
    while True:
        text1pos, text2pos = (width/2, height / 2 + 20), (width/2, 3 * height / 4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif pygame.mouse.get_pos()[1] in range(int(text1pos[1] - 30), int(text1pos[1] + 30)):
                color1 = blue
                if event.type == pygame.MOUSEBUTTONUP:
                    game_loop(v_comp=True)

            elif pygame.mouse.get_pos()[1] in range(int(text2pos[1] - 30), int(text2pos[1] + 30)):
                color2 = blue
                if event.type == pygame.MOUSEBUTTONUP:
                    game_loop(v_comp=False)

            else:
                color1, color2 = black, black

        gameDisplay.fill(white)
        mediumText = pygame.font.Font('freesansbold.ttf', 50)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf1, TextRect1 = text_objects('Play Computer', mediumText, color=color1)
        TextSurf2, TextRect2 = text_objects('2 Player', mediumText, color=color2)
        TextSurf3, TextRect3 = text_objects('Main Menu', largeText)
        TextRect1.center = text1pos
        TextRect2.center = text2pos
        TextRect3.center = (width/2, height / 4 + 20)
        gameDisplay.blit(TextSurf1, TextRect1)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':

    black = (0,0,0)
    white = (255,255,255)
    blue = (12, 49, 233)

    pygame.init()

    size, gameDisplay, clock, bg = initiate_game()
    width, height = size

    main_menu()
