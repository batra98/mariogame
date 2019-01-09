import collectable_objects
class Cakes(collectable_objects.collectables):
	def __init__(self):		
		self.char="@"		
		self.cake_position=[]	

	def set_position(self,y,x):
		self.cake_position.append([y,x,False])		
