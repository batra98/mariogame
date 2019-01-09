from sys import argv as rd
import os
import time
import NonBlockingInput as hack
import config 
import scene
import mario_player
from random import randrange,randint
import coins
import small_enemy
import clouds
import poles
import cake
import pistol
import bulletclass
import ending
import flag_1
def init_game(height,width,level):


	config.mario=scene.Mario_map(height,width)

	config.mario.initialize()
	config.enemy=[]

	config.coin=coins.Coins()
	config.cake=cake.Cakes()
	config.pistol=pistol.Pistol()
	config.flagger=flag_1.Flag(config.mario.map_mario)

	if level == 1:
		counter=3
	elif level==2:
		counter=4	
	
	#initialize enemies
	for i in range(0,counter-2):
		for i in config.mario.boundary:
			enemy_original_y=i+randint(int(width/2),width-15)
			enemy_original_x=height-4
			config.enemy.append(small_enemy.enemy_1(enemy_original_x,enemy_original_y))
		stable_set=["#","&"]

	#initialize clouds
	for i in config.mario.boundary:
		n=randint(counter,counter+2)
		for count in range(0,n):
			cloud=clouds.Clouds(config.mario.map_mario)
			cloud_x,cloud_y=randint(30,140)+i,randint(3,5)
			cloud.update(n,cloud_y,cloud_x)
			config.clouds.append(cloud)

	#initialize pillars
	for i in config.mario.boundary:		
		for count in range(0,counter):
			pole=poles.Poles(config.mario.map_mario)
			pole_x,pole_y=randint(int(width/2),width-15)+i,height-4
			pole.draw(pole_x,pole_y)
			config.poles.append(pole)

	#initialize stairs
	for count in range(0,3):
		config.ending=ending.End(config.mario.map_mario)
		stair_x,stair_y=width*6+20+count*21,height-10
		config.ending.draw_left(stair_x,stair_y,height,width)
		stair_x,stair_y=width*6+31+count*21,height-10
		config.ending.draw_right(stair_x,stair_y,height,width)
		config.stair_coordinates.append([stair_x,stair_y])

	#initialize coins	
	for j in range(0,4):
		for i in range(0,6):
			k=randint(height-14,height-8)
			a=randint(int(width/12),width-24)
			b=a+12
			config.coin.set_position(k,a,randint(0,13),config.mario.boundary[i])
			config.coin.set_position(k,a,randint(0,13),config.mario.boundary[i])	
			config.mario.make_wall(k,a,b,config.char,i)
			config.mario.make_wall(k-1,a,b,config.char,i)
			if i%3 == 0:				
				cake_y,cake_x=k,a+randint(1,11)+config.mario.boundary[i]
				config.cake.set_position(cake_y,cake_x)
			if i%3 == 1:
				pistol_y,pistol_x=k,a+randint(1,11)+config.mario.boundary[i]
				config.pistol.set_position(pistol_y,pistol_x)	
				

	#initialize variables
	config.x_flag=width*6+int(width/2)+30
	config.y_flag=height-14
	config.flagger.draw_2(config.y_flag,config.x_flag)
	config.distance=0
	config.score=0
	config.index=0
	config.counter=0
	config.counter_back=0
	config.start_x=0
	os.system('clear')
	print("score- "+str(config.score)+" "+"distance- "+str(config.distance))
	config.player=mario_player.Mario(int(height-4),0)
	config.player.draw(config.mario.map_mario)
	for items in config.enemy:
		items.draw(config.mario.map_mario)
		config.enemy_count.append(1)
	config.mario.print_map(int(width),int(height),config.start_x)
	config.final_height=height-4
	config.limit=0
	config.flag=1
	config.follow_coefficient=-1
	config.game_over=False
	config.big_mario=False
	os.system('aplay -qN ./sound/theme.wav &')
	
#function to update map
def update_map(height,width,verify,steps):
	os.system('clear')
	print("score- "+str(config.score)+" "+"distance- "+str(config.distance))
	if config.player.get_y() < int(width/2):
		config.mario.print_map(int(width),int(height),config.start_x)
	else:
		if verify == True:
			config.counter_back=config.counter_back+steps	
		config.mario.print_map(int(width)+config.counter_back,int(height),config.start_x+config.counter_back)


