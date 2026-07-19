from time import sleep
from tkinter import *
import pygame
#variables
#C:\Users\USER\Downloads\daily_download_20201020_128.mp3

music_files_list = [r"C:\Users\USER\PycharmProjects\The_Final_Project\FP_Music\daily_download_20171020_128.mp3",r"C:\Users\USER\PycharmProjects\The_Final_Project\FP_Music\daily_download_20201020_128.mp3",
                    ]


file_location = r"/static/daily_download_20201020_128.mp3"

current_music_queue = []




def Check_If_Idle():
    if pygame.mixer.music.getbusy():
        print ("finished")

# plays a song
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(file_location)
    pygame.mixer.music.play(loops=0)

play_music()
while True:
    one = 1



#'C:/Users/USER/Downloads/daily_download_20201020_128.mp3'