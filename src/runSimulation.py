import pygame
import random
import numpy as np
from environment import Environment

################
# Main Program #
################

inputSig = random.randint(3, 30)
samplingFreqSelection = inputSig * 2
t = 0

env = Environment(1000, 300)
env.redrawEnv(inputSig, samplingFreqSelection, 0)

while(True):
    ## check if game was exited
    #-------------------------
    env.checkExited()

    ## Sampling Signal Input Selection
    #---------------------------------
    if pygame.mouse.get_pressed()[0] != 0:
        samplingFreqSelection = pygame.mouse.get_pos()[0] - 5
        env.redrawEnv(inputSig, samplingFreqSelection, t)

    #Sampling and Signal Reconstruction
    #----------------------------------


    ## Update Time
    #-------------
    t = t + 1
    if(t > env.screenSizeX/2):
        t = 0
