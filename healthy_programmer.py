from pygame import mixer
from datetime import datetime
from time import time

def musicplay(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a == stopper:
            mixer.music.stop()
            break

def log_m(msg):
    with open("my_log.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musicplay("song1.mp3","stop")

    init_water=time()
    init_eye=time()
    init_excercies=time()

    water=5
    eye=30
    excercies=40

    while True:
        if time()-init_water>water:
            
            print("Please Drink water. for stop write water")
            musicplay("song1.mp3","water")
            init_water=time()
            print("Thank you")
            log_m("water  ")
        if time()-init_eye>eye:
            print("Please take rest some time. for stop write eye")
            musicplay("song2.mp3","eye")
            init_eye=time()
            print("Thank you")
            log_m("Rest  ")
        if time()-init_excercies>excercies:
            print("Do some excercies. for stop write excercies")
            musicplay("song3.mp3","excercies")
            init_excercies=time()
            print("Thank you")
            log_m("Excercies  ")
            
        
