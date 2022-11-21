from pygame import *
from random import *
import pygame.math


class snaryad():

    def __init__(self, coordinate, size, img, facing):
        self.coordinate = coordinate
        self.img = img
        self.size = size
        self.facing = facing
        self.vel = (40 * facing[0], 40 * facing[1])

    def draw(self, sc):
        sc.blit(self.img[randint(0, 1)], (*self.coordinate, self.size, self.size))


class Eyeball():
    delay = 6
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load('Graphics/bosses/Eyeball/eyeball_right 80x60/eyeball_right1.png'),
                      pygame.image.load('Graphics/bosses/Eyeball/eyeball_right 80x60/eyeball_right2.png'),
                      pygame.image.load('Graphics/bosses/Eyeball/eyeball_right 80x60/eyeball_right3.png'),
                      pygame.image.load('Graphics/bosses/Eyeball/eyeball_right 80x60/eyeball_right4.png'),
                      pygame.image.load('Graphics/bosses/Eyeball/eyeball_right 80x60/eyeball_right5.png'),
                      pygame.image.load('Graphics/bosses/Eyeball/eyeball_right 80x60/eyeball_right6.png')]

        self.left = [pygame.image.load('Graphics/bosses/Eyeball/eyeball_left 80x60/eyeball_left1.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_left 80x60/eyeball_left2.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_left 80x60/eyeball_left3.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_left 80x60/eyeball_left4.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_left 80x60/eyeball_left5.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_left 80x60/eyeball_left6.png')]

        self.up = [pygame.image.load('Graphics/bosses/Eyeball/eyeball_up 80x60/eyeball_up1.png'),
                   pygame.image.load('Graphics/bosses/Eyeball/eyeball_up 80x60/eyeball_up2.png'),
                   pygame.image.load('Graphics/bosses/Eyeball/eyeball_up 80x60/eyeball_up3.png'),
                   pygame.image.load('Graphics/bosses/Eyeball/eyeball_up 80x60/eyeball_up4.png'),
                   pygame.image.load('Graphics/bosses/Eyeball/eyeball_up 80x60/eyeball_up5.png'),
                   pygame.image.load('Graphics/bosses/Eyeball/eyeball_up 80x60/eyeball_up6.png')]

        self.down = [pygame.image.load('Graphics/bosses/Eyeball/eyeball_down 80x60/eyeball_down1.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_down 80x60/eyeball_down2.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_down 80x60/eyeball_down3.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_down 80x60/eyeball_down4.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_down 80x60/eyeball_down5.png'),
                     pygame.image.load('Graphics/bosses/Eyeball/eyeball_down 80x60/eyeball_down6.png')]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = [(pygame.image.load('Graphics/bosses/Eyeball/bullet 80x60/bullet_right.png'),
                        pygame.image.load('Graphics/bosses/Eyeball/bullet 80x60/bullet_right.png')),

                       (pygame.image.load('Graphics/bosses/Eyeball/bullet 80x60/bullet_left.png'),
                       pygame.image.load('Graphics/bosses/Eyeball/bullet 80x60/bullet_left.png')),

                       (pygame.image.load('Graphics/bosses/Eyeball/bullet 80x60/bullet_up.png'),
                        pygame.image.load('Graphics/bosses/Eyeball/bullet 80x60/bullet_up.png')),

                        (pygame.image.load('Graphics/bosses/Eyeball/bullet 80x60/bullet_down.png'),
                         pygame.image.load('Graphics/bosses/Eyeball/bullet 80x60/bullet_down.png'))]

        self.direcctions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        self.choose_action()

    def choose_action(self):
        self.animcount = 0
        r = randint(0, 3)
        self.current_action = self.actions[r]

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                   self.bullet[self.actions.index(self.current_action)],
                                   self.direcctions[self.actions.index(self.current_action)]))
            self.choose_action()
        self.animcount += 1
        x = 0
        for i in range(self.lifes):
            pygame.draw.rect(self.sc, pygame.Color('red'), (100 + x, 980, 40, 10))
            x += 40

    def move_from(self, snake):
        if not randint(0, 10):
            self.coordinate = Vector2(randrange(
                self.coordinate[0] - self.width if self.coordinate[0] - self.width > 0 else self.coordinate[0],
                self.coordinate[0] + self.width * 2 if self.coordinate[0] + self.width < self.RES else self.RES, self.width),
                randrange(self.coordinate[1] - self.width if self.coordinate[1] - self.width > 0 else self.coordinate[1],
                          self.coordinate[1] + self.width * 2 if self.coordinate[1] + self.width < self.RES else self.RES,
                          self.width))
            while list(x for x in self.coordinate) in list(list(y * self.width for y in x) for x in snake.body)\
                    or self.coordinate.x < 0 or self.coordinate.x > self.RES or self.coordinate.y < 0 or \
                    self.coordinate.y > self.RES:
                self.coordinate = Vector2(randrange(
                    self.coordinate[0] - self.width if self.coordinate[0] - self.width > 0 else self.coordinate[0],
                    self.coordinate[0] + self.width * 2 if self.coordinate[0] + self.width < self.RES else self.RES,
                    self.width), \
                    randrange(self.coordinate[1] - self.width if self.coordinate[1] - self.width > 0 else self.coordinate[1],
                              self.coordinate[1] + self.width * 2 if self.coordinate[1] + self.width < self.RES else self.RES,
                              self.width))


