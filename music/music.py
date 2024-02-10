import pygame

class MusicHandler:

    def __init__(self):
         self.tracks = [
            "./music/tracks/dark-sanft-final.wav", #music in levels 
            "./music/tracks/horrer_synths.wav"     #music im start screen
        ]
         self.currentTrack = 0
         
         #sound effects
         self.soundJump = pygame.mixer.Sound("./music/soundEffects/SoundEffect_Jump.wav")
         self.soundJump.set_volume(0.27)
         self.soundDie = pygame.mixer.Sound("./music/soundEffects/SoundEffect_Die.wav")
         self.soundDie.set_volume(0.5)
         self.soundClone = pygame.mixer.Sound("./music/soundEffects/SoundEffect_Clone.wav")
         self.soundClone.set_volume(0.5)
         self.soundJumpPad = pygame.mixer.Sound("./music/soundEffects/SoundEffect_JumpPad.wav")
         self.soundJumpPad.set_volume(0.3)
         
    #music
    def playTrack(self,track,update):
        if self.currentTrack != track or update:
            pygame.mixer.music.load(self.tracks[track])
            pygame.mixer.music.play()
            self.currentTrack = track
    def updateMusic(self):
        if  not pygame.mixer.music.get_busy():
            self.playTrack(self.currentTrack,True)
    
    #soundefects
    def playSoundJump(self):
        self.soundJump.play()
        
    def playSoundDie(self):
        self.soundDie.play()
        
    def playSoundClone(self):
        self.soundClone.play()
        
    def playSoundJumpPad(self):
        self.soundJumpPad.play()
        
        