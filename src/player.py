import time
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def play(self, filepath, play_time=10):
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        print(f"🎵 Now Playing: {filepath} (for {play_time} sec)")

        time.sleep(play_time)   # play limited duration
        pygame.mixer.music.stop()

        while pygame.mixer.music.get_busy():
            time.sleep(5)
        pygame.quit()
