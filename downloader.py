from time import sleep
import youtube_dl
import ffmpeg
import os


{
    ffmpeg
    .input('/home/milan/music/Pisces.mp4')
    .output('pisces.mp3')
    .run()
} 
sleep(2)
os.system('rm ./pisces.mp3')