import pygame
import sys
import random

redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)

##--------------------------------------------------------------------------------------------
## Environment: initializes 'pygame' environment for signal simulation
##--------------------------------------------------------------------------------------------
class Environment:
	def __init__(self, screenWidth, screenHeight):
		pygame.init()
		self.screenSizeX, self.screenSizeY = screenWidth, screenHeight
		self.screen = pygame.display.set_mode((self.screenSizeX, self.screenSizeY))
		self.screen.fill((255,255,255))

	# Redraw the environment with current generation printout, obstacles, samples, and path
	def redrawEnv(self, inputSignalRate, frequencyScreenPos):
                ## Background
		self.screen.fill((255,255,255))
                pygame.draw.rect(self.screen, blackColor, pygame.Rect(self.screenSizeX/2, 0, 5, self.screenSizeY))

                ## Draw Slider
                if frequencyScreenPos < 0:
                    frequencyScreenPos = 0

                pygame.draw.rect(self.screen, blackColor, pygame.Rect(0, 0, self.screenSizeX, 50))
                pygame.draw.rect(self.screen, redColor, pygame.Rect(frequencyScreenPos, 0, 20, 50))
		pygame.font.init()
                font = pygame.font.SysFont('Comic Sans MS', 25)
		textsurface = font.render('Sampling Rate: ' + str(frequencyScreenPos) + " Hz", False, (255, 255, 255))
		self.screen.blit(textsurface,(0,0))

                ## Draw Input Signal
                pygame.font.init()
                font = pygame.font.SysFont('Comic Sans MS', 25)
                textsurface = font.render('Input Signal: ' + str(inputSignalRate) + " Hz", False, (0, 0, 0))
                self.screen.blit(textsurface,(0, 50))


                ## Draw Sampled Signal
                pygame.font.init()
                font = pygame.font.SysFont('Comic Sans MS', 25)
                textsurface = font.render('Output Signal: ', False, (0, 0, 0))
                self.screen.blit(textsurface,(self.screenSizeX/2 + 10, 50))

		#for sample in population.samples:
			#pygame.draw.rect(self.screen, sample.color, (sample.kinematics.p.x, sample.kinematics.p.y, 5, 5), 0)
			#if(sample.isFittest):
				#self.linePoints.append((sample.kinematics.p.x, sample.kinematics.p.y))
				#pygame.draw.lines(self.screen, (0, 0, 200), False, self.linePoints, 3)	
		pygame.display.update()

	# Check to see if the program was exited
	def checkExited(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

