import pygame
import sys
import time
from random import randint
pygame.init()
screen=pygame.display.set_mode((1000,1000))
bg = pygame.image.load('sky.jpg')
bg_END = pygame.image.load('sky_END.jpg')
tux = pygame.image.load("Snipe.png")
pygame.display.set_caption("First Game")
Snipe= pygame.mixer.Sound("beam 8 small laser.ogg")
posX=randint(0,800)
posY=randint(0,850)
score = 0
timecounter= 120
clock = pygame.time.Clock()
texttime = '120'
pygame.time.set_timer(pygame.USEREVENT, 250)
movecount=0
music = pygame.mixer.music.load('M2U X NICODE - Lune.mp3')
pygame.mixer.music.play(-1)
while True:
	clock.tick(30)
	
	
	for x in pygame.event.get():
		prey = [pygame.image.load('bird_1.png'), pygame.image.load('bird_2.png'), pygame.image.load('bird_3.png'), pygame.image.load('bird_2.png')]

		mx,my=pygame.mouse.get_pos()
		screen.blit(bg, (0,0))
		screen.blit(prey[movecount], (posX,posY))
		screen.blit(tux,(mx-1007,my-1000))
		fontscore = pygame.font.SysFont('cconsolas', 30, True)
		fomttime = pygame.font.SysFont('consolas', 30, True)
		textscore = fontscore.render('Score: ' + str(score), True, (0,255,0))
		texttime = fontscore.render('Time: ' + str(timecounter), True, (0,255,0))
		screen.blit(textscore, (350, 10))
		screen.blit(texttime, (800, 100))
		pygame.display.update()
		if x.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
		
		if x.type == pygame.USEREVENT and timecounter!="Time's up": 
			movecount+=1
			if movecount +1  >= 4:
				movecount = 0
			screen.blit(prey[movecount], (posX,posY))
			pygame.display.update()
			timecounter -= 0.25
			texttime = str(timecounter)
			if timecounter < 0:
				timecounter="Time's up"
				continue
		elif timecounter == "Time's up":
			screen.blit(bg_END, (0,0))
			pygame.display.update()
			textscore1 = fontscore.render(' ' + str(timecounter), True, (0,255,255))
			fomtscore1 = pygame.font.SysFont('consolas', 300, True)
			texttime1 = fontscore.render('Final Score:' + str(score), True, (0,255,255))
			fomttime1 = pygame.font.SysFont('consolas', 120, True)
			screen.blit(textscore1, (450, 450))
			screen.blit(texttime1, (450, 470))
			pygame.display.update()
			time.sleep(5)
			pygame.quit()
			sys.exit()
		if x.type == pygame.MOUSEBUTTONDOWN:
			Snipe.play()
			print (mx, my)
			if (mx>posX and mx<posX+190) and (my>posY and my<posY+190):
				score+=1
				prey=None
				posX=randint(0,810)
				posY=randint(0,810)
		

			

