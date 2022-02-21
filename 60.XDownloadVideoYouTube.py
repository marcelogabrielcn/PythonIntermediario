from pytube import YouTube

youtube = YouTube('<link do video>')
for stream in youtube.streams:
    print(stream)

#Baixo Vídeos mp4 format
#youtube.streams.get_highest_resolution().download()

#Baixar apenas áudio mp4 format
#youtube.streams.get_audio_only().download()
