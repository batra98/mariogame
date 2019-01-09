import config
class Coins:
	def __init__(self):
		self.coin_position=[]

	def set_position(self,k,a,g,index):
		self.coin_position.append([k,a+g+index])

	def show(self,map_mario,x,y):
		map_mario[x][y]="*"

	def disappear_coin(self,map_mario,x,y,score):
		map_mario[x][y]=" "
		score=score+1
		return score

	def change_brick(self,map_mario,x,y,char_changed):
		map_mario[x][y]="&"		