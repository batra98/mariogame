import person
class Mario(person.Person):
	def __init__(self,x,y):		
		person.Person.__init__(self,x,y)
		self.bullet="-"

	def update_pos(self,map_mario,x_new,y_new):
		previous=map_mario[x_new][y_new]
		map_mario[x_new][y_new]=self.char
		map_mario[self.x][self.y]=previous
		if previous == 'e' or previous == "#" or previous == "@" or previous == "$"or previous=="-":
			map_mario[self.x][self.y]=" "
		self.x=x_new
		self.y=y_new

	

	


