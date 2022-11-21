import pygame.event
from pygame import *

init()
ARIAL_50 = font.SysFont('arial', 50)


class Menu:
    def __init__(self):
        self._options = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._options.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._options) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._options):
            option_rect: Rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)




'''
font_score = pygame.font.SysFont('Arial', 26, bold=True)
render_lifes = font_score.render(f'LIFES: {snake.lifes} / {snake.maxlifes}', 1, pygame.Color('darkred'))
sc.blit(render_lifes, (5, 5))
'''


def clean_rating_board():
    f = open('txt/rating_board.txt', 'w')
    f.close()


def reset_rating_board():
    board = open('txt/rating_board.txt')
    rating = []
    lines = {}
    for x in board:
        curr_line = x.split()
        if curr_line:
            rating.append(int(curr_line[0]))
            lines[curr_line[0]] = str(x)

    rating.sort(reverse=True)
    deleted = -1
    if len(rating) > 10:
        deleted = rating[0]
        rating.pop(0)
    board = open('txt/rating_board.txt', 'w')
    board.close()
    board = open('txt/rating_board.txt', 'w')
    for i in range(len(rating)):
        if rating[i] != deleted:
            board.write(lines[str(rating[i])])
