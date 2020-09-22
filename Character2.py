import pygame
class Character2(pygame.sprite.Sprite):
	def __init__(self):
		super(Character2, self).__init__()
		self.images = []

		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_0.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_1.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_2.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_3.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_4.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_5.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_6.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_7.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_8.png"), (250, 200)))
		self.images.append(pygame.transform.scale(pygame.image.load("Character2/Sprites/HeroKnight/Run/HeroKnight_Run_9.png"), (250, 200)))
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(100,100,200,100)

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]