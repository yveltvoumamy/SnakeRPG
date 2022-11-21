# Pygame шаблон - скелет для нового проекта Pygame
from RPG_SCENE import *


def start_menu():
    menu = Menu()
    menu.append_option('Start the game', lambda: scene_RPG())
    menu.append_option('Rating board', lambda: open_rating_board())
    menu.append_option('Clean rating board', lambda: clean_rating_board())
    shop_alive(menu)


def open_rating_board():
    global sc
    f = open('txt/rating_board.txt')
    data = []
    for x in f:
        data.append(str(x))
    board = Menu()
    for i in range(len(data)):
        text = data[i][:-1]
        board.append_option(text, lambda: ...)
    shop_alive(board)


if __name__ == "__main__":
    start_menu()
