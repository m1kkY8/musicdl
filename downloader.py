from __future__ import unicode_literals
import youtube_dl
import ffmpeg
import os

#videoLink = 'https://www.youtube.com/watch?v=SQNtGoM3FVU'



def status(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')



ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    
    'progress_hooks': [status],
    'quiet': True
}

ytdl = youtube_dl.YoutubeDL(ydl_opts)


url = input("Enter URL: ")

title = ytdl.extract_info(url, download=False)

print("Video name: ",title['title'])

dlBool = input("Download video (y/n): ")

if dlBool == 'y':
    ytdl.download([url])
    print("Downloaded ", title['title'])


    #https://www.youtube.com/watch?v=BaW_jenozKc
    #https://www.youtube.com/watch?v=0CM3IvuTuRk