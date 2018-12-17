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
posx=randint(0,800)
posy=randint(0,850)
score = 0
timecounter= 120
clock = pygame.time.Clock()
texttime = '120'
pygame.time.set_timer(pygame.USEREVENT, 1000) 
music = pygame.mixer.music.load('M2U X NICODE - Lune.mp3')
pygame.mixer.music.play(-1)
while True:
	clock.tick(60)
	screen.blit(bg, (0,0))
	
	
	for x in pygame.event.get():
		
		mx,my=pygame.mouse.get_pos()
		prey_Y=pygame.image.load("Yellobird.png")
		screen.blit(prey_Y,(posx,posy))
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
		if x.type == pygame.MOUSEBUTTONDOWN:
			Snipe.play()
			print (mx, my)
			if (mx>posx and mx<posx+200) and (my>posy and my<posy+150):
				score+=1
				prey_Y=None
				posx=randint(0,800)
				posy=randint(0,850)
		if x.type == pygame.USEREVENT and timecounter!="Time's up": 
			timecounter -= 1
			texttime = str(timecounter)
			if timecounter < 0:
				timecounter="Time's up"
				continue
		elif timecounter == "Time's up":
			textscore = None
			fomtscore = None
			texttime = None
			fomttime = None
			screen.blit(bg_END, (0,0))
			pygame.display.update()
			textscore1 = fontscore.render(' ' + str(timecounter), True, (0,255,255))
			fomtscore1 = pygame.font.SysFont('consolas', 100, True)
			texttime1 = fontscore.render('Final Score:' + str(score), True, (0,255,255))
			fomttime1 = pygame.font.SysFont('consolas', 120, True)
			screen.blit(textscore1, (450, 450))
			screen.blit(texttime1, (450, 470))
			pygame.display.update()
			time.sleep(5)
			pygame.quit()
			sys.exit()

			
