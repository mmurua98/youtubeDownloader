from pytube import YouTube
from sys import argv
from datetime import timedelta
import os

# sys.argv is a list that contains all of the arguments passed to the program via the command line 
# (where the first item in the list is the script name "[0]").
#link = argv[1]

videoTitle = None
videoChannel = None
videoViews = None
videoThumbnail = None
videoLength = None
yd = None

def getVideo(link):
    yt = YouTube(link)
    #streams = set()
    # print("Title: ", yt.title)
    # print("views: ", yt.views)
    # print("Thumbnail: ", yt.thumbnail_url)
    # print("Channel: ", yt.author)

    global videoTitle, videoChannel, videoViews,videoThumbnail, videoLength, yd

    videoTitle = yt.title
    videoChannel = yt.author
    videoViews = yt.views
    videoThumbnail = yt.thumbnail_url
    videoLength = timedelta(seconds=int(yt.length))

    # for stream in yt.streams.filter(type="video"):  # Only look for video streams to avoid None values
    #     streams.add(stream.resolution)

    # print(streams)

    yd = yt.streams.get_by_resolution("720p")
    # yd.download('C:/Users/migmu/Desktop/pythonvideos')

def getTitle():
    return videoTitle

def getChannel():
    return videoChannel

def getViews():
    return videoViews

def getThumbnail():
    return videoThumbnail

def getLength():
    return videoLength

def downloadVideo():
    if os.name == "nt":
        DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
    else:  # PORT: For *Nix systems
        DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"
    return yd.download(DOWNLOAD_FOLDER)