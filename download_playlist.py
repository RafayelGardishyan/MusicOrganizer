from youtube_search import YoutubeSearch
import json
import youtube_dl
from os import listdir, mkdir
import os


playlist = []

playlist_title = input("playlist: ")

with open('playlists/playlist_{}.list'.format(playlist_title), 'r+') as playlist_file:
    playlist = json.loads(playlist_file.read())

if not os.path.isdir("./download/{}".format(playlist_title)):
    mkdir("./download/{}".format(playlist_title))

for track in playlist:

    # if not track["name"].lower() in str(listdir("./download")).lower():
    #     results = YoutubeSearch("{} by {} lyrics".format(track["name"], track["artist"]), max_results=1).to_json()
    #     ydl_opts = {
    #         'format': 'bestaudio/best',
    #         'postprocessors': [{
    #             'key': 'FFmpegExtractAudio',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '192',
    #         }],
    #         'outtmpl': 'download/%(title)s.%(etx)s',
    #         'quiet': False
    #     }

    #     print("Downloading: {}".format(json.loads(results)["videos"][0]["title"]))
    #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #         ydl.download(['https://www.youtube.com/watch?v={}'.format(json.loads(results)["videos"][0]["id"])])
    # else:
    #     print(track["name"], "already exists")

    results = YoutubeSearch("{} by {} lyrics".format(track["name"], track["artist"]), max_results=1).to_json()
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'download/' + playlist_title + '/%(title)s.%(etx)s',
        'quiet': False
    }

    print("Downloading: {}".format(json.loads(results)["videos"][0]["title"]))
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v={}'.format(json.loads(results)["videos"][0]["id"])])