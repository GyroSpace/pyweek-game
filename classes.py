import pygame
from game import *
class Character(pygame.sprite.Sprite):
	def __init__(self):
		super(Character, self).__init__()
		# adding all the images
		self.images = []

		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-00.png"), (200, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-01.png"), (200, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-02.png"), (200, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-03.png"), (200, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-04.png"), (200, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character/adventurer-run-05.png"), (200, 200)))
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0,0,0,0)

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]