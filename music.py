from pygame import mixer

def playmusic(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    print("Music playing ...")
    while True:
        print("write stop for stop the music")
        a=input()
        
        if(a=="stop"):
            mixer.music.stop()
            break

def user_choice():
    print("""
    1. song1
    2. song2
    3. song3
    """)
    ch =int(input("Enter your choice : "))
    if ch == 1:
        playmusic("song1.mp3")
    elif ch == 2:
        playmusic("song2.mp3")
    elif ch == 3:
        playmusic("song3.mp3")

        


if __name__ == '__main__':
    user_choice()
    
    while True:
        print("Want to play next song write, show list and write exit, if you want to exit")
        ag=input()
        
        if(ag=="show list"):
            user_choice()
        if(ag=="exit"):
            break

