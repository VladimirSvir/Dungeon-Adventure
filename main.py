import pygame
import sys
import os
from ctypes  import *
from sprite_classes import Left_turn_wall_up, Left_turn_wall_down, Front_wall_up, Front_wall_down, Right_turn_wall_up
from sprite_classes import Right_turn_wall_down, Wall_on_the_left, Wall_on_the_right, Down_right_turn_wall
from sprite_classes import Down_left_turn_wall, Back_wall, Floor, Wall_turn_right_down_1, Wall_turn_right_down_2
from sprite_classes import Wall_turn_left_down_1, Wall_turn_left_down_2, Inner_wall_left_up, Inner_wall_left_down
from sprite_classes import Inner_wall_right_up, Inner_wall_right_down, Down_Inner_wall_left_1, Down_Inner_wall_left_2
from sprite_classes import Down_Inner_wall_right_1, Down_Inner_wall_right_2, Post_up, Post_down
from Camera import Camera


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, ' '), level_map))



def calculate_vectors(x, y):
    len_tru_vec = (100 ** 2 * 2) ** 0.5
    len_vec = (x ** 2 + y ** 2) ** 0.5 * 10
    col_tru_vec = len_vec / len_tru_vec
    return [x / col_tru_vec, y / col_tru_vec]


def render_text(text, font, color, surface, x, y):
    text = font.render(text, 1, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    surface.blit(text, text_rect)

def draw_button(screen, color1, color2, button, border):
    pygame.draw.rect(screen, pygame.Color(color1), button)
    pygame.draw.rect(screen, pygame.Color(color2), button, border)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image("hero/Hero.png"), (36, 64))
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.rect.x, self.rect.y = pos

    def update(self, direction, account, sprites_wall):
        # hits = pygame.sprite.spritecollide(self, sprites_wall, False)
        # if not hits:
        if direction == 'up':
            self.image = pygame.transform.scale(load_image("hero/Hero_ass.png"), (36, 64))
            self.rect.y -= 8
        elif direction == 'down':
            self.image = pygame.transform.scale(load_image("hero/Hero.png"), (36, 64))
            self.rect.y += 8
        elif direction == 'left':
            self.image = pygame.transform.scale(load_image("hero/Hero_left.png"), (36, 64))
            self.rect.x -= 8
        elif direction == 'right':
            self.image = pygame.transform.scale(load_image("hero/Hero_right.png"), (36, 64))
            self.rect.x += 8


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dir, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('bullet.png'), (8, 8))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = dir

    def update(self, sprites_wall):
        hits = pygame.sprite.spritecollide(self, sprites_wall, False)
        if not hits:
            self.rect.x += self.dir[0]
            self.rect.y += self.dir[1]
        else:
            self.kill()


