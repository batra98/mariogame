import main_mario_4
import start_screen
import os
import NonBlockingInput as hack
import config
from random import randint

height,width = os.popen('stty size','r').read().split()
width = (int(width)-4)

height=(int(height)-4)
start=start_screen.start(height,width)

start.initialize()
start.label()
os.system('clear')
start.draw()

kb = hack.KBHit()
text="f"
while(1):
	if kb.kbhit():
		text = kb.getch()

	if text == "e":
		back=main_mario_4.main(1)
		break
	elif text == "h":
		back=main_mario_4.main(2)
		break	
	elif text == "q":
		break


	


if back == 0:
	print("Game exited normally")
else:
	print("You won")
	print("score- "+str(config.score)+" "+"distance- "+str(config.distance))
	while(config.drop>=0):

		if config.drop%(109999)==0:
			
			config.mario.map_mario[config.y_flag-randint(3,6)][config.x_flag+randint(-9,+9)]="*"
			
		if(config.drop%(1099999)==0):
			os.system('clear')
			os.system('aplay -qN ./sound/fireworks.wav &')	
			config.flagger.draw(config.g,config.y_flag,config.x_flag)
			main_mario_4.update_map(height,width,False,1)
			config.g=config.g+1

		config.drop+=1
		if config.g>6:
			break

	print("You won")
	print("score- "+str(config.score)+" "+"distance- "+str(config.distance))			
