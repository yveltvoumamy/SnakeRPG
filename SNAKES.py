from MENU import *
from ITEMS import Apple
from datetime import datetime


class Snake():
    RES = 1000
    sc = pygame.display.set_mode([RES, RES])
    SIZE = 20 * 2
    fps_start = fps = 10
    coefficient = 1
    SCORE = 0
    alive = True
    lifes = 1
    maxlifes = 3

    def __init__(self):
        self.body = [Vector2(80, 0), Vector2(40, 0), Vector2(0, 0)]
        self.dirs = {'W': False, 'S': True, 'A': False, 'D': True}
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/snakes/DefaultSnake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/snakes/DefaultSnake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/snakes/DefaultSnake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/snakes/DefaultSnake/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/snakes/DefaultSnake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/snakes/DefaultSnake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/snakes/DefaultSnake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/snakes/DefaultSnake/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/snakes/DefaultSnake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/snakes/DefaultSnake/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/snakes/DefaultSnake/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/snakes/DefaultSnake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/snakes/DefaultSnake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/snakes/DefaultSnake/body_bl.png').convert_alpha()
        # self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(40, 0) or head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-40, 0) or head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 40) or head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -40) or head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(40, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-40, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 40):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -40):
            self.tail = self.tail_down

    ##########################################
    def render(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # x_pos = int(block.x * self.SIZE)
            # y_pos = int(block.y * self.SIZE)
            x_pos = int(block.x)
            y_pos = int(block.y)
            block_rect = pygame.Rect(x_pos, y_pos, self.SIZE, self.SIZE)

            if index == 0:
                self.sc.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.sc.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.sc.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.sc.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -40 and next_block.y == -40 or previous_block.y == -40 and next_block.x == -40:
                        self.sc.blit(self.body_tl, block_rect)
                    elif previous_block.x == -40 and next_block.y == 40 or previous_block.y == 40 and next_block.x == -40:
                        self.sc.blit(self.body_bl, block_rect)
                    elif previous_block.x == 40 and next_block.y == -40 or previous_block.y == -40 and next_block.x == 40:
                        self.sc.blit(self.body_tr, block_rect)
                    elif previous_block.x == 40 and next_block.y == 40 or previous_block.y == 40 and next_block.x == 40:
                        self.sc.blit(self.body_br, block_rect)

    def eat(self, item, mountains):
        # if [i * self.SIZE for i in self.body[0]] == item.coordinate:
        if list(self.body[0]) == item.coordinate:
            item.was_eaten(self, mountains)
            self.SCORE += self.coefficient
            if type(item) != Apple:
                item.on_board = False
                self.SCORE += 5 + self.coefficient
            return True

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(40, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-40, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 40):
            self.head = self.head_up
        elif head_relation == Vector2(0, -40):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(40, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-40, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 40):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -40):
            self.tail = self.tail_down

    def move_new(self):
        if self.direction == Vector2(0, 0):
            return
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, self.body[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            self.body[0] += self.direction
            for i in range(1, len(self.body)):
                relation = (self.body[i - 1] - self.body[i]) // 40
                self.body[i] += relation

    def move(self):
        if self.direction == Vector2(0, 0):
            return
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction * 40)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction * 40)
            self.body = body_copy[:]

    def write_down_score(self):
        f = open('txt/rating_board.txt')
        board = []
        for x in f:
            board.append(str(x))
        f.close()
        f = open('txt/rating_board.txt', 'w')
        ans = ''
        for x in board:
            if x.split():
                ans += x
        ans += str(self.SCORE) + ' ' * 15 + str(datetime.now()).split('.')[0] + '\n'
        f.write(ans)
        f.close()
        reset_rating_board()

    def add_block(self):
        self.new_block = True

    def control(self, event):
        if event.key == pygame.K_w and self.dirs['W']:
            self.direction = Vector2(0, -1)
            self.dirs = {'W': True, 'S': False, 'A': True, 'D': True}
        elif event.key == pygame.K_d and self.dirs['D']:
            self.dirs = {'W': True, 'S': True, 'A': False, 'D': True}
            self.direction = Vector2(1, 0)
        elif event.key == pygame.K_s and self.dirs['S']:
            self.dirs = {'W': False, 'S': True, 'A': True, 'D': True}
            self.direction = Vector2(0, 1)
        elif event.key == pygame.K_a and self.dirs['A']:
            self.dirs = {'W': True, 'S': True, 'A': True, 'D': False}
            self.direction = Vector2(-1, 0)
        else:
            return False
        return True

    def game_over(self):
        '''
        if self.body[0].x < 0 or self.body[0].x * self.SIZE > self.RES - self.SIZE or self.body[0].y < 0 or \
                self.body[0].y * self.SIZE > self.RES - self.SIZE:
        '''
        if self.body[0].x < 0 or self.body[0].x > self.RES - self.SIZE or self.body[0].y < 0 or \
                self.body[0].y > self.RES - self.SIZE:
            if self.lifes == 1:
                self.alive = False
            else:
                self.lifes -= 1
                self.reset()

        if len(list(self.body)) != len(set(tuple(x) for x in self.body)):
            if self.lifes == 1:
                self.alive = False
            else:
                self.lifes -= 1
                # self.body[0].x, self.body[0].y = self.RES // 2, self.RES // 2
                self.reset()

    def reset(self):
        self.dirs = {'W': False, 'S': True, 'A': False, 'D': True}
        self.body = [Vector2(80, 0), Vector2(40, 0), Vector2(0, 0)]
        self.direction = Vector2(0, 0)
        self.fps = self.fps_start

    def changing_lenght(self, num):
        if num < 0 and len(self.body) - 4 > num:
            body_copy = self.body[:num - 1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        else:
            for i in range(num):
                body_copy = self.body[:]
                body_copy.insert(-1, Vector2(body_copy[-1].x, body_copy[-1].y - i))
                self.body = body_copy[:]

    def changing_speed(self, num):
        if self.fps <= abs(num):
            ...
        else:
            self.fps += num

    def changing_maxlifes(self, num):
        self.maxlifes += num


class PortalSnake(Snake):
    def __init__(self):
        self.body = [Vector2(80, 0), Vector2(40, 0), Vector2(0, 0)]
        self.dirs = {'W': True, 'S': True, 'A': True, 'D': False}
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/snakes/PortalSnake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/snakes/PortalSnake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/snakes/PortalSnake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/snakes/PortalSnake/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/snakes/PortalSnake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/snakes/PortalSnake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/snakes/PortalSnake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/snakes/PortalSnake/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/snakes/PortalSnake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/snakes/PortalSnake/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/snakes/PortalSnake/body_tr1.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/snakes/PortalSnake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/snakes/PortalSnake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/snakes/PortalSnake/body_bl.png').convert_alpha()

    def game_over(self):
        # if self.body[0].x < 0 or self.body[0].x * self.SIZE > self.RES - self.SIZE or self.body[0].y < 0 or \
        #         self.body[0].y * self.SIZE > self.RES - self.SIZE:
        if self.body[0].x < 0 or self.body[0].x > self.RES - self.SIZE or self.body[0].y < 0 or \
                self.body[0].y > self.RES - self.SIZE:
            if self.body[0].x < 0:
                self.body[0].x = self.RES
            elif self.body[0].x > self.RES - self.SIZE:
                self.body[0].x = 0
            elif self.body[0].y < 0:
                self.body[0].y = self.RES
            elif self.body[0].y > self.RES - self.SIZE:
                self.body[0].y = 0
        if len(list(self.body)) != len(set(tuple(x) for x in self.body)):
            if self.lifes == 1:
                self.alive = False
            else:
                self.lifes -= 1
                # self.body[0].x, self.body[0].y = self.RES // 2, self.RES // 2
                self.reset()


class HugeFaceSnake(Snake):
    def __init__(self):
        self.body = [Vector2(80, 0), Vector2(40, 0), Vector2(0, 0)]
        self.dirs = {'W': True, 'S': True, 'A': False, 'D': True}
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/snakes/HugeFaceSnake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/snakes/HugeFaceSnake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/snakes/HugeFaceSnake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/snakes/HugeFaceSnake/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/snakes/HugeFaceSnake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/snakes/HugeFaceSnake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/snakes/HugeFaceSnake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/snakes/HugeFaceSnake/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/snakes/HugeFaceSnake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/snakes/HugeFaceSnake/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/snakes/HugeFaceSnake/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/snakes/HugeFaceSnake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/snakes/HugeFaceSnake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/snakes/HugeFaceSnake/body_bl.png').convert_alpha()
        # self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def eat(self, item, mountains):
        '''
        if [i * self.SIZE for i in self.body[0]] == item.coordinate \
                or Vector2(self.body[0].x * self.SIZE + self.SIZE, self.body[0].y * self.SIZE) == item.coordinate \
                or Vector2(self.body[0].x * self.SIZE, self.body[0].y * self.SIZE + self.SIZE) == item.coordinate \
                or Vector2(self.body[0].x * self.SIZE, self.body[0].y * self.SIZE - self.SIZE) == item.coordinate \
                or Vector2(self.body[0].x * self.SIZE - self.SIZE, self.body[0].y * self.SIZE) == item.coordinate:
        '''
        if list(self.body[0]) == item.coordinate \
                or Vector2(self.body[0].x + self.SIZE, self.body[0].y) == item.coordinate \
                or Vector2(self.body[0].x, self.body[0].y + self.SIZE) == item.coordinate \
                or Vector2(self.body[0].x, self.body[0].y - self.SIZE) == item.coordinate \
                or Vector2(self.body[0].x - self.SIZE, self.body[0].y) == item.coordinate:
            item.was_eaten(self, mountains)
            if type(item) != Apple:
                item.on_board = False


class DiabeticSnake(Snake):

    def __init__(self):
        self.body = [Vector2(80, 0), Vector2(40, 0), Vector2(0, 0)]
        self.dirs = {'W': True, 'S': True, 'A': False, 'D': True}
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/snakes/DiabeticSnake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/snakes/DiabeticSnake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/snakes/DiabeticSnake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/snakes/DiabeticSnake/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/snakes/DiabeticSnake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/snakes/DiabeticSnake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/snakes/DiabeticSnake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/snakes/DiabeticSnake/tail_left.png').convert_alpha()
        self.body_vertical = pygame.image.load('Graphics/snakes/DiabeticSnake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/snakes/DiabeticSnake/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/snakes/DiabeticSnake/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/snakes/DiabeticSnake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/snakes/DiabeticSnake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/snakes/DiabeticSnake/body_bl.png').convert_alpha()

    def changing_lenght(self, num):
        ...


class GhostSnake(Snake):
    def __init__(self):
        self.body = [Vector2(80, 0), Vector2(40, 0), Vector2(0, 0)]
        self.dirs = {'W': True, 'S': True, 'A': False, 'D': True}
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/snakes/GhostSnake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/snakes/GhostSnake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/snakes/GhostSnake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/snakes/GhostSnake/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/snakes/GhostSnake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/snakes/GhostSnake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/snakes/GhostSnake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/snakes/GhostSnake/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/snakes/GhostSnake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/snakes/GhostSnake/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/snakes/GhostSnake/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/snakes/GhostSnake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/snakes/GhostSnake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/snakes/GhostSnake/body_bl.png').convert_alpha()

    def render(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # x_pos = int(block.x * self.SIZE)
            # y_pos = int(block.y * self.SIZE)
            x_pos = int(block.x)
            y_pos = int(block.y)
            block_rect = pygame.Rect(x_pos, y_pos, self.SIZE, self.SIZE)

            if index == 0:
                self.sc.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.sc.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x and previous_block.y == next_block.y:
                    if previous_block == Vector2(40, 0):
                        self.sc.blit(self.tail_left, block_rect)
                    elif previous_block == Vector2(-40, 0):
                        self.sc.blit(self.tail_right, block_rect)
                    elif previous_block == Vector2(0, 40):
                        self.sc.blit(self.tail_up, block_rect)
                    elif previous_block == Vector2(0, -40):
                        self.sc.blit(self.tail_down, block_rect)

                elif previous_block.x == next_block.x:
                    self.sc.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.sc.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -40 and next_block.y == -40 or previous_block.y == -40 and next_block.x == -40:
                        self.sc.blit(self.body_tl, block_rect)
                    elif previous_block.x == -40 and next_block.y == 40 or previous_block.y == 40 and next_block.x == -40:
                        self.sc.blit(self.body_bl, block_rect)
                    elif previous_block.x == 40 and next_block.y == -40 or previous_block.y == -40 and next_block.x == 40:
                        self.sc.blit(self.body_tr, block_rect)
                    elif previous_block.x == 40 and next_block.y == 40 or previous_block.y == 40 and next_block.x == 40:
                        self.sc.blit(self.body_br, block_rect)

    def game_over(self):
        # if self.body[0].x < 0 or self.body[0].x * self.SIZE > self.RES - self.SIZE or self.body[0].y < 0 or \
        #         self.body[0].y * self.SIZE > self.RES - self.SIZE:
        if self.body[0].x < 0 or self.body[0].x > self.RES - self.SIZE or self.body[0].y < 0 or \
                self.body[0].y > self.RES - self.SIZE:
            if self.lifes == 1:
                self.alive = False
            else:
                self.lifes -= 1
                self.reset()

    def control(self, event):
        if event.key == pygame.K_w:
            self.direction = Vector2(0, -1)
        elif event.key == pygame.K_d:
            self.direction = Vector2(1, 0)
        elif event.key == pygame.K_s:
            self.direction = Vector2(0, 1)
        elif event.key == pygame.K_a:
            self.direction = Vector2(-1, 0)
        else:
            return False
        return True


class SpeederSnake(Snake):
    def __init__(self):
        self.body = [Vector2(80, 0), Vector2(40, 0), Vector2(0, 0)]
        self.dirs = {'W': True, 'S': True, 'A': False, 'D': True}
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/snakes/SpeederSnake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/snakes/SpeederSnake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/snakes/SpeederSnake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/snakes/SpeederSnake/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/snakes/SpeederSnake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/snakes/SpeederSnake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/snakes/SpeederSnake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/snakes/SpeederSnake/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/snakes/SpeederSnake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/snakes/SpeederSnake/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/snakes/SpeederSnake/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/snakes/SpeederSnake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/snakes/SpeederSnake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/snakes/SpeederSnake/body_bl.png').convert_alpha()

    last = {'S': False, 'L': True}

    def control(self, event):
        if event.key == pygame.K_SPACE:
            if self.last['L']:
                self.fps += 10
                self.last = {'S': True, 'L': False}
            else:
                self.fps -= 10
                self.last = {'S': False, 'L': True}
        if event.key == pygame.K_w and self.dirs['W']:
            self.direction = Vector2(0, -1)
            self.dirs = {'W': True, 'S': False, 'A': True, 'D': True}
        elif event.key == pygame.K_d and self.dirs['D']:
            self.dirs = {'W': True, 'S': True, 'A': False, 'D': True}
            self.direction = Vector2(1, 0)
        elif event.key == pygame.K_s and self.dirs['S']:
            self.dirs = {'W': False, 'S': True, 'A': True, 'D': True}
            self.direction = Vector2(0, 1)
        elif event.key == pygame.K_a and self.dirs['A']:
            self.dirs = {'W': True, 'S': True, 'A': True, 'D': False}
            self.direction = Vector2(-1, 0)

        else:
            return False
        return True