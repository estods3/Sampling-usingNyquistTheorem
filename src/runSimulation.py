import pygame
import random
import numpy as np
from environment import Environment

################
# Main Program #
################

inputSig = random.randint(1, 100)
env = Environment(1000, 300)
env.redrawEnv(inputSig, 50, 0)

samplingFreqSelection = 0
t = 0

while(True):
    # check if game was exited
    #-------------------------
    env.checkExited()

    #Simulate Input Signal
    #-------------------

    #env.redrawEnv(inputSig, 2 * inputSig)

    #Sampling
    #-----------------

    # Input Selection
    if pygame.mouse.get_pressed()[0] != 0:
        samplingFreqSelection = pygame.mouse.get_pos()[0] - 5
        env.redrawEnv(inputSig, samplingFreqSelection, t)

    t = t + 1
    if(t > env.screenSizeX/2):
        t = 0
