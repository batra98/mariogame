class Flag():
	def __init__(self,map_mario):
		self.map_mario=map_mario
		self.flag=["  ++-----","  ++-----","  ++-----","  ++     ","  ++     ","  ++     ","  ++     ","  ++     ","  ++     ","  ++     ","++++++   "]

	def draw(self,i,y,x):
		s=list(self.flag[i])
		for j in range(4,9):
			s[j]=" "
		for j in range(0,9):
			self.map_mario[y+i][x+j]=s[j]	
		
			
		s=list(self.flag[i+3])
		for j in range(4,9):
			s[j]="-"
		for j in range(0,9):
			self.map_mario[y+i+3][x+j]=s[j]

	def draw_2(self,y,x):
		for i in range(0,len(self.flag)):
			s=list(self.flag[i])
			for j in range(0,9):
				self.map_mario[y+i][x+j]=s[j]



		
