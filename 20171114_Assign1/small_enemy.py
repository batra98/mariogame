import config
import person
from random import randrange,randint
class enemy_1(person.Person):
	def __init__(self,x,y):	
		person.Person.__init__(self,x,y)
		self.char="e"
		self.x_original=x
		self.y_original=y
		self.follow_coefficient=-1
		self.velocity=randint(10999,11099)		

	def get_x(self):
		if len(config.enemy_count) > 0:
			return self.x
		else:
			return -100	


	def get_y(self):
		if len(config.enemy_count) > 0:
			return self.y
		else:
			return -100	

	def follow(self,x_player,x):
		if x_player < x:
			return -1
		else:
			return 1	

	def detect_collision(self,map_mario):
		if map_mario[self.get_x()][self.get_y()-1] == "#" or map_mario[self.get_x()][self.get_y()+1] == "#":
			self.follow_coefficient=self.follow_coefficient*(-1)

	def undo(self,map_mario,y,x):
		map_mario[x][y]=" "				