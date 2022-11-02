from pytube import YouTube

save_path = "D:\\"
video_link = "https://www.youtube.com/watch?v=JeznW_7DlB0"

try:
    yt = YouTube(video_link)

except:
    print("Connection Error")

yt.streams.filter(progressive=True, file_extension="mp4").order_by(
    "resolution").desc().first().download(save_path)
