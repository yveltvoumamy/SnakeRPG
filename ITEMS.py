from random import randrange, randint
from time import sleep
import pygame
from pygame.math import Vector2


class Item():
    RES = 1000
    sc = pygame.display.set_mode([RES, RES])
    SIZE = 20 * 2
    coordinate = Vector2(randrange(0, RES, SIZE), randrange(0, RES, SIZE))
    on_board = False
    color = "white"

    def render(self):
        if self.on_board:
            pygame.draw.rect(self.sc, pygame.Color(self.color), (*self.coordinate, self.SIZE, self.SIZE))

    def set_color(self, color_):
        self.color = color_

    def del_item(self):
        self.on_board = False

    # list(x for x in self.coordinate) in list(list(s[0]) for s in mountains.rocks)
    def new_item(self, mountains):
        self.coordinate = Vector2(randrange(0, self.RES, self.SIZE), randrange(0, self.RES, self.SIZE))
        while list(x for x in self.coordinate) in mountains:
            self.coordinate = Vector2(randrange(0, self.RES, self.SIZE), randrange(0, self.RES, self.SIZE))
        self.on_board = True


class Apple(Item):
    on_board = True

    def __init__(self):
        self.img = pygame.image.load('Graphics/items/apple.png').convert_alpha()

    def render(self):
        if self.on_board:
            self.sc.blit(self.img, (*self.coordinate, self.SIZE, self.SIZE))

    def was_eaten(self, snake, mountains):
        snake.changing_lenght(1)
        snake.changing_speed(1)
        self.new_item(list(list(x[0]) for x in mountains.rocks))


class Speeder(Item):
    def __init__(self):
        self.img = pygame.image.load('Graphics/items/bolt.png').convert_alpha()

    def render(self):
        if self.on_board:
            self.sc.blit(self.img, (*self.coordinate, self.SIZE, self.SIZE))

    def was_eaten(self, snake, mountains):
        snake.changing_speed(5)
        self.del_item()


