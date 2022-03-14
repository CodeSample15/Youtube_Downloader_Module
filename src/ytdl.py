from __future__ import unicode_literals
import youtube_dl
import sys

if len(sys.argv) == 2:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': sys.argv[1],
            'preferredquality': '192',
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([sys.argv[0]])
else:
    print("Incorrect number of arguments given!")