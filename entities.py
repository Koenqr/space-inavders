class bullet():
	def __init__(self, x, y, angle=0, speed=1, damage=1):
		self.x = x
		self.y = y
		self.angle = angle
		self.speed = speed
		self.damage = damage
  
  
class invaders():
	def __init__(self, x, y, speed=1, damage=1):
		self.x = x
		self.y = y
		self.speed = speed
		self.damage = damage

class player():
	def __init__(self, x, y, speed=1, damage=1):
		self.x = x
		self.y = y
		self.speed = speed
		self.damage = damage


class boss():
	def __init__(self, x, y, speed=1, damage=1):
		self.x = x
		self.y = y
		self.speed = speed
		self.damage = damage