import time
import pygame

timer = int(input("Enter time in seconds: "))

for i in range(timer, 0, -1):
    seconds = i % 60
    minutes = (i//60) % 60
    hours = (i//3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

    timer_sound = "hidupjokowi.mp3"

    if i == 0:
        print("Time is up")
        pygame.mixer.init()
        pygame.mixer.music.load(timer_sound)
        pygame.mixer.music.play()

        time.sleep(3)
        # while pygame.mixer.music.get_busy():
        #     time.sleep(1)



