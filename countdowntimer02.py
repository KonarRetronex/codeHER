import time
import pygame

angka = int(input("Masukkan angka dalam detik : "))

for i in range(angka,-1,-1):
    detik = i % 60
    menit = (i//60) % 60
    jam = (i//3600) %24
    print(f"{jam}:{menit:02}:{detik:02}")
    time.sleep(1)

    sound = "anime-wow-sound-effect.mp3"

    while i == 0:



        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()

        # time.sleep(3)

        if pygame.mixer.music.get_busy():
            time.sleep(1)
