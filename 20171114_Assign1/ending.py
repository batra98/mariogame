class End():
	def __init__(self,map_mario):
		self.map_mario=map_mario
		self.stair_right=["##       ","####     ","####     ","######   ","######   ","#########","#########"]
		self.stair_left=["       ##","     ####","     ####","   ######","   ######","#########","#########"]
		self.castle=[]

	def draw_left(self,x,y,height,width):
		for i in range(0,9):
			for j in range(0,len(self.stair_left)):
				self.map_mario[y+j][x+i]=self.stair_left[j][i]

				

	def draw_right(self,x,y,height,width):
		for i in range(0,9):
			for j in range(0,len(self.stair_right)):
				self.map_mario[y+j][x+i]=self.stair_right[j][i]

						

