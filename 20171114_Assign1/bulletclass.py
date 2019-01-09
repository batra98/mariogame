class Bullet():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.char="-"
		self.x_original=x
		self.y_original=y

	def update_pos(self,x_new,y_new,map_mario):
		if map_mario[x_new][y_new] == "@" or map_mario[x_new][y_new+1] == "e" or map_mario[x_new][y_new] == "$":
			map_mario[x_new][y_new]=" "		
		else:
			map_mario[x_new][y_new]=self.char

		self.x=x_new
		self.y=y_new

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y	