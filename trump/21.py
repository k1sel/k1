import pygame
import sys

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My game")

x = 50
y = 420
width = 60
height = 71
speed = 40
is_jump = False
jump_count = 10

left = False
right = False
anim_count = 0

walk_right = [
    pygame.image.load("pygame_right_1.png"),
    pygame.image.load("pygame_right_2.png"),
    pygame.image.load("pygame_right_3.png"),
    pygame.image.load("pygame_right_4.png"),
    pygame.image.load("pygame_right_5.png"),
    pygame.image.load("pygame_right_6.png"),
]
walk_left = [
    pygame.image.load("pygame_left_1.png"),
    pygame.image.load("pygame_left_2.png"),
    pygame.image.load("pygame_left_3.png"),
    pygame.image.load("pygame_left_4.png"),
    pygame.image.load("pygame_left_5.png"),
    pygame.image.load("pygame_left_6.png"),
]

background = pygame.image.load("pygame_bg.jpg")
player_stand = pygame.image.load("pygame_idle.png")
bullets = []

class Whizzbang:

    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing  # ( 1 or -1)
        self.speed = 8 * facing  # velocity (speed)

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)


def display_win():
    global anim_count
    win.fill((127, 181, 181))
    win.blit(background, (0, 0))

    # pygame.draw.rect(win, (250, 204, 209), (x, y, width, height))

    if anim_count >= 30:
        anim_count = 0
    if left:
        win.blit(walk_left[anim_count // 5], (x, y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    else:
        win.blit(player_stand, (x, y))


    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        if right:
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(
                Whizzbang(x=round((x + width // 2)), y=round((y + height // 2)), radius=8, colour=(0, 0, 0), facing=facing))

    if keys[pygame.K_LEFT] and x > 5:
        left = True
        right = False
        x -= speed

    elif keys[pygame.K_RIGHT] and x < 500 - width:
        right = True
        left = False
        x += speed
    else:
        right = False
        left = False
    if not is_jump:
        # if keys[pygame.K_UP] and y > 5:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < 500 - height:
        #     y += speed
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 2
            else:
                y -= (jump_count ** 2) / 2 if y >= 0 else y
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    display_win()