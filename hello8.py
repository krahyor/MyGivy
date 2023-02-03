from kivy.core.audio import SoundLoader

def __init__(self):
 # -----
 # change file test.mp3 to your favorite music
 self.sound = SoundLoader.load('test.mp3')
 self.sound.play()
 # -----
