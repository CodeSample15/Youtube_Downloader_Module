from __future__ import unicode_literals
import yt_dlp
import sys
import os

def download(format='wav', link=''):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(os.path.expanduser('~')) + '/Downloads/%(title)s-%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': sys.argv[2],
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

#making sure there are enough system arguments to run the program
if len(sys.argv) == 1:
    #ask for both the link and the format
    sys.argv.append(input("Enter the link for the video: "))
    sys.argv.append(input("Enter the format for the output audio (press enter for .wav default): "))

    if(sys.argv[2] == ''):
        sys.argv[2] = 'wav'
elif len(sys.argv) == 2:
    sys.argv.append('wav')

#double checking that there are enough arguments before running
if len(sys.argv) >= 3:
    if len(sys.argv) > 3:
        print("WARNING: Too many arguments entered. This isn't a problem, but only two are needed to run:") #print a warning, but continue running
        print(" the link to the video and the download format.")
        print("This may change in a future update (but not too likely)")

    #all of the correct arguments, download the audio
    try:
        download(format=sys.argv[2], link=sys.argv[1])
    except:
        print("Error downloading audio")
        print("Maybe you entered the arguments incorrectly?")