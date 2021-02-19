import pygame
import os

WIDTH = HEIGHT = 64


def load_image(name, color_keys=None):
    full_name = os.path.join(name)

    try:
        image = pygame.image.load(full_name)
        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    except pygame.error as message:
        print('не удалось загрузить', name)
        raise SystemExit(message)
    return image


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__( *group)
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill((145, 176, 154))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Left_turn_wall_up(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Left_turn_wall_up.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Left_turn_wall_down(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Left_turn_wall_down.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Front_wall_up(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Front_wall_up.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Front_wall_down(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Front_wall_down.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Right_turn_wall_up(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Right_turn_wall_up.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Right_turn_wall_down(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Right_turn_wall_down.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Wall_on_the_left(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Left_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Wall_on_the_right(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Right_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Down_right_turn_wall(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Down_Right_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Down_left_turn_wall(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Down_Left_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Back_wall(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Back_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Wall_turn_right_down_1(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Back_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Wall_turn_right_down_2(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Back_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Wall_turn_left_down_1(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Back_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Wall_turn_left_down_2(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Back_wall.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)

# ======================================================================================================================
# ======================================================================================================================


class Inner_wall_left_up(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Inner_wall_left_up.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Inner_wall_left_down(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Inner_wall_left_down.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Inner_wall_right_up(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Inner_wall_right_up.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Inner_wall_right_down(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Inner_wall_right_down.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Down_Inner_wall_left_1(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Down_Inner_wall_left_1.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Down_Inner_wall_left_2(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Down_Inner_wall_left_2.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Down_Inner_wall_right_1(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Down_Inner_wall_right_1.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Down_Inner_wall_right_2(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Down_Inner_wall_right_2.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Post_up(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Post_up.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)


class Post_down(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('data/wall/Post_down.png'), (WIDTH, HEIGHT))
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)
