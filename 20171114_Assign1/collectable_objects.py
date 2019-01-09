class collectables():
	def __init__(self):		
		pass

	def update_pos(self,y_new,x_new,map_mario,y_old,x_old):
		map_mario[y_new][x_new]=self.char
		map_mario[y_old][x_old]=" "

	
	def get_x():
		return self.x

	def get_y():
		return self.y

	def draw(self,map_mario,y,x):
		map_mario[y][x]=self.char