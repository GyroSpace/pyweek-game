import pygame
from game_functions import *
class Character(pygame.sprite.Sprite):
	def __init__(self):
		super(Character, self).__init__()
		# adding all the images
		self.images = []
		self.size = (200,200)
		self.index = 0

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]

	def clear(self):
		self.images = []

	def run(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-03.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-04.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-05.png"), self.size))
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def idle(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-idle-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-idle-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-idle-02.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def idle2(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-idle-2-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-idle-2-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-idle-2-02.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def attack1(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack1-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack1-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack1-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack1-03.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack1-04.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def attack2(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack2-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack2-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack2-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack2-03.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack2-04.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack2-05.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def attack3(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack3-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack3-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack3-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack3-03.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack3-04.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-attack3-05.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def climb(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-clmb-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-clmb-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-clmb-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-clmb-03.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-clmb-04.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def grab(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-grb-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-grb-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-grb-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-grb-03.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def mid_jump(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-jmp-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-jmp-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crnr-jmp-02.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def crouch(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crouch-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crouch-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crouch-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-crouch-03.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def fall(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-fall-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-fall-01.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def die(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-die-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-die-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-die-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-die-03.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-die-04.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-die-05.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-die-06.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def hurt(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-hurt-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-hurt-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-hurt-02.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def jump(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-jump-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-jump-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-jump-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-jump-03.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def slide(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-slide-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-slide-01.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def summersault(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-smrslt-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-smrslt-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-smrslt-02.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-smrslt-03.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()

	def stand(self):
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-stand-00.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-stand-01.png"), self.size))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-stand-02.png"), self.size))
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

		self.update()