class Ghost(Eyeball):
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.delay = 2
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load('Graphics/bosses/ghost/ghost_right/ghost_right1.png'),
                      pygame.image.load('Graphics/bosses/ghost/ghost_right/ghost_right2.png'),
                      pygame.image.load('Graphics/bosses/ghost/ghost_right/ghost_right3.png'),
                      pygame.image.load('Graphics/bosses/ghost/ghost_right/ghost_right4.png'),
                      pygame.image.load('Graphics/bosses/ghost/ghost_right/ghost_right5.png'),
                      pygame.image.load('Graphics/bosses/ghost/ghost_right/ghost_right6.png')]

        self.left = [pygame.image.load('Graphics/bosses/ghost/ghost_left/ghost_left1.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_left/ghost_left2.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_left/ghost_left3.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_left/ghost_left4.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_left/ghost_left5.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_left/ghost_left6.png')]

        self.up = [pygame.image.load('Graphics/bosses/ghost/ghost_up/ghost_up1.png'),
                   pygame.image.load('Graphics/bosses/ghost/ghost_up/ghost_up2.png'),
                   pygame.image.load('Graphics/bosses/ghost/ghost_up/ghost_up3.png'),
                   pygame.image.load('Graphics/bosses/ghost/ghost_up/ghost_up4.png'),
                   pygame.image.load('Graphics/bosses/ghost/ghost_up/ghost_up5.png'),
                   pygame.image.load('Graphics/bosses/ghost/ghost_up/ghost_up6.png')]

        self.down = [pygame.image.load('Graphics/bosses/ghost/ghost_down/ghost_down1.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_down/ghost_down2.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_down/ghost_down3.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_down/ghost_down4.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_down/ghost_down5.png'),
                     pygame.image.load('Graphics/bosses/ghost/ghost_down/ghost_down6.png')]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = [((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_down2.png'))),

                       ((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_down2.png'))),

                       ((pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_down2.png'))),

                       ((pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_right1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_right2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_left1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_left2.png')))]

        self.direcctions = [((1, -1), (-1, 1)), ((-1, -1), (1, 1)), ((0, -1), (0, 1)), ((1, 0), (-1, 0))]
        self.choose_action()

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                   self.bullet[self.actions.index(self.current_action)][0],
                                   self.direcctions[self.actions.index(self.current_action)][0]))
            bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                   self.bullet[self.actions.index(self.current_action)][1],
                                   self.direcctions[self.actions.index(self.current_action)][1]))
            self.choose_action()
        self.animcount += 1


class BigWorm(Eyeball):
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.delay = 2
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load('Graphics/bosses/big_worm/big_worm_right/worm_right1.png'),
                      pygame.image.load('Graphics/bosses/big_worm/big_worm_right/worm_right2.png'),
                      pygame.image.load('Graphics/bosses/big_worm/big_worm_right/worm_right3.png'),
                      pygame.image.load('Graphics/bosses/big_worm/big_worm_right/worm_right4.png'),
                      pygame.image.load('Graphics/bosses/big_worm/big_worm_right/worm_right5.png'),
                      pygame.image.load('Graphics/bosses/big_worm/big_worm_right/worm_right6.png')]

        self.left = [pygame.image.load('Graphics/bosses/big_worm/big_worm_left/worm_left1.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_left/worm_left2.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_left/worm_left3.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_left/worm_left4.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_left/worm_left5.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_left/worm_left6.png')]

        self.up = [pygame.image.load('Graphics/bosses/big_worm/big_worm_up/worm_up1.png'),
                   pygame.image.load('Graphics/bosses/big_worm/big_worm_up/worm_up2.png'),
                   pygame.image.load('Graphics/bosses/big_worm/big_worm_up/worm_up3.png'),
                   pygame.image.load('Graphics/bosses/big_worm/big_worm_up/worm_up4.png'),
                   pygame.image.load('Graphics/bosses/big_worm/big_worm_up/worm_up5.png'),
                   pygame.image.load('Graphics/bosses/big_worm/big_worm_up/worm_up6.png')]

        self.down = [pygame.image.load('Graphics/bosses/big_worm/big_worm_down/worm_down1.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_down/worm_down2.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_down/worm_down3.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_down/worm_down4.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_down/worm_down5.png'),
                     pygame.image.load('Graphics/bosses/big_worm/big_worm_down/worm_down6.png')]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = [((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_down2.png')),
                        ),
                       ((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_down2.png')),
                        ),
                       ((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_up2.png')),
                       ),
                       ((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_down2.png')),
                       (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_down1.png'),
                        pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_down2.png')),
                       )
                    ]

        self.direcctions = [((1, -1), (1, 1)), ((-1, -1), (-1, 1)), ((1, -1), (-1, -1)), ((1, 1), (-1, 1))]
        self.choose_action()

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            for i in range(len(self.bullet[self.actions.index(self.current_action)])):
                bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                       self.bullet[self.actions.index(self.current_action)][i],
                                       self.direcctions[self.actions.index(self.current_action)][i]))
            self.choose_action()
        self.animcount += 1

class Pumpking(Eyeball):
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.delay = 2
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load('Graphics/bosses/pumpkin/pumpkin_right/pumpkin_right1.png'),
                      pygame.image.load('Graphics/bosses/pumpkin/pumpkin_right/pumpkin_right2.png'),
                      pygame.image.load('Graphics/bosses/pumpkin/pumpkin_right/pumpkin_right3.png'),
                      pygame.image.load('Graphics/bosses/pumpkin/pumpkin_right/pumpkin_right4.png'),
                      pygame.image.load('Graphics/bosses/pumpkin/pumpkin_right/pumpkin_right5.png'),
                      pygame.image.load('Graphics/bosses/pumpkin/pumpkin_right/pumpkin_right6.png')]

        self.left = [pygame.image.load('Graphics/bosses/pumpkin/pumpkin_left/pumpkin_left1.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_left/pumpkin_left2.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_left/pumpkin_left3.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_left/pumpkin_left4.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_left/pumpkin_left5.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_left/pumpkin_left6.png')]

        self.up = [pygame.image.load('Graphics/bosses/pumpkin/pumpkin_up/pumpkin_up1.png'),
                   pygame.image.load('Graphics/bosses/pumpkin/pumpkin_up/pumpkin_up2.png'),
                   pygame.image.load('Graphics/bosses/pumpkin/pumpkin_up/pumpkin_up3.png'),
                   pygame.image.load('Graphics/bosses/pumpkin/pumpkin_up/pumpkin_up4.png'),
                   pygame.image.load('Graphics/bosses/pumpkin/pumpkin_up/pumpkin_up5.png'),
                   pygame.image.load('Graphics/bosses/pumpkin/pumpkin_up/pumpkin_up6.png')]

        self.down = [pygame.image.load('Graphics/bosses/pumpkin/pumpkin_down/pumpkin_down1.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_down/pumpkin_down2.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_down/pumpkin_down3.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_down/pumpkin_down4.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_down/pumpkin_down5.png'),
                     pygame.image.load('Graphics/bosses/pumpkin/pumpkin_down/pumpkin_down6.png')]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = [((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_down2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_right1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_right2.png'))
                        ),
                       ((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_down2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_left1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_left2.png'))
                        ),
                       ((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_up2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_up1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_up2.png'))
                        ),
                       ((pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_down2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_down2.png')),
                        (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_down1.png'),
                         pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_down2.png'))
                        )
                       ]

        self.direcctions = [((1, -1), (1, 1), (1, 0)), ((-1, -1), (-1, 1), (-1, 0)), ((1, -1), (-1, -1), (0, -1)),
                            ((1, 1), (-1, 1), (0, 1))]
        self.choose_action()

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            for i in range(len(self.bullet[self.actions.index(self.current_action)])):
                bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                       self.bullet[self.actions.index(self.current_action)][i],
                                       self.direcctions[self.actions.index(self.current_action)][i]))
            self.choose_action()
        self.animcount += 1


class ManEater(Eyeball):
    def __init__(self):
        self.lifes = 20
        self.current_sprite = None
        self.current_action = None
        self.animcount = None
        self.RES = 1000
        self.coordinate = Vector2(520, 520)
        self.width = 40
        self.height = 40
        self.delay = 2
        self.sc = pygame.display.set_mode([self.RES, self.RES])

        self.right = [pygame.image.load('Graphics/bosses/man_eater/man_eater_right/maneater_right1.png'),
                      pygame.image.load('Graphics/bosses/man_eater/man_eater_right/maneater_right2.png'),
                      pygame.image.load('Graphics/bosses/man_eater/man_eater_right/maneater_right3.png'),
                      pygame.image.load('Graphics/bosses/man_eater/man_eater_right/maneater_right4.png'),
                      pygame.image.load('Graphics/bosses/man_eater/man_eater_right/maneater_right5.png'),
                      pygame.image.load('Graphics/bosses/man_eater/man_eater_right/maneater_right6.png')]

        self.left = [pygame.image.load('Graphics/bosses/man_eater/man_eater_left/maneater_left1.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_left/maneater_left2.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_left/maneater_left3.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_left/maneater_left4.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_left/maneater_left5.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_left/maneater_left6.png')]

        self.up = [pygame.image.load('Graphics/bosses/man_eater/man_eater_up/maneater_up1.png'),
                   pygame.image.load('Graphics/bosses/man_eater/man_eater_up/maneater_up2.png'),
                   pygame.image.load('Graphics/bosses/man_eater/man_eater_up/maneater_up3.png'),
                   pygame.image.load('Graphics/bosses/man_eater/man_eater_up/maneater_up4.png'),
                   pygame.image.load('Graphics/bosses/man_eater/man_eater_up/maneater_up5.png'),
                   pygame.image.load('Graphics/bosses/man_eater/man_eater_up/maneater_up6.png')]

        self.down = [pygame.image.load('Graphics/bosses/man_eater/man_eater_down/maneater_down1.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_down/maneater_down2.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_down/maneater_down3.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_down/maneater_down4.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_down/maneater_down5.png'),
                     pygame.image.load('Graphics/bosses/man_eater/man_eater_down/maneater_down6.png')]

        self.actions = [self.right, self.left, self.up, self.down]

        self.bullet = {
                        (1, 0): (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_right1.png'),
                                 pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_right2.png')),
                        (-1, 0): (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_left1.png'),
                                  pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_left2.png')),
                        (0, -1): (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_up1.png'),
                                  pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_up2.png')),
                        (0, 1): (pygame.image.load('Graphics/bosses/fireball/fireball_straight1/fireball_down1.png'),
                                 pygame.image.load('Graphics/bosses/fireball/fireball_straight2/fireball_down2.png')),
                        (1, 1):  (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_down1.png'),
                                  pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_down2.png')),
                        (1, -1): (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_right_up1.png'),
                                  pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_right_up2.png')),
                        (-1, 1): (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_down1.png'),
                                  pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_down2.png')),
                        (-1, -1): (pygame.image.load('Graphics/bosses/fireball/fireball_diag1/fireball_left_up1.png'),
                                   pygame.image.load('Graphics/bosses/fireball/fireball_diag2/fireball_left_up2.png'))
                        }

        self.direcctions = [[[(1, 0)],
                              [(1, -1), (1, 1)],
                              [(1, -1), (1, 1), (1, 0)],
                              [(1, 1), (1, -1), (-1, 1), (-1, -1)]],
                           [[(-1, 0)],
                              [(-1, -1), (-1, 1)],
                              [(-1, -1), (-1, 1), (-1, 0)],
                              [(1, 1), (1, -1), (-1, 1), (-1, -1)]],

                            [[(0, -1)],
                              [(1, -1), (-1, -1)],
                              [(1, -1), (-1, -1), (0, -1)],
                              [(1, 0), (-1, 0), (0, 1), (0, -1)]],

                            [[(0, 1)],
                              [(1, 1), (-1, 1)],
                              [(1, 1), (-1, 1), (0, 1)],
                              [(1, 0), (-1, 0), (0, 1), (0, -1)]]
                            ]

        self.choose_action()

    def render(self, bullets):
        self.current_sprite = self.current_action[self.animcount // self.delay]
        self.sc.blit(self.current_sprite, (*self.coordinate, 100, 100))
        if self.animcount // self.delay == 5:
            atack = self.direcctions[self.actions.index(self.current_action)][randint(0, 3)]
            for i in range(len(atack)):
                bullets.append(snaryad(Vector2(round(self.coordinate.x), round(self.coordinate.y)), 40,
                                       self.bullet[atack[i]], atack[i]))
            self.choose_action()
        self.animcount += 1