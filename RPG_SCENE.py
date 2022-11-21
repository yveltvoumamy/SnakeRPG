import pygame

from ITEMS import *
from AREAS import *
from SNAKES import *
from MENU import *
from BATTLE_SCENE import *


ITEMS = [Speeder(), Slower(), BusterPoints(), Screamer(), Freezer(), Longer(), Jewish()]
SNAKES = [Snake(), PortalSnake(), HugeFaceSnake(), DiabeticSnake(), GhostSnake(), SpeederSnake()]
AREAS = [SpeedArea(), SlowArea(), GrowArea(), JewishArea()]

stone_heart = LifeHeart()
mountains = RockOnDefaultArea()
apple = Apple()
gode_mode = False
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
sprite = pygame.image.load("Graphics/area/default_area.png")
snake = Snake()
current_area = AREAS[randint(0, len(AREAS) - 1)]
new_item = ITEMS[randint(0, len(ITEMS) - 1)]
sc = pygame.display.set_mode([snake.RES, snake.RES])


def scene_RPG():
    global current_area
    global snake
    global new_item
    sc = pygame.display.set_mode([snake.RES, snake.RES])
    current_area.new_item([])
    new_item.on_board = True
    apple.new_item(list(list(x[0]) for x in mountains.rocks))
    snake.reset()
    snake.alive = True
    while snake.alive:
        sc.fill(pygame.Color('black'))
        for h in range(0, 1040, snake.SIZE):
            for w in range(0, 1040, snake.SIZE):
                sc.blit(sprite, (w, h, snake.SIZE, snake.SIZE))
        current_area.render_img()
        # render some shit
        mountains.render()
        apple.render()
        stone_heart.run_from(snake, mountains)
        stone_heart.render()
        new_item.render()
        snake.render()
        render_lifes = font_score.render(f'LIFES: {snake.lifes} / {snake.maxlifes}', 1, pygame.Color('darkred'))
        render_score = font_score.render(f'MONEY: {snake.SCORE}$', 1, pygame.Color('darkred'))
        render_coeficient = font_score.render(f'Coefficient: X{snake.coefficient}', 1, pygame.Color('darkred'))
        sc.blit(render_lifes, (5, 5))
        sc.blit(render_score, (5, 35))
        sc.blit(render_coeficient, (5, 65))
        # snake movement
        snake.move()

        #
        if not gode_mode:
            mountains.in_rocks(snake)
            snake.game_over()
        #

        stone_heart.spawn(mountains)

        # spawn trash
        ran = randint(0, 10)
        if not ran and not new_item.on_board:
            new_item = ITEMS[randint(0, len(ITEMS) - 1)]
            new_item.new_item(list(list(x[0]) for x in mountains.rocks))

        # rendering
        pygame.display.flip()
        clock.tick(snake.fps)

        # eating apple
        if not snake.eat(apple, mountains):
            # in area
            current_area.check_in_area(snake)

        snake.eat(new_item, mountains)
        snake.eat(stone_heart, mountains)

        # escape the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and snake.direction != Vector2(0, 0):
                    scene_SHOP(snake)
                if snake.control(event):
                    break
        print(type(snake))
    snake.write_down_score()


def change_snake(i):
    global snake
    print(type(snake))
    score = snake.SCORE
    lifes = snake.lifes
    maxlifes = snake.maxlifes
    coeficient = snake.coefficient
    snake = SNAKES[i]
    snake.SCORE = score
    snake.lifes = lifes
    snake.maxlifes = maxlifes
    snake.coefficient = coeficient
    snake.reset()
    print(type(snake))


def buy_snake():
    showcase = Menu()
    showcase.append_option(SNAKES[5].__class__.__name__ + '      -50$', lambda: pay(20, lambda: change_snake(5)))
    showcase.append_option(SNAKES[2].__class__.__name__ + '  -50$', lambda: pay(50, lambda: change_snake(2)))
    showcase.append_option(SNAKES[3].__class__.__name__ + '      -100$', lambda: pay(100, lambda: change_snake(3)))
    showcase.append_option(SNAKES[1].__class__.__name__ + '          -150$', lambda: pay(150, lambda: change_snake(1)))
    showcase.append_option(SNAKES[4].__class__.__name__ + '          -200$', lambda: pay(200, lambda: change_snake(4)))

    shop_alive(showcase)


def pay(num, func):
    global snake
    if gode_mode:
        func()
    elif snake.SCORE >= num:
        snake.SCORE -= num
        func()


def upgrade_snake(snake):
    showcase = Menu()
    # showcase.append_option('Increase lenght', lambda: snake.changing_lenght(1))
    showcase.append_option('Decrease lenght       -3$', lambda: pay(3, lambda: snake.changing_lenght(-1)))
    showcase.append_option('Increase speed        -1$', lambda: pay(1, lambda: snake.changing_speed(1)))
    # showcase.append_option('Decrease speed', lambda: snake.changing_speed(-1))
    showcase.append_option('Increase coefficient -20$', lambda: pay(20, lambda: changing_coefficient(1)))
    showcase.append_option('Increase maxlifes    -10$', lambda: pay(10, lambda: snake.changing_maxlifes(1)))

    shop_alive(showcase)


def changing_coefficient(num):
    global snake
    snake.coefficient += 1


def change_area(i):
    global current_area
   # print(type(current_area))
    current_area = AREAS[i]
    current_area.new_item([])
    print(type(current_area))