class Slower(Item):
    def __init__(self):
        self.animation = [pygame.image.load('Graphics/items/Snail/snail1.png'),
                          pygame.image.load('Graphics/items/Snail/snail2.png'),
                          pygame.image.load('Graphics/items/Snail/snail3.png')]
        self.animcount = 0

    def render(self):
        if self.on_board:
            self.sc.blit(self.animation[self.animcount // 5], (*self.coordinate, self.SIZE, self.SIZE))
            self.animcount += 1
            if self.animcount > 14:
                self.animcount = 0

    def was_eaten(self, snake, mountains):
        snake.changing_speed(-5)
        self.del_item()


class BusterPoints(Item):
    def __init__(self):
        self.animation = [pygame.image.load('Graphics/items/coin/01coin (0).png'),
                          pygame.image.load('Graphics/items/coin/01coin (1).png'),
                          pygame.image.load('Graphics/items/coin/01coin (2).png'),
                          pygame.image.load('Graphics/items/coin/01coin (3).png'),
                          pygame.image.load('Graphics/items/coin/01coin (4).png'),
                          pygame.image.load('Graphics/items/coin/01coin (5).png'),
                          pygame.image.load('Graphics/items/coin/01coin (6).png'),
                          pygame.image.load('Graphics/items/coin/01coin (7).png')]
        self.animcount = 0

    def render(self):
        if self.on_board:
            self.sc.blit(self.animation[self.animcount // 5], (*self.coordinate, self.SIZE, self.SIZE))
            self.animcount += 1
            if self.animcount > 30:
                self.animcount = 0

    def was_eaten(self, snake, mountains):
        snake.coefficient += 1
        self.del_item()


class Screamer(Item):
    def __init__(self):
        self.img = pygame.image.load('Graphics/items/Skul.png').convert_alpha()
        self.img_screamer = [pygame.image.load('Graphics/Screamer/screamer1.png'), pygame.image.load('Graphics/Screamer/screamer2.png'),
                             pygame.image.load('Graphics/Screamer/screamer3.png')]
        self.screamer_sound = pygame.mixer.Sound('Sounds/screamer_sound.wav')

    def render(self):
        if self.on_board:
            self.sc.blit(self.img, (*self.coordinate, self.SIZE, self.SIZE))

    def was_eaten(self, snake, mountains):
        self.screamer_sound.play()
        self.sc.blit(self.img_screamer[randint(0, 2)], (0, 0, self.RES, self.RES))
        pygame.display.flip()
        self.del_item()
        sleep(2)


class Freezer(Item):
    def __init__(self):
        self.img = pygame.image.load('Graphics/items/Snowflake.png').convert_alpha()

    def render(self):
        if self.on_board:
            self.sc.blit(self.img, (*self.coordinate, self.SIZE, self.SIZE))

    def was_eaten(self, snake, mountains):
        pygame.display.flip()
        sleep(5)
        self.del_item()


class Longer(Item):
    def was_eaten(self, snake, mountains):
        snake.changing_lenght(5)
        snake.SCORE += randint(0, 6)
        self.del_item()

    def __init__(self):
        self.animation = [pygame.image.load('Graphics/items/RedMushroom/RedMushroom1.png'),
                          pygame.image.load('Graphics/items/RedMushroom/RedMushroom2.png'),
                          pygame.image.load('Graphics/items/RedMushroom/RedMushroom3.png'),
                          pygame.image.load('Graphics/items/RedMushroom/RedMushroom4.png'),
                          pygame.image.load('Graphics/items/RedMushroom/RedMushroom5.png')]
        self.animcount = 0

    def render(self):
        if self.on_board:
            self.sc.blit(self.animation[self.animcount // 5], (*self.coordinate, self.SIZE, self.SIZE))
            self.animcount += 1
            if self.animcount > 24:
                self.animcount = 0


class Jewish(Item):
    def __init__(self):
        self.animation = [pygame.image.load('Graphics/items/PurpleMushroom/PurpleMushroom1.png'),
                          pygame.image.load('Graphics/items/PurpleMushroom/PurpleMushroom2.png'),
                          pygame.image.load('Graphics/items/PurpleMushroom/PurpleMushroom3.png'),
                          pygame.image.load('Graphics/items/PurpleMushroom/PurpleMushroom4.png'),
                          pygame.image.load('Graphics/items/PurpleMushroom/PurpleMushroom5.png')]
        self.animcount = 0

    def render(self):
        if self.on_board:
            self.sc.blit(self.animation[self.animcount // 5], (*self.coordinate, self.SIZE, self.SIZE))
            self.animcount += 1
            if self.animcount > 24:
                self.animcount = 0

    def was_eaten(self, snake, mountains):
        snake.body = [Vector2(snake.body[0].x, snake.body[0].y),
                      Vector2(snake.body[1].x, snake.body[1].y),
                      Vector2(snake.body[2].x, snake.body[2].y)]
        self.del_item()


class LifeHeart(Item):
    def __init__(self):
        self.img = pygame.image.load('Graphics/items/Heart.png').convert_alpha()

    def render(self):
        if self.on_board:
            self.sc.blit(self.img, (*self.coordinate, self.SIZE, self.SIZE))

    def move(self, snake, mountains):
        self.coordinate = Vector2(randrange(
            self.coordinate[0] - self.SIZE if self.coordinate[0] - self.SIZE > 0 else self.coordinate[0],
            self.coordinate[0] + self.SIZE * 2 if self.coordinate[0] + self.SIZE < self.RES else self.RES, self.SIZE),
            randrange(self.coordinate[1] - self.SIZE if self.coordinate[1] - self.SIZE > 0 else self.coordinate[1],
                      self.coordinate[1] + self.SIZE * 2 if self.coordinate[1] + self.SIZE < self.RES else self.RES,
                      self.SIZE))

        # while list(x for x in self.coordinate) in list(list(y * self.SIZE for y in x) for x in snake.body) or \
        #       list(x for x in self.coordinate) in list(list(s[0]) for s in mountains.rocks):
        while list(x for x in self.coordinate) in list(list(x) for x in snake.body) or \
              list(x for x in self.coordinate) in list(list(s[0]) for s in mountains.rocks):
            self.coordinate = Vector2(randrange(
                self.coordinate[0] - self.SIZE if self.coordinate[0] - self.SIZE > 0 else self.coordinate[0],
                self.coordinate[0] + self.SIZE * 2 if self.coordinate[0] + self.SIZE < self.RES else self.RES,
                self.SIZE), \
                randrange(self.coordinate[1] - self.SIZE if self.coordinate[1] - self.SIZE > 0 else self.coordinate[1],
                          self.coordinate[1] + self.SIZE * 2 if self.coordinate[1] + self.SIZE < self.RES else self.RES,
                          self.SIZE))

    def spawn(self, mountains):
        if not randint(0, 300) and not self.on_board:
            self.new_item(list(list(x[0]) for x in mountains.rocks))
            self.on_board = True

    def run_from(self, snake, mountains):
        if self.on_board and not randint(0, 5):
            self.move(snake, mountains)

    def was_eaten(self, snake, mountains):
        if snake.lifes < snake.maxlifes:
            snake.lifes += 1
        self.del_item()


class RockOnDefaultArea(Item):

    def __init__(self):
        self.sprites = [pygame.image.load('Graphics/items/rocks/rock_on_deafault_area1.png'),
                        pygame.image.load('Graphics/items/rocks/rock_on_default_area2.png'),
                        pygame.image.load('Graphics/items/rocks/rock_on_default_area3.png'),
                        pygame.image.load('Graphics/items/rocks/rock_on_default_area4.png'),
                        pygame.image.load('Graphics/items/rocks/rock_on_default_area5.png')]

        self.rocks_count = randint(10, 100)
        self.count_chains = randint(2, 20)
        self.current_rock_count = 0
        self.rocks = []
        for i in range(self.count_chains):
            if self.rocks_count <= 1:
                self.rocks.append((Vector2(randrange(120, self.RES, self.SIZE), randrange(120, self.RES, self.SIZE)), self.sprites[randint(0, 4)]))
                break
            count_rocks_in_chain = randint(1, self.rocks_count)
            coordinates_previous_rock = Vector2(randrange(120, self.RES, self.SIZE), randrange(120, self.RES, self.SIZE))
            self.rocks.append((coordinates_previous_rock, self.sprites[randint(0, 4)]))
            self.rocks_count -= 1
            for j in range(count_rocks_in_chain - 1):
                coordinates_current_rock = Vector2(randrange(
                    coordinates_previous_rock[0] - self.SIZE if coordinates_previous_rock[0] - self.SIZE > 0 else
                    coordinates_previous_rock[0],
                    coordinates_previous_rock[0] + self.SIZE * 2 if coordinates_previous_rock[
                                                                        0] + self.SIZE < self.RES else self.RES,
                    self.SIZE),
                    randrange(
                        coordinates_previous_rock[1] - self.SIZE if coordinates_previous_rock[1] - self.SIZE > 0 else
                        coordinates_previous_rock[1],
                        coordinates_previous_rock[1] + self.SIZE * 2 if coordinates_previous_rock[
                                                                            1] + self.SIZE < self.RES else self.RES,
                        self.SIZE))
                self.rocks.append((coordinates_current_rock, self.sprites[randint(0, 4)]))
                coordinates_previous_rock = coordinates_current_rock
                self.rocks_count -= 1

    def render(self):
        for i in range(len(self.rocks)):
            self.sc.blit(self.rocks[i][1], (*self.rocks[i][0], self.SIZE, self.SIZE))

    def in_rocks(self, snake):
        # if list(i * self.SIZE for i in snake.body[0]) in list(list(x[0]) for x in self.rocks):
        if list(snake.body[0]) in list(list(x[0]) for x in self.rocks):
            if snake.lifes == 1:
                snake.alive = False
            else:
                snake.lifes -= 1
                snake.reset()


class RockOnBosssArea(RockOnDefaultArea):
    def __init__(self):
        self.sprites = sprites = [pygame.image.load('Graphics/items/rocks/rock_on_boss_area1.png'),
                                  pygame.image.load('Graphics/items/rocks/rock_on_boss_area2.png'),
                                  pygame.image.load('Graphics/items/rocks/rock_on_boss_area3.png'),
                                  pygame.image.load('Graphics/items/rocks/rock_on_boss_area4.png'),
                                  pygame.image.load('Graphics/items/rocks/rock_on_boss_area5.png')]

        self.rocks_count = randint(10, 200)
        self.count_chains = randint(2, 50)

        self.current_rock_count = 0
        self.rocks = []
        for i in range(self.count_chains):
            if self.rocks_count <= 1:
                self.rocks.append((Vector2(randrange(120, self.RES, self.SIZE), randrange(120, self.RES, self.SIZE)),
                                   self.sprites[randint(0, 4)]))
                break
            count_rocks_in_chain = randint(1, self.rocks_count)
            coordinates_previous_rock = Vector2(randrange(120, self.RES, self.SIZE),
                                                randrange(120, self.RES, self.SIZE))
            self.rocks.append((coordinates_previous_rock, self.sprites[randint(0, 4)]))
            self.rocks_count -= 1
            for j in range(count_rocks_in_chain - 1):
                coordinates_current_rock = Vector2(randrange(
                    coordinates_previous_rock[0] - self.SIZE if coordinates_previous_rock[0] - self.SIZE > 0 else
                    coordinates_previous_rock[0],
                    coordinates_previous_rock[0] + self.SIZE * 2 if coordinates_previous_rock[
                                                                        0] + self.SIZE < self.RES else self.RES,
                    self.SIZE),
                    randrange(
                        coordinates_previous_rock[1] - self.SIZE if coordinates_previous_rock[1] - self.SIZE > 0 else
                        coordinates_previous_rock[1],
                        coordinates_previous_rock[1] + self.SIZE * 2 if coordinates_previous_rock[
                                                                            1] + self.SIZE < self.RES else self.RES,
                        self.SIZE))
                self.rocks.append((coordinates_current_rock, self.sprites[randint(0, 4)]))
                coordinates_previous_rock = coordinates_current_rock
                self.rocks_count -= 1