def render(level):
    x, y = 0, 0
    for cow in level:
        for col in cow:
            if col == '0':
                pl = Floor(x, y, wall_sprites)
            elif col == '1':
                pl = Right_turn_wall_up(x, y, wall_sprites)
                wall.append(pl)
            elif col == '2':
                pl = Front_wall_up(x, y, wall_sprites)
                wall.append(pl)
            elif col == '3':
                pl = Left_turn_wall_up(x, y, wall_sprites)
                wall.append(pl)
            elif col == '4':
                pl = Right_turn_wall_down(x, y, wall_sprites)
                wall.append(pl)
            elif col == '5':
                pl = Front_wall_down(x, y, wall_sprites)
                wall.append(pl)
            elif col == '6':
                pl = Left_turn_wall_down(x, y, wall_sprites)
                wall.append(pl)
            elif col == '7':
                pl = Wall_on_the_left(x, y, wall_sprites)
                wall.append(pl)
            elif col == '8':
                pl = Wall_on_the_right(x, y, wall_sprites)
                wall.append(pl)
            elif col == '9':
                pl = Down_right_turn_wall(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'A':
                pl = Back_wall(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'B':
                pl = Down_left_turn_wall(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'C':
                pl = Inner_wall_left_up(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'D':
                pl = Inner_wall_right_up(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'E':
                pl = Inner_wall_left_down(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'F':
                pl = Inner_wall_right_down(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'G':
                pl = Post_down(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'H':
                pl = Post_up(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'I':
                pl = Down_Inner_wall_left_1(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'J':
                pl = Down_Inner_wall_right_1(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'K':
                pl = Down_Inner_wall_left_2(x, y, wall_sprites)
                wall.append(pl)
            elif col == 'L':
                pl = Down_Inner_wall_right_2(x, y, wall_sprites)
                wall.append(pl)
            x += 64
        y += 64
        x = 0

wall = []
Bullets = []

def menu():
    cursor_img = pygame.transform.scale(load_image('scope.png'), (22, 22))
    pygame.mouse.set_visible(False)
    cursor_img_rect = cursor_img.get_rect()
    title_font = pygame.font.Font("dung_font.ttf", 100)
    font = pygame.font.Font("dung_font.ttf", 50)
    click = False
    while True:
        screen.fill((47, 40, 58))

        button_start = pygame.Rect(width // 2 - 140, height // 3 + 30, 280, 65)
        button_options = pygame.Rect(width // 2 - 140, height // 3 * (1 + 1 / 2) + 30, 280, 65)
        button_exit = pygame.Rect(width // 2 - 140, height // 3 * 2 + 30, 280, 65)

        draw_button(screen, "#b25d4d", "#3f3656", button_start, 10)
        draw_button(screen, "#b25d4d", "#3f3656", button_options, 10)
        draw_button(screen, "#b25d4d", "#3f3656", button_exit, 10)

        render_text("Dunger Adventure", title_font, pygame.Color("#c2c1bf"), screen, width // 2, height // 4)
        render_text("Start Game", font, pygame.Color("#c2c1bf"), screen, width // 2, height // 3 + 30 * 2)
        render_text("howw play", font, pygame.Color("#c2c1bf"), screen, width // 2, (height // 3 * (1 + 1 / 2) + 30) * 1.1)
        render_text("Exit", font, pygame.Color("#c2c1bf"), screen, width // 2, (height // 3 * 2 + 30) * 1.075)
        cursor_img_rect.center = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_img_rect)
        x, y = pygame.mouse.get_pos()

        # Проверяем нажатие на кнопки
        if button_start.collidepoint((x, y)):
            if click:
                game()
                click = False

        if button_options.collidepoint((x, y)):
            if click:
                how_to_play()
                click = False

        if button_exit.collidepoint((x, y)):
            if click:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()


def pause():
    cursor_img = pygame.transform.scale(load_image('scope.png'), (22, 22))
    pygame.mouse.set_visible(False)
    cursor_img_rect = cursor_img.get_rect()
    title_font = pygame.font.Font("dung_font.ttf", 100)
    font = pygame.font.Font("dung_font.ttf", 50)
    button_exit_on_table_font = pygame.font.Font("dung_font.ttf", 20)
    click = False
    pause = True
    while pause:
        screen.fill((47, 40, 58))
        button_continue = pygame.Rect(width // 2 - 140, height // 3 + 30, 280, 65)
        button_exit = pygame.Rect(width // 2 - 140, height // 3 * (1 + 1 / 2) + 30, 280, 65)
        button_exit_on_table = pygame.Rect(width // 2 - 140, height // 3 * 2 + 30, 280, 65)

        draw_button(screen, "#b25d4d", "#3f3656", button_continue, 10)
        draw_button(screen, "#b25d4d", "#3f3656", button_exit_on_table, 10)
        draw_button(screen, "#b25d4d", "#3f3656", button_exit, 10)

        render_text("PAUSE", title_font, pygame.Color("#c2c1bf"), screen, width // 2, height // 4)
        render_text("continue", font, pygame.Color("#c2c1bf"), screen, width // 2, height // 3 + 30 * 2)
        render_text("exit", font, pygame.Color("#c2c1bf"), screen, width // 2,
                    (height // 3 * (1 + 1 / 2) + 30) * 1.1)
        render_text("exit to desktop", button_exit_on_table_font, pygame.Color("#c2c1bf"), screen, width // 2, (height // 3 * 2 + 30) * 1.075)


        x, y = pygame.mouse.get_pos()

        # Проверяем нажатие на кнопки
        if button_continue.collidepoint((x, y)):
            if click:
                pause = False
                click = False

        if button_exit.collidepoint((x, y)):
            if click:
                menu()

        if button_exit_on_table.collidepoint((x, y)):
            if click:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
        cursor_img_rect.center = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_img_rect)
        pygame.display.flip()


def how_to_play():
    title_font = pygame.font.Font("dung_font.ttf", 80)
    font = pygame.font.Font("dung_font.ttf", 30)
    cursor_img = pygame.transform.scale(load_image('scope.png'), (22, 22))
    pygame.mouse.set_visible(False)
    cursor_img_rect = cursor_img.get_rect()
    how = True
    click = False
    while how:
        screen.fill((47, 40, 58))
        button_ok = pygame.Rect(width * 0.80, height * 0.75, 120, 65)
        draw_button(screen, "#b25d4d", "#3f3656", button_ok, 10)
        render_text("ok", title_font, pygame.Color("#c2c1bf"), screen, width * 0.85, height * 0.80)
        render_text("HoW tO PlAy ThIs GAME?", title_font, pygame.Color("#c2c1bf"), screen, width // 2 , height // 6)
        render_text("the control is WASD", font, pygame.Color("#c2c1bf"), screen, width // 2, height // 3)
        render_text("shooting is the left mouse button", font, pygame.Color("#c2c1bf"), screen, width // 2, height // 3 + 60)
        render_text("have a nice game!!!", font, pygame.Color("#c2c1bf"), screen, width // 2,
                    height // 3 + 90)
        x, y = pygame.mouse.get_pos()
        if button_ok.collidepoint((x, y)):
            if click:
                how = False
                click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        cursor_img_rect.center = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_img_rect)
        pygame.display.flip()

def game():
    count = 0
    pl = Player((width * 1.7, height // 2), sprites_of_hero)
    moving_up = moving_down = moving_right = moving_left = False
    render(load_level('map'))
    camera = Camera()
    cursor_img = pygame.transform.scale(load_image('scope.png'), (22, 22))
    pygame.mouse.set_visible(False)
    cursor_img_rect = cursor_img.get_rect()
    while True:
        screen.fill((47, 40, 58))
        count += 1

        if moving_up:
            sprites_of_hero.update('up', count, wall)
        if moving_down:
            sprites_of_hero.update('down', count, wall)
        if moving_right:
            sprites_of_hero.update('right', count, wall)
        if moving_left:
            sprites_of_hero.update('left', count, wall)

        wall_sprites.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bult = Bullet(pl.rect.x + 31, pl.rect.y + 32, calculate_vectors(event.pos[0] - pl.rect.x - 31,
                                                                                    event.pos[1] - pl.rect.y - 32),
                                  Bullet_sprites)
                    Bullets.append(bult)


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    moving_right = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    moving_left = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    moving_up = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    moving_down = True
                elif event.key == pygame.K_ESCAPE:
                    pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    moving_right = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    moving_left = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    moving_up = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    moving_down = False

        Bullet_sprites.update(wall)
        Bullet_sprites.draw(screen)

        camera.update(pl)
        camera.apply(pl)
        for sprite in wall_sprites:
            camera.apply(sprite)

        for sprite in Bullet_sprites:
            camera.apply(sprite)


        sprites_of_hero.draw(screen)

        cursor_img_rect.center = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_img_rect)


        pygame.display.flip()
        clock.tick(fps)
        if count == 30:
            count = 0


if __name__ == '__main__':
    pygame.init()
    size = width, height = int(windll.user32.GetSystemMetrics(0) / 1.321),\
                           int(windll.user32.GetSystemMetrics(1) / 1.321)
    screen = pygame.display.set_mode(size)
    clock, fps = pygame.time.Clock(), 30
    sprites_of_hero = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    Bullet_sprites = pygame.sprite.Group()
    menu()