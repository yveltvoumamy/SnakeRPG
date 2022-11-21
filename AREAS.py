from ITEMS import *


class Area(Item):
    def __init__(self):
        self.weight = randrange(400, self.RES, self.SIZE)
        self.height = randrange(400, self.RES, self.SIZE)
        self.in_area = False

        self.new_item([])
        self.on_board = True

    def new_coordinates(self):
        self.weight = randrange(300, Item.RES, Item.SIZE)
        self.height = randrange(300, Item.RES, Item.SIZE)

    def render_img(self):
        if self.on_board:
            for h in range(int(self.coordinate[1]), int(self.coordinate[1]) + self.height, self.SIZE):
                for w in range(int(self.coordinate[0]), int(self.coordinate[0]) + self.weight, self.SIZE):
                    self.sc.blit(self.sprite, (w, h, self.SIZE, self.SIZE))

    def render(self):
        if self.on_board:
            pygame.draw.rect(self.sc, pygame.Color(self.color),
                             (*self.coordinate, self.weight, self.height))

    def check_in_area(self, snake):
        '''
        if not self.in_area and self.coordinate[0] <= snake.body[0].x * snake.SIZE <= self.coordinate[0] + self.weight - snake.SIZE \
                and self.coordinate[1] <= snake.body[0].y * snake.SIZE <= self.coordinate[1] + self.height - snake.SIZE \
                and snake.direction != Vector2(0, 0):
        '''
        if not self.in_area and self.coordinate[0] <= snake.body[0].x <= self.coordinate[0] + self.weight - snake.SIZE \
                and self.coordinate[1] <= snake.body[0].y <= self.coordinate[1] + self.height - snake.SIZE \
                and snake.direction != Vector2(0, 0):
            self.effect(snake)
            self.in_area = True
        elif self.in_area:
            self.out_of_effect(snake)
            self.in_area = False

    def effect(self, snake):
        ...

    def out_of_effect(self, snake):
        ...


class SpeedArea(Area):
    sprite = pygame.image.load('Graphics/area/speed_area.png')
    def effect(self, snake):
        snake.fps += 1000

    def out_of_effect(self, snake):
        snake.fps -= 1000


class SlowArea(Area):
    sprite = pygame.image.load('Graphics/area/slow_area.png')
    last_speed = 30

    def effect(self, snake):
        if snake.fps > 2:
            self.last_speed = snake.fps
        snake.fps = 2

    def out_of_effect(self, snake):
        snake.fps = self.last_speed


class GrowArea(Area):
    sprite = pygame.image.load('Graphics/area/grow_area.png')

    def effect(self, snake):
        snake.changing_lenght(1)
        if randint(0, 2):
            snake.SCORE += 1

    def out_of_effect(self, snake):
        ...


class JewishArea(Area):
    sprite = pygame.image.load('Graphics/area/holy_water.png')
    def __init__(self):
        self.weight = Item.SIZE
        self.height = randrange(300, Item.RES, Item.SIZE)
        self.in_area = False

        self.new_item([])
        self.on_board = True

    def new_coordinates(self):
        self.height = randrange(300, Item.RES, Item.SIZE)
        self.weight = Item.SIZE

    def effect(self, snake):
        snake.body = [Vector2(snake.body[0].x + snake.direction.x, snake.body[0].y), \
                      Vector2(snake.body[0].x + snake.direction.x, snake.body[0].y), \
                      Vector2(snake.body[0].x + snake.direction.x, snake.body[0].y)]

    def out_of_effect(self, snake):
        snake.lifes = snake.lifes - 1 if snake.lifes - 1 >= 0 else snake.lifes # умер от жадности
        if snake.lifes == 0:
            snake.alive = False
        snake.coefficient += 1