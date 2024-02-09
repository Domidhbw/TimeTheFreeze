import pygame
from Menu import menu
class MusicHandler:

    def __init__(self):
         self.tracks = [
            "./music/dark-sanft-final.wav", #music in levels
            "./music/horrer_synths.wav"     #music im start screen
        ]
         self.currentTrack = 0
    def playMusic(self):
        pygame.mixer.music.load(self.tracks[self.currentTrack])
        pygame.mixer.music.play()
    def updateMusic(self):
        if  not pygame.mixer.music.get_busy():
            MusicHandler.playMusic(self)
            
#musicHandler = music.MusicHandler()
#musicHandler.playMusic()
#from music import music