import color
class start():
	def __init__(self,height,width):
		self.height=height
		self.width=width
		self.start_screen=[" ____       ___  ___  ___","|     |   ||   ||    |   |                            Instructions:","|____ |   ||___||___ |___|","     ||   ||    |    | \\                         1) Press E to start the Easy mode or H to start the Hard mode"," ____||___||    |___ |  \\                        2) Press R to restart the Game","                                                 3) Press Q to quit the Game","       ___  ___  ___  ___","|\\  /||   ||   |  |  |   |                            Controls:","| \\/ ||___||___|  |  |   |","|    ||   || \\    |  |   |                       1) Use WAD to move the player","|    ||   ||  \\  _|_ |___|                       2) Use F to shoot (can be used in super mode)",""]
		self.mario_start=[]

	def initialize(self):
		temp=[]
		temp_2=[]
		for i in range(0,self.height-1):
			for j in range(0,self.width):
				if i == 0:
					temp.append("*")
				elif i >= self.height-3:
					temp.append("#")	
				else:	
					temp.append(" ")
			
			self.mario_start.append(temp)
			temp=[]

		for i in range(0,self.width):
			temp_2.append("*")
		self.mario_start.append(temp_2)

	def draw(self):
		for g in range(0,self.height):
			print(color.getcolor("*"),end="")
			for h in range(0,self.width):
				print(color.getcolor(self.mario_start[g][h]),end="")
			print(color.getcolor("*"))

	def label(self):
		for i in range(0,11):
			for j in range(0,len(self.start_screen[i])):
				self.mario_start[int(self.height/4)+i][int(self.width/12)+j]=self.start_screen[i][j]
 
		