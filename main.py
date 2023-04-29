# Создай собственный Шутер!
from random import randint
from pygame import *

window = display.set_mode((800, 600))
display.set_caption('Wolter,wolter')
background = transform.scale(image.load('galaxy.jpg'), (800, 600))
hero = transform.scale(image.load('rocket.png'), (900, 900))
cyborg = transform.scale(image.load('ufo.png'), (100, 100))
aster = transform.scale(image.load('asteroid.png'), (100, 100))
font.init()
font2 = font.Font(None, 36)

x1 = 100
x2 = 400
y1 = 100
y2 = 200

clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 10:
            self.rect.x -= 8
        if key_pressed[K_RIGHT] and self.rect.x < 720:
            self.rect.x += 8

    def fire(self):

        self.sprite_centerx = self.rect.centerx
        self.Sprite_top = self.rect.top
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, -15)
        bullets.add(bullet)


lost = 0
win_counter = 0


class Enemy(GameSprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__(player_image, x, y, speed)
        self.image = transform.scale(image.load(player_image), (100, 80))

    def update(self):
        self.rect.y += randint(1, 3)
        global lost
        if self.rect.y > 700:
            self.rect.x = randint(50, 600)
            self.rect.y = 0
            lost += 1


class Aster(GameSprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__(player_image, x, y, speed)
        self.image = transform.scale(image.load(asteroid.png), (100, 80))

    def update(self):
        self.rect.y += randint(1, 3)
        if self.rect.y > 700:
            self.rect.x = randint(50, 600)
            self.rect.y = 0


bullets = sprite.Group()


class Bullet(GameSprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__(player_image, x, y, speed)
        self.image = transform.scale(image.load(player_image), (10, 10))

    def update(self):
        self.rect.y -= 5
        if self.rect.y <= 0:
            self.kill()


monsters = sprite.Group()
monsters.add(Enemy('ufo.png', randint(50, 850), 0, randint(1, 2)))
monsters.add(Enemy('ufo.png', randint(50, 850), 0, randint(1, 2)))
monsters.add(Enemy('ufo.png', randint(50, 850), 0, randint(1, 2)))
monsters.add(Enemy('ufo.png', randint(50, 850), 0, randint(1, 2)))
monsters.add(Enemy('ufo.png', randint(50, 850), 0, randint(1, 2)))

game = True
p1 = Player('rocket.png', 500, 500, 30)

while game:

    window.blit(background, (0, 0))
    text_lose = font2.render("Пропущено:" + str(lost), 1, (255, 255, 255))
    p1.reset()
    p1.update()
    monsters.draw(window)
    monsters.update()
    bullets.update()
    bullets.draw(window)
    collision = sprite.groupcollide(monsters, bullets, True, True)
    if collision:
        win_counter += 1
        monsters.add(Enemy('ufo.png', randint(50, 850), 0, randint(1, 2)))

    keys_pressed = key.get_pressed()
    if keys_pressed[K_SPACE]:
        p1.fire()

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()

