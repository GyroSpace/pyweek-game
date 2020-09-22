import pygame
from game import *
class Character(pygame.sprite.Sprite):
	def __init__(self):
		super(Character, self).__init__()
		# adding all the images
		self.images = []


		self.images.append(pygame.image.load("Character/adventurer-run-00.png"))
		self.images.append(pygame.image.load("Character/adventurer-run-01.png"))
		self.images.append(pygame.image.load("Character/adventurer-run-02.png"))
		self.images.append(pygame.image.load("Character/adventurer-run-03.png"))
		self.images.append(pygame.image.load("Character/adventurer-run-04.png"))
		self.images.append(pygame.image.load("Character/adventurer-run-05.png"))
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(100,100,200,200)

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]