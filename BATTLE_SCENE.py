from RPG_SCENE import *
from BOSSES import *


def scene_BATTLE(snake, current_area, num_boss, god_mode):
    ITEMS = [Speeder(), Slower(), BusterPoints(), Screamer(), Freezer(), Longer(), Jewish()]

    mountains = RockOnBosssArea()

    stone_heart = LifeHeart()

    apple = Apple()
    apple.new_item(list(list(x[0]) for x in mountains.rocks))

    snake = snake

    new_item = ITEMS[randint(0, len(ITEMS) - 1)]
    new_item.on_board = True

    sc = pygame.display.set_mode([snake.RES, snake.RES])
    clock = pygame.time.Clock()
    font_score = pygame.font.SysFont('Arial', 26, bold=True)
    sprite = pygame.image.load("Graphics/area/boss_area.png")

    BOSSES = [Eyeball(), Ghost(), BigWorm(), Pumpking(), ManEater()]
    boss = BOSSES[num_boss]
    snake.reset()
    bullets = []

    while snake.alive:
        for bullet in bullets:
            if snake.RES > bullet.coordinate.x > 0 and 0 < bullet.coordinate.y < snake.RES:
                bullet.coordinate.x += bullet.vel[0]
                bullet.coordinate.y += bullet.vel[1]
            else:
                bullets.pop(bullets.index(bullet))

        sc.fill(pygame.Color((139, 69, 19)))
        for h in range(0, 1040, snake.SIZE):
            for w in range(0, 1040, snake.SIZE):
                sc.blit(sprite, (w, h, snake.SIZE, snake.SIZE))

        current_area.render_img()
        # render some shit
        mountains.render()
        for bullet in bullets:
            bullet.draw(sc)
        apple.render()
        stone_heart.run_from(snake, mountains)
        stone_heart.render()
        new_item.render()
        snake.render()
        render_lifes = font_score.render(f'LIFES: {snake.lifes} / {snake.maxlifes}', 1, pygame.Color('orange'))
        sc.blit(render_lifes, (5, 5))
        # snake movement
        snake.move()

        #
        if not god_mode:
            mountains.in_rocks(snake)
            snake.game_over()
            # snake_body = list(list(y * snake.SIZE for y in x) for x in snake.body)
            snake_body = list(list(x) for x in snake.body)
            bullets_coords = list(list(s for s in list(x for x in bullet.coordinate)) for bullet in bullets)
            if any(x in bullets_coords or x == boss.coordinate for x in snake_body):
                if snake.lifes == 1:
                    snake.alive = False
                else:
                    snake.lifes -= 1
                    snake.reset()

        # eating apple
        if not snake.eat(apple, mountains):
            # in area
            current_area.check_in_area(snake)
        else:
            boss.lifes -= 1
            if boss.lifes == 0:
                sc.fill(pygame.Color('black'))
                render_score = font_score.render('YOU WIN', 1, pygame.Color('orange'))
                sc.blit(render_score, (snake.RES // 2 - 50, snake.RES // 2))
                pygame.display.flip()
                sleep(5)
                snake.alive = False

        snake.eat(new_item, mountains)
        snake.eat(stone_heart, mountains)

        stone_heart.spawn(mountains)

        # spawn trash

        ran = randint(0, 10)
        if not ran and not new_item.on_board:
            new_item = ITEMS[randint(0, len(ITEMS) - 1)]
            # list(list(y for y in s[0]) for s in mountains.rocks)
            new_item.new_item(list(list(x[0]) for x in mountains.rocks))

        boss.move_from(snake)
        boss.render(bullets)

        # rendering
        pygame.display.flip()
        clock.tick(snake.fps)

        # escape the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                snake.alive = exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                snake.control(event)
