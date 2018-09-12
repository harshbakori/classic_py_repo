#trex-game.skipsker.com  game URL

from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *



class Cordinates():
    replayBtn = (340, 390) #middle button of game 
    dinasaur = (171, 395) #dinasaur codinates as my screen resolution


def restartGame():
    pyautogui.click(Cordinates.replayBtn) #replay button 


def pressSapce():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')


def imageGrab():
    box = (
    Cordinates.dinasaur[0] + 240, Cordinates.dinasaur[1], Cordinates.dinasaur[0] + 100, Cordinates.dinasaur[1] + 30) #tree cordinates as box
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()


def main():
    restartGame()
    while True:
        if (imageGrab() != 1447): #conditions for make dino jump
            	pressSapce()
            	time.sleep(0.05)
main()
