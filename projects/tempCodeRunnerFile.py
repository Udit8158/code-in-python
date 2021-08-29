def playmusic():
    '''It play just random music from my given path {music_dir} by using os module'''
    music_dir = "D:\\music"
    songs = os.listdir(music_dir)
    speak("playing a random music")
    print(songs)
    os.startfile(os.path.join(music_dir,songs[randomNo]))