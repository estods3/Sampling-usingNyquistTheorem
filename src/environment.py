import pygame
import sys
import random
import math
import numpy, scipy.optimize
redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)
grayColor = pygame.Color(10,10,10)

##--------------------------------------------------------------------------------------------
## Environment: initializes 'pygame' environment for signal simulation
##--------------------------------------------------------------------------------------------
class Environment:
	def __init__(self, screenWidth, screenHeight):
		pygame.init()
                pygame.display.set_caption('Nyquist Shannon Sampling Theorem Simulator')
		self.screenSizeX, self.screenSizeY = screenWidth, screenHeight
		self.screen = pygame.display.set_mode((self.screenSizeX, self.screenSizeY))
		self.screen.fill((255,255,255))

	# Redraw the environment with current generation printout, obstacles, samples, and path
	def redrawEnv(self, inputSignalRate, frequencyScreenPos, time):
                ## Background and Signal Viewing Windows
		self.screen.fill((255,255,255))
                pygame.draw.rect(self.screen, blackColor, pygame.Rect(self.screenSizeX/2, 0, 5, self.screenSizeY))
                pygame.draw.rect(self.screen, grayColor, pygame.Rect(0, self.screenSizeY/2+50, self.screenSizeX, 2))

                ## Draw Slider
                if frequencyScreenPos <= 1:
                    frequencyScreenPos = 1
                    samplingFrequency = 1
		else:
                    #scale the position so the sampling frequency maxes at the signal window size
                    samplingFrequency = frequencyScreenPos/2

                pygame.draw.rect(self.screen, blackColor, pygame.Rect(0, 0, self.screenSizeX, 50))
                pygame.draw.rect(self.screen, redColor, pygame.Rect(frequencyScreenPos, 0, 20, 50))
		pygame.font.init()
                font = pygame.font.SysFont('Comic Sans MS', 25)
		textsurface = font.render('Sampling Rate: ' + str(samplingFrequency) + " Hz", False, (255, 255, 255))
		self.screen.blit(textsurface,(0,0))

                ## Draw Input Signal
                pygame.font.init()
                font = pygame.font.SysFont('Comic Sans MS', 25)
                textsurface = font.render('Input Signal: ' + str(inputSignalRate) + " Hz", False, (0, 0, 0))
                self.screen.blit(textsurface,(0, 50))

                timeToSamplesConversion = 1.0/(self.screenSizeX/2.0) # This converts the time shown in the viewing window (1.0 second) into discrete data points for displaying
                samplingInterval = int((1.0/timeToSamplesConversion) / samplingFrequency)
                inputPlotPoints = []
                outputPlotPoints = []
                for x in range(0, self.screenSizeX):
                    centerPlotLineOffset = self.screenSizeY/2 + 50
                    amplitude = 70
                    y = int(amplitude * math.sin((inputSignalRate) * (2*math.pi) * timeToSamplesConversion * x) + centerPlotLineOffset)
                    if(x-time < self.screenSizeX/2.0):
                        inputPlotPoints.append([int(x-time), y])
                    if(x-time > 0 and samplingInterval > 0 and x % samplingInterval == 0):
                        outputPlotPoints.append([int(x-time + (self.screenSizeX/2.0 + 5)), y])
                pygame.draw.lines(self.screen, [0, 0, 255], False, inputPlotPoints, 2)
                pygame.display.flip()

                ## Draw Sampled Signal
                pygame.font.init()
                font = pygame.font.SysFont('Comic Sans MS', 25)
                textsurface = font.render('Output Signal', False, (0, 0, 0))
                self.screen.blit(textsurface,(self.screenSizeX/2 + 10, 50))
                if(len(outputPlotPoints) > 1):
                    #Thanks to "unsym" for the function: https://stackoverflow.com/questions/16716302/how-do-i-fit-a-sine-curve-to-my-data-with-pylab-and-numpy
                    def fit_sin(tt, yy, timeToSamplesConversion):
                        '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
                        tt = numpy.array(tt)
                        yy = numpy.array(yy)
                        ff = numpy.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
                        Fyy = abs(numpy.fft.fft(yy))
                        guess_freq = abs(ff[numpy.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
                        guess_amp = numpy.std(yy) * 2.**0.5
                        guess_offset = numpy.mean(yy)
                        guess = numpy.array([guess_amp, 2.*numpy.pi*guess_freq, 0., guess_offset])

                        def sinfunc(t, A, w, p, c):  return A * numpy.sin(w*t + p) + c
                        popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
                        A, w, p, c = popt
                        f = w/(timeToSamplesConversion * 2.*numpy.pi)
                        fitfunc = lambda t: A * numpy.sin(w*t + p) + c
                        return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": numpy.max(pcov), "rawres": (guess,popt,pcov)}
                    a,b = zip(*outputPlotPoints)
                    res = fit_sin(a, b, timeToSamplesConversion)
                    print( "Amplitude=%(amp)s, freq =%(freq)s, phase=%(phase)s, offset=%(offset)s, Max. Cov.=%(maxcov)s" % res )
                    pygame.draw.lines(self.screen, [0, 255, 0], False, outputPlotPoints, 2)
                    pygame.display.flip()

                ## Update Display
		pygame.display.update()

	# Check to see if the program was exited
	def checkExited(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

