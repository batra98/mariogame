import collectable_objects
class Pistol(collectable_objects.collectables):
	def __init__(self):
		self.char="$"		
		self.pistol_position=[]	

	def set_position(self,y,x):
		self.pistol_position.append([y,x,False])