def main(level=1):	
	height,width = os.popen('stty size','r').read().split()
	width = (int(width)-4)
	height=(int(height)-4)	
	kb=hack.KBHit()


	init_game(height,width,level)
	
	start_time=time.time()
	
	while(1):
			
		if time.time()-start_time > 89:
			os.system('aplay -qN ./sound/theme.wav &')			
			start_time=time.time()


		if config.big_mario == False:
			while(config.mario.map_mario[config.player.get_x()+1][config.player.get_y()]!='#' and config.mario.map_mario[config.player.get_x()+1][config.player.get_y()]!='&'):
				
				if kb.kbhit() and config.flag==1:
					text_2=kb.getch()
					config.flag=0
				else:
					text_2='p'

				
				if text_2=='d':
					config.distance+=1					
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+3)
					if config.player.get_y() > int(width/2):
						config.counter_back=config.counter_back

						
					
				elif text_2=='a':
					config.distance-=1					
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),max(config.player.get_y()-3,0))
					if config.player.get_y() > int(width/2):
						config.counter_back=config.counter_back
				else:
					config.player.update_pos(config.mario.map_mario,config.player.get_x()+1,config.player.get_y())				
					update_map(height,width,False,1)	
					time.sleep(0.02)



			config.flag=1
			x=-1
			y=-1
			coin_show=False
			cake_show=False
			for enemies in config.enemy:
				if config.player.get_y() == enemies.get_y() and config.player.get_x() == enemies.get_x():					
					if config.game_over == False:
						os.system('pkill -kill aplay')
						os.system('aplay -qN ./sound/mariodie.wav &')						
					config.mario.end_game(config.player.get_y(),config.player.get_x(),config.score,config.distance)					
					update_map(height,width,False,1)	
					config.game_over=True
					break				

			if kb.kbhit():
				text=kb.getch()
			else:
				text='p'

			if text=='r':
				os.system('pkill -kill aplay')
				os.system('aplay -qN ./sound/reset.wav &')
				init_game(height,width,level)

			if text=='q':
				os.system('pkill -kill aplay')
				break	
			if config.game_over == False:	

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "@":					
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.score=config.score+5
					config.player.char="M"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+1)
					update_map(height,width,True,1)
					config.big_mario=True

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "@":					
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.score=config.score+5
					config.player.char="M"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
					update_map(height,width,True,1)
					config.big_mario=True	

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] == "@":					
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.score=config.score+5
					config.player.char="M"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()-1)
					update_map(height,width,True,-1)
					config.big_mario=True

				if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "@":
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.score=config.score+5
					config.player.char="M"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
					update_map(height,width,False,1)
					config.big_mario=True

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "+":
						os.system('pkill -kill aplay')
						return 1
				if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()+1] == "+":
						os.system('pkill -kill aplay')
						return 1
				if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "+":
						os.system('pkill -kill aplay')
						return 1
				if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "+":
						os.system('pkill -kill aplay')
						return 1							

				if text == 'd':					
					config.distance+=1
					if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] != "#":
						config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+1)
						update_map(height,width,True,1)
						
					else:
						update_map(height,width,False,1)

				elif text == 'a':
					config.distance-=1
					config.counter=config.counter-1					
					if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] != "#":
						config.player.update_pos(config.mario.map_mario,config.player.get_x(),max(config.player.get_y()-1,0))
						update_map(height,width,True,-1)

					else:
						update_map(height,width,False,1)			
					
				elif text == 'w':
					os.system('clear')
					print("score- "+str(config.score)+" "+"distance- "+str(config.distance))
					os.system('aplay -qN ./sound/jump.wav &')					
					while(config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] != '#' and config.player.get_x() > config.final_height-14 and config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] != '&'):
						config.player.update_pos(config.mario.map_mario,config.player.get_x()-1,config.player.get_y())						
						update_map(height,width,False,1)	
						time.sleep(0.02)

					if config.mario.map_mario[config.player.get_x()-1][config.player.get_y()]=='#':
						config.mario.shift_up(config.player.get_x()-1,config.player.get_y())
						x=config.player.get_x()-3
						y=config.player.get_y()
						if [x+2,y] in config.coin.coin_position or [x+1,y] in config.coin.coin_position:
							config.coin.show(config.mario.map_mario,x-1,y)
							coin_show=True
							os.system('aplay -qN ./sound/coin.wav &')
						if [x+2,y,False] in config.cake.cake_position or [x+1,y,False] in config.cake.cake_position:
							os.system('aplay -qN ./sound/powerup_appear.wav &')
							config.cake.draw(config.mario.map_mario,x-1,y)
							try:
								config.cake.cake_position.remove([x+2,y,False])
							except Exception:
								pass
							try:		
								config.cake.cake_position.remove([x+1,y,False])
							except Exception:
								pass
							config.cake.cake_position.append([x-1,y,True])
						


					flag=1
					while(config.mario.map_mario[config.player.get_x()+1][config.player.get_y()]!='#' and config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] != '&'):
						if kb.kbhit() and flag==1:
							text_2=kb.getch()
							flag=0
						else:
							text_2='p'

						
						if text_2=='d':
							config.distance+=2							
							if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] !='#':
								config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+2)
								if config.player.get_y() > int(width/2):
									config.counter_back=config.counter_back+2
									
							else:
								config.player.update_pos(config.mario.map_mario,config.player.get_x()+1,config.player.get_y())						
						elif text_2=='a':
							config.distance-=2							
							config.player.update_pos(config.mario.map_mario,config.player.get_x(),max(config.player.get_y()-2,0))
							if config.player.get_y() > int(width/2):
								config.counter_back=config.counter_back-2
						else:
							config.player.update_pos(config.mario.map_mario,config.player.get_x()+1,config.player.get_y())						
						update_map(height,width,False,1)	
						time.sleep(0.02)						

						if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()]=="e":							
							os.system('aplay -qN ./sound/stomp.wav &')
							config.mario.smash_enemy(config.player.get_y(),config.player.get_x())
							config.score=config.score+10
							config.enemy_count.remove(1)
							for items in config.enemy:
								if items.get_x() == config.player.get_x()+1 and items.get_y() == config.player.get_y():
									config.enemy.remove(items)
									break							
							update_map(height,width,False,1)	
								

						if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "@":
							os.system('aplay -qN ./sound/powerup_take.wav &')
							if config.super_mario == False:
								config.score=config.score+5
								config.player.char="M"	
							config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
							update_map(height,width,False,1)
							config.big_mario=True		

				if x!=-1 and y!=-1:
					config.mario.shift_down(x,y)
					if coin_show == True:
						config.score=config.coin.disappear_coin(config.mario.map_mario,x-1,y,config.score)						
						if [x+1,y] in config.coin.coin_position:
							config.coin.coin_position.remove([x+1,y])
							
						if [x+2,y] in config.coin.coin_position:
							config.coin.coin_position.remove([x+2,y])
							

						config.coin.change_brick(config.mario.map_mario,x+1,y,"&")
						config.coin.change_brick(config.mario.map_mario,x+2,y,"&")


				
				for positions in config.cake.cake_position:
					if positions[2] == True and config.index%(1000) == 0:					

						while config.mario.map_mario[positions[0]+1][positions[1]] != "#" and config.mario.map_mario[positions[0]+1][positions[1]] != "&":
							config.cake.update_pos(positions[0]+1,positions[1],config.mario.map_mario,positions[0],positions[1])
							positions[0]=positions[0]+1

				
				for enemies in config.enemy:

					if enemies.get_y() < enemies.y_original-width/6:
						enemies.follow_coefficient=1
					elif enemies.get_y() > enemies.y_original+width/6:
						enemies.follow_coefficient=-1

					if abs(config.player.get_y()-enemies.get_y()) <= 10:
						 enemies.follow_coefficient=enemies.follow(config.player.get_y(),enemies.get_y())
					try:	 
						enemies.detect_collision(config.mario.map_mario)
					except Exception:
						config.enemy.remove(enemies)		 	
					if config.index%(10999) == 0:

						try:
							enemies.update_pos(config.mario.map_mario,enemies.get_x(),enemies.get_y()+enemies.follow_coefficient)
						except Exception:
							config.enemy.remove(enemies)	
						
				if config.index%(10999) == 0:			
					
					update_map(height,width,False,1)				
				config.index=config.index+1				

				if config.counter_back <= 0:
					config.counter_back=0
				if config.counter_back > width*7:
					print("You won")
					break
				config.final_height=config.player.get_x()
			else:
				time.sleep(0.02)



		#####################################################################################################################################
		#####################################################################################################################################
		elif config.big_mario == True:
			while(config.mario.map_mario[config.player.get_x()+1][config.player.get_y()]!='#' and config.mario.map_mario[config.player.get_x()+1][config.player.get_y()]!='&'):
				if kb.kbhit() and config.flag==1:
					text_2=kb.getch()
					config.flag=0
				else:
					text_2='p'
				if text_2=='d':
					config.distance+=1					
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+3)
					if config.player.get_y() > int(width/2):
						config.counter_back=config.counter_back						
					
				elif text_2=='a':
					config.distance-=1					
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),max(config.player.get_y()-3,0))
					if config.player.get_y() > int(width/2):
						config.counter_back=config.counter_back
				else:
					config.player.update_pos(config.mario.map_mario,config.player.get_x()+1,config.player.get_y())				
					update_map(height,width,False,1)	
					time.sleep(0.02)



			config.flag=1
			x=-1
			y=-1
			coin_show=False
			cake_show=False
			for enemies in config.enemy:
			
				if config.player.get_y() == enemies.get_y() and config.player.get_x() == enemies.get_x():
					os.system('aplay -qN ./sound/collision.wav &')
					if config.super_mario == False:
						config.big_mario=False
						config.player.char="m"
					elif config.super_mario == True:
						config.super_mario = False
						config.player.char="M"
					enemies.undo(config.mario.map_mario,enemies.get_y(),enemies.get_x())
					config.enemy.remove(enemies)					
					update_map(height,width,False,1)	
					

			if kb.kbhit():
				text=kb.getch()
			else:
				text='p'

			if text=='r':
				os.system('pkill -kill aplay')
				os.system('aplay -qN ./sound/reset.wav &')
				init_game(height,width,level)

			if text=='q':
				os.system('pkill -kill aplay')
				break	
			if config.game_over == False:	

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "@":					
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.score=config.score+5
					if config.super_mario == False:
						config.player.char="M"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+1)
					update_map(height,width,True,1)
					

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "@":					
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.score=config.score+5
					if config.super_mario == False:
						config.player.char="M"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
					update_map(height,width,True,1)
						

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] == "@":					
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.score=config.score+5
					if config.super_mario == False:
						config.player.char="M"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()-1)
					update_map(height,width,True,-1)
					

				if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "@":
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.score=config.score+5
					if config.super_mario == False:
						config.player.char="M"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
					update_map(height,width,False,1)
					
				if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "$":					
					config.score=config.score+5
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.player.char="S"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+1)
					update_map(height,width,True,1)
					config.super_mario=True
					

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "$":					
					config.score=config.score+5
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.player.char="S"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
					update_map(height,width,True,1)
					config.super_mario=True
						

				if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] == "$":					
					config.score=config.score+5
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.player.char="S"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()-1)
					update_map(height,width,True,-1)
					config.super_mario=True
					

				if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "$":
					config.score=config.score+5
					os.system('aplay -qN ./sound/powerup_take.wav &')
					config.player.char="S"
					config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
					update_map(height,width,False,1)
					config.super_mario=True
					
				if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "+":
					os.system('pkill -kill aplay')
					return 1
				if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()+1] == "+":
					os.system('pkill -kill aplay')
					return 1
				if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "+":
					os.system('pkill -kill aplay')
					return 1
				if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "+":
					os.system('pkill -kill aplay')
					return 1

				if text == 'd':					
					config.distance+=1

					if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] != "#":
						config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+1)
						update_map(height,width,True,1)
											
					else:
						update_map(height,width,False,1)

				elif text == 'a':
					config.distance-=1
					config.counter=config.counter-1					
					if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] != "#":
						config.player.update_pos(config.mario.map_mario,config.player.get_x(),max(config.player.get_y()-1,0))
						update_map(height,width,True,-1)

					else:
						update_map(height,width,False,1)			
					
				elif text == 'w':
					os.system('clear')
					print("score- "+str(config.score)+" "+"distance- "+str(config.distance))
					os.system('aplay -qN ./sound/jump.wav &')					
					while(config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] != '#' and config.player.get_x() > config.final_height-14 and config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] != '&'):
						config.player.update_pos(config.mario.map_mario,config.player.get_x()-1,config.player.get_y())					

						update_map(height,width,False,1)	
						time.sleep(0.02)

					if config.mario.map_mario[config.player.get_x()-1][config.player.get_y()]=='#':
						os.system('aplay -qN ./sound/breakblock.wav &')
						config.mario.shift_up_big(config.player.get_x()-1,config.player.get_y())
						x=config.player.get_x()-3
						y=config.player.get_y()
						if [x+2,y] in config.coin.coin_position or [x+1,y] in config.coin.coin_position:
							config.coin.show(config.mario.map_mario,x-1,y)
							coin_show=True
							os.system('aplay -qN ./sound/coin.wav &')
						if [x+2,y,False] in config.cake.cake_position or [x+1,y,False] in config.cake.cake_position:
							os.system('aplay -qN ./sound/powerup_appear.wav &')
							config.cake.draw(config.mario.map_mario,x-1,y)
							try:
								config.cake.cake_position.remove([x+2,y,False])
							except Exception:
								pass
							try:		
								config.cake.cake_position.remove([x+1,y,False])
							except Exception:
								pass
							config.cake.cake_position.append([x-1,y,True])
						if [x+2,y,False] in config.pistol.pistol_position or [x+1,y,False] in config.pistol.pistol_position:
							os.system('aplay -qN ./sound/powerup_appear.wav &')
							config.pistol.draw(config.mario.map_mario,x-1,y)
							try:
								config.pistol.pistol_position.remove([x+2,y,False])
							except Exception:
								pass
							try:		
								config.pistol.pistol_position.remove([x+1,y,False])
							except Exception:
								pass
							config.pistol.pistol_position.append([x-1,y,True])	
							

					flag=1
					while(config.mario.map_mario[config.player.get_x()+1][config.player.get_y()]!='#' and config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] != '&'):
						if kb.kbhit() and flag==1:
							text_2=kb.getch()
							flag=0
						else:
							text_2='p'

						if text_2=='d':
							config.distance+=4							
							if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] !='#':
								config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y()+4)
								if config.player.get_y() > int(width/2):
									config.counter_back=config.counter_back+4
									
							else:
								config.player.update_pos(config.mario.map_mario,config.player.get_x()+1,config.player.get_y())		
							
						elif text_2=='a':
							config.distance-=4							
							config.player.update_pos(config.mario.map_mario,config.player.get_x(),max(config.player.get_y()-4,0))
							if config.player.get_y() > int(width/2):
								config.counter_back=config.counter_back-4
						else:
							config.player.update_pos(config.mario.map_mario,config.player.get_x()+1,config.player.get_y())		
						
						update_map(height,width,False,1)	
						time.sleep(0.02)
						

						if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()]=="e":							
							os.system('aplay -qN ./sound/stomp.wav &')
							config.mario.smash_enemy(config.player.get_y(),config.player.get_x())
							config.score=config.score+10
							config.enemy_count.remove(1)
							for items in config.enemy:
								if items.get_x() == config.player.get_x()+1 and items.get_y() == config.player.get_y():
									config.enemy.remove(items)
									break							
							update_map(height,width,False,1)	
								
						if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "@":
							os.system('aplay -qN ./sound/powerup_take.wav &')
							config.score=config.score+5
							config.player.char="M"
							config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
							update_map(height,width,False,1)
							config.big_mario=True

						if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "$":
							config.score=config.score+5
							os.system('aplay -qN ./sound/powerup_take.wav &')
							config.player.char="S"
							config.player.update_pos(config.mario.map_mario,config.player.get_x(),config.player.get_y())
							update_map(height,width,False,1)
							config.super_mario=True
									

				if x!=-1 and y!=-1:
					config.mario.shift_down_big(x,y)
					if coin_show == True:
						config.score=config.coin.disappear_coin(config.mario.map_mario,x-1,y,config.score)						
						if [x+1,y] in config.coin.coin_position:
							config.coin.coin_position.remove([x+1,y])
							
						if [x+2,y] in config.coin.coin_position:
							config.coin.coin_position.remove([x+2,y])
							

						config.coin.change_brick(config.mario.map_mario,x+1,y,"&")
						config.coin.change_brick(config.mario.map_mario,x+2,y,"&")


				
				for positions in config.cake.cake_position:
					if positions[2] == True and config.index%(1000) == 0:						

						while config.mario.map_mario[positions[0]+1][positions[1]] != "#" and config.mario.map_mario[positions[0]+1][positions[1]] != "&":
							config.cake.update_pos(positions[0]+1,positions[1],config.mario.map_mario,positions[0],positions[1])
							positions[0]=positions[0]+1

				for positions in config.pistol.pistol_position:
					if positions[2] == True and config.index%(1000) == 0:

						while config.mario.map_mario[positions[0]+1][positions[1]] != "#" and config.mario.map_mario[positions[0]+1][positions[1]] != "&":
							config.pistol.update_pos(positions[0]+1,positions[1],config.mario.map_mario,positions[0],positions[1])
							positions[0]=positions[0]+1				
				for enemies in config.enemy:

					if enemies.get_y() < enemies.y_original-width/6:
						enemies.follow_coefficient=1
					elif enemies.get_y() > enemies.y_original+width/6:
						enemies.follow_coefficient=-1

					if abs(config.player.get_y()-enemies.get_y()) <= 10:
						 enemies.follow_coefficient=enemies.follow(config.player.get_y(),enemies.get_y())
					try:	 
						enemies.detect_collision(config.mario.map_mario)
					except Exception:
						config.enemy.remove(enemies)		 	
					if config.index%(10999) == 0:

						try:
							enemies.update_pos(config.mario.map_mario,enemies.get_x(),enemies.get_y()+enemies.follow_coefficient)
						except Exception:
							config.enemy.remove(enemies)						
				for bullets in config.bullets:
					
					if bullets.get_y() > bullets.y_original+width/6:
						config.mario.map_mario[bullets.get_x()][bullets.get_y()]=" "
						config.bullets.remove(bullets)
					else:	

						if config.index%(1099) == 0:
							if config.mario.map_mario[bullets.get_x()][bullets.get_y()+1]=="e":
								config.enemy_count.remove(1)
								for items in config.enemy:
									if items.get_x() == bullets.get_x() and items.get_y() == bullets.get_y()+1:
										config.enemy.remove(items)
										break
								
							if config.mario.map_mario[bullets.get_x()][bullets.get_y()] != "S":
								config.mario.map_mario[bullets.get_x()][bullets.get_y()]=" "

							if config.mario.map_mario[bullets.get_x()][bullets.get_y()+1]=="#":
								config.mario.map_mario[bullets.get_x()][bullets.get_y()]=" "
								config.bullets.remove(bullets)
								continue

							try:
								
								bullets.update_pos(bullets.get_x(),bullets.get_y()+1,config.mario.map_mario)
							except Exception:
								
								config.bullets.remove(bullets)
							update_map(height,width,False,1)			

					


				if config.super_mario == True:
					if text == "f":
						os.system('aplay -qN ./sound/fireball.wav &')
						bullet=bulletclass.Bullet(config.player.get_x(),config.player.get_y())
						config.bullets.append(bullet)

				if config.index%(10999) == 0:					
					update_map(height,width,False,1)				
				config.index=config.index+1

				if config.counter_back <= 0:
					config.counter_back=0
				if config.counter_back > width*7:
					
					break
				config.final_height=config.player.get_x()

			else:				
				break

	
		

	return 0	
if __name__ == '__main__':
    main()