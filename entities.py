import pygame
import random

class Entity:
	def __init__(self, sprite, position):
		self.sprite = sprite
		self.position = pygame.Vector2(position)

class Enemy(Entity):
	def __init__(self, sprite, position):
		super().__init__(sprite, position)
		self.bullets = []
		
	def update(self):
		self.position.x += 10
		if self.position.x > 800 - self.sprite.get_width():
			self.position.x = self.sprite.get_width()
			self.position.y += 10

		if random.random() < 0.01:
			bp = pygame.Vector2(self.position.x + self.sprite.get_width() / 2, self.position.y)
			self.bullets.append(Bullet(bp,-5))
			


class Player(Entity):
	def __init__(self, sprite, position):
		super().__init__(sprite, position)
		self.bullets = []

	def move_left(self):
		self.position.x -= 5  # Adjust the value to change the speed of movement
		if self.position.x < 0:
			self.position.x = 0

	def move_right(self):
		self.position.x += 5  # Adjust the value to change the speed of movement
		if self.position.x > 800 - self.sprite.get_width():
			self.position.x = 800 - self.sprite.get_width()

	def shoot(self):
		bp = pygame.Vector2(self.position.x + self.sprite.get_width() / 2, self.position.y)
		bullet = Bullet(bp)  # Assuming the Bullet class takes the starting position as a parameter
		self.bullets.append(bullet)

class Bullet(Entity):
	def __init__(self, position, speed=3):
		self.speed = speed
		sprite = pygame.Surface((3, 10))
		sprite.fill((255, 255, 255))
		super().__init__(sprite, position)

	def update(self):
		self.position.y -= self.speed  # Adjust the value to change the speed of the bullet
		if self.position.y < 0:
			return False
		return True

class Barrier(Entity):
	def __init__(self, position):
		sprite = pygame.Surface((50, 25))
		sprite.fill((0, 255, 0))
		super().__init__(sprite, position)