import pygame
from classes import *
from Character2 import *

def game():
    pygame.init()

    screen = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("Pyweek Game")

    x = 50
    y = 50
    width = 40
    height = 60
    vel = 5

    isJump = False
    jumpCount = 10

    run = True
	Char = Character()
	Char.stand()
	Char.idle()
	Char.crouch()
	Char.idle2()
	Char.jump()
	Char.attack1()
	Char.attack2()
	Char.attack3()
	Char.grab()
	Char.run()
	Char.slide()
	Char.run()
	Char.climb()
	Char.run()
	Char.summersault()
	Char.idle2()
	Char.jump()
	Char.mid_jump()
	Char.crouch()
	Char.hurt()
	Char.die()
    Group = pygame.sprite.Group(Char)
    clock = pygame.time.Clock()

    # Character 2
    Char2 = Character2()
    Group2 = pygame.sprite.Group(Char2)
    while run:
        pygame.time.delay(100)
	
	Group = pygame.sprite.Group(Char)
	clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel

        if keys[pygame.K_RIGHT] and x < 500 - width:
            x += vel
        if not(isJump):
            if keys[pygame.K_UP] and y > vel:
                y -= vel

            if keys[pygame.K_DOWN] and y < 500 - height - vel:
                y += vel
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                JumpCount = 10

        Group.update()
        Group2.update()
        screen.fill((0, 0, 0))
        Group.draw(screen)
        Group2.draw(screen)
        pygame.display.update()
        clock.tick(10)

    pygame.quit()