def buy_area():
    showcase = Menu()
    showcase.append_option(AREAS[0].__class__.__name__ + '          -50$', lambda: pay(50, lambda: change_area(0)))
    showcase.append_option(AREAS[1].__class__.__name__ + '            -50$', lambda: pay(50, lambda: change_area(1)))
    showcase.append_option(AREAS[2].__class__.__name__ + '           -250 $', lambda: pay(250, lambda: change_area(2)))
    showcase.append_option('HolyWaterArea  -100$', lambda: pay(100, lambda: change_area(3)))

    shop_alive(showcase)


def sell_lenght():
    global snake
    snake.changing_lenght(5)
    # snake.SCORE += 2


def sell_coeficient():
    global snake
    if snake.coefficient == 1:
        return
    snake.coefficient -= 1
    # snake.SCORE += 100


def sell_speed():
    global snake
    if snake.fps == 1:
        return
    snake.fps -= 1
    # snake.SCORE += 1


def sell_lifes():
    global snake
    if snake.lifes == 1:
        return
    snake.lifes -= 1
    # snake.SCORE += 25


def sell_maxlifes():
    global snake
    if snake.maxlifes == 1:
        return
    snake.maxlifes -= 1
    # snake.SCORE += 75


def sell_something(snake):
    showcase = Menu()
    showcase.append_option('sell snake                             +75$',
                           lambda: pay(-75, lambda: change_snake(0)) if type(snake) != Snake else ...)
    showcase.append_option('Increase lenght for money  +10$', lambda: pay(-10, lambda: sell_lenght()))
    showcase.append_option('sell coeficient                       +15$',
                           lambda: pay(-15, lambda: sell_coeficient()) if snake.coefficient != 1 else ...)
    showcase.append_option('sell speed                               +1$',
                           lambda: pay(-1, lambda: sell_speed()) if snake.fps != 1 else ...)
    showcase.append_option('sell lifes                                +10$',
                           lambda: pay(-10, lambda: sell_lifes) if snake.lifes != 1 else ...)
    showcase.append_option('sell maxlifes                         +20$',
                           lambda: pay(-20, lambda: sell_maxlifes()) if snake.maxlifes != 1 else ...)

    shop_alive(showcase)


def pay_to_win(snake):
    sc.fill(pygame.Color('black'))
    render_score = font_score.render('YOU WIN', 1, pygame.Color('orange'))
    sc.blit(render_score, (snake.RES // 2 - 50, snake.RES // 2))
    pygame.display.flip()
    sleep(5)


ITEMS = [Speeder(), Slower(), BusterPoints(), Screamer(), Freezer(), Longer(), Jewish()]


def spawn_item(i):
    global new_item
    new_item = ITEMS[i]
    new_item.new_item(list(list(x[0]) for x in mountains.rocks))
    print(ITEMS[i].__class__.__name__)


def spawn_items():
    showcase = Menu()
    showcase.append_option('Spawn Speeder', lambda: spawn_item(0))
    showcase.append_option('Spawn Slower', lambda: spawn_item(1))
    showcase.append_option('Spawn BusterPoints', lambda: spawn_item(2))
    showcase.append_option('Spawn Screamer', lambda: spawn_item(3))
    showcase.append_option('Spawn Freezer', lambda: spawn_item(4))
    showcase.append_option('Spawn Longer', lambda: spawn_item(5))
    showcase.append_option('Spawn Jewish', lambda: spawn_item(6))
    showcase.append_option('Spawn StoneHeart', lambda: stone_heart.new_item(list(list(x[0]) for x in mountains.rocks)))

    shop_alive(showcase)


def changing_gode_mode():
    global gode_mode
    if gode_mode:
        gode_mode = False
    else:
        gode_mode = True


def scene_SHOP(snake):
    global gode_mode
    shop = Menu()
    shop.append_option('Buy new snake', lambda: buy_snake())
    shop.append_option("Upgrade ur snake", lambda: upgrade_snake(snake))
    shop.append_option("Change Area", lambda: buy_area())
    shop.append_option("Sell something", lambda: sell_something(snake))
    shop.append_option("Pay to Win  -1000$", lambda: pay(10000, lambda: pay_to_win(snake)))
    shop.append_option("", lambda: print('ты че ?'))
    shop.append_option("Gode mode", lambda: changing_gode_mode())
    if gode_mode:
        shop.append_option("Spawn Items", lambda: spawn_items())
    shop.append_option("", lambda: print('чеееел...'))
    shop.append_option("Battle with Boss", lambda: choose_boss(snake, current_area, gode_mode))

    shop_alive(shop)


def choose_boss(snake, current_area, god_mode):
    showcase = Menu()
    showcase.append_option('EyeBall', lambda: scene_BATTLE(snake, current_area, 0, god_mode))
    showcase.append_option('Ghost', lambda: scene_BATTLE(snake, current_area, 1, gode_mode))
    showcase.append_option('BigWorm', lambda: scene_BATTLE(snake, current_area, 2, god_mode))
    showcase.append_option('Pumpking', lambda: scene_BATTLE(snake, current_area, 3, god_mode))
    showcase.append_option('ManEater', lambda: scene_BATTLE(snake, current_area, 4, god_mode))

    shop_alive(showcase)


def shop_alive(shop):
    r = True
    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                # switch_scene(scene_MENU())
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    shop.switch(-1)
                elif event.key == K_s:
                    shop.switch(1)
                elif event.key == K_SPACE:
                    shop.select()
                elif event.key == K_ESCAPE:
                    return
        sc.fill((0, 0, 0))

        shop.draw(sc, 100, 100, 75)

        display.flip()
