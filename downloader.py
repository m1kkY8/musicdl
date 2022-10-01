from __future__ import unicode_literals
import youtube_dl
import ffmpeg
import os

#videoLink = 'https://www.youtube.com/watch?v=SQNtGoM3FVU'


def download(ytdl):

    while 1:
        url = input("Enter URL: ")

        if url == 'q':
            return

        info = ytdl.extract_info(url, download=False)
        print("Video name: ",info['title'])
        sizeMB = info['formats'][0]['filesize']
        print("Size: %f MB: "% sizeMB)
        ytdl.download([url])
        


def status(d):

    eta = d.get('eta')

    if eta and eta >0:
        elapsed = d.get('elapsed')
        total_time = eta-elapsed
        percent = (total_time / 100) * elapsed
        print(percent,"%")
    

    if d['status'] == 'finished':
        print('Done downloading')


ydl_opts = {
    'format': 'bestaudio/best',
#    'outtmpl': '/home/milan/Music/',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
    
    'progress_hooks': [status],
    'quiet': True
}

ytdl = youtube_dl.YoutubeDL(ydl_opts)

download(ytdl)



    #https://www.youtube.com/watch?v=BaW_jenozKc
    #https://www.youtube.com/watch?v=0CM3IvuTuRk