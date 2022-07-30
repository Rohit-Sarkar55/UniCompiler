#Youtube Video  Downloader

from pytube import YouTube

link = input("Paste Your Link Here ")

yt = YouTube(link)

videos = yt.streams.all()

options = list(enumerate(videos))

for option in options:
    print(option)


resolution = int(input("Choose the resolution"))
videos[resolution].download()


print("Your Video ", yt.title , " downloaded Successfully ")