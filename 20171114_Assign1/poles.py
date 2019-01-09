class Poles:
	def __init__(self,map_mario):
		self.map_mario=map_mario
		self.poles=['###','###','###','###']

	def draw(self,x,y):
		for j in range(0,len(self.poles)):
			for i in range(0,len(self.poles[j])):
				self.map_mario[y-j][x+i]=self.poles[j][i]	