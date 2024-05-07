from logic.Shazzam import Shazzam
from tools.mic import record_audio

def main():
    engine = Shazzam()
    '''
    this will add songs present in 'mp3' folder to database
    don't worry if song is already added, it wont over-write so saves time :)
    '''
    engine.add_songs()
    '''
    just write song name, which is present in 'test' folder 
    no need to mention relative path
    '''
    # engine.match_song('5.m4a')
    filename = "output.wav"
    record_audio(f"./test/{filename}")
    engine.match_song(f"{filename}")

if __name__=="__main__":
    main()