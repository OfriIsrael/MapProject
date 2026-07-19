from time import sleep
from tkinter import *
import pygame


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\USER\Downloads\daily_download_20201020_128.mp3")
    pygame.mixer.music.play(loops=-1)

play_music()
sleep(100)



#'C:/Users/USER/Downloads/daily_download_20201020_128.mp3'