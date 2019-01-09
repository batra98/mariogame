class Person():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.char="m"

	def draw(self,map_mario):
		map_mario[self.x][self.y]=self.char

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y


	def update_pos(self,map_mario,x_new,y_new):		
		map_mario[x_new][y_new]=self.char
		map_mario[self.x][self.y]=" "
		self.x=x_new
		self.y=y_new			