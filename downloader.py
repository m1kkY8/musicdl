from webbrowser import get
import youtube_dl
import ffmpeg
import os


#videoLink = 'https://www.youtube.com/watch?v=SQNtGoM3FVU'

videoLink = input("Enter URL: ")

def getSongName(url):

    ydl = youtube_dl.YoutubeDL(
        {
            "outtmpl": "%(id)s%(ext)s",
            "noplaylist": True,
            "quiet": True,
            "format": "bestvideo",
        }
    )
    with ydl:
        result = ydl.extract_info(url, download=False)  
    return (result["title"]) 

print("Song name is: ", getSongName(videoLink))
