import pygame
from Menu import menu
class MusicHandler:

    def __init__(self):
         self.tracks = [
            "./music/dark-sanft-final.wav", #music in levels
            "./music/horrer_synths.wav"     #music im start screen
        ]
         self.currentTrack = 0
    def playTrack(self,track):
        if self.currentTrack != track:
            pygame.mixer.music.load(self.tracks[track])
            pygame.mixer.music.play()
            self.currentTrack = track
    def updateMusic(self):
        if  not pygame.mixer.music.get_busy():
            MusicHandler.playMusic(self)
            
#musicHandler = music.MusicHandler()
#musicHandler.playMusic(0 or 1)
#from music import music