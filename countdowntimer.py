import time
import pygame


timer =int(input("Masukkan berapa detik maunya: "))

for i in range(timer, -1, -1):
    detik = i % 60  #modulus 60 biar kalo detiknya lebih dari 60,
                    # yang keambil cuman sisanya

    menit = (i // 60) % 60 #i//60 karna seminit itu cuman 60 detik,
                           # %60 biar menitnya gak lebih dari 60

    jam = (i // 3600) % 24  #i//3600 karna satu jam ada 3600 detik
                            #% 24 karna jam cuman nyampe 24

    print(f"{jam:02}:{menit:02}:{detik:02}") #buat nampilin timernya
    time.sleep(1) #dia bakal nunggu satu detik dulu baru ngejelanin hal setelahnya

    sound_effect = "hidupjokowi.mp3"


    if i == 0:
        print("TIME IS UP")
        pygame.mixer.init()
        pygame.mixer.music.load(sound_effect)
        pygame.mixer.music.play()

        time.sleep(3)
        # while pygame.mixer.music.get_busy():
        #     time.sleep(1)









