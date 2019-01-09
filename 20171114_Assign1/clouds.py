class Clouds:
	def __init__(self,map_mario):
		self.cloud = ["()()()","..()()()()...."]
		self.map_mario=map_mario
	
	def draw(self,y,x):
		for j in range(0,len(self.cloud[0])):			
			try:
				self.map_mario[y][x+j]=self.cloud[0][j]
			except Exception:
				pass	
		for j in range(0,len(self.cloud[1])):			
			try:
				self.map_mario[y+1][x-3+j]=self.cloud[1][j]
			except Exception:
				pass	

	def update(self,n,y,x):
		self.draw(y,x)
