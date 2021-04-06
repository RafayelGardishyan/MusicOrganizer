from youtube_search import YoutubeSearch
import json
import youtube_dl
from os import listdir, mkdir
import os
import music_tag
import sys
import unidecode


playlist = []

playlist_title = input("playlist: ")

with open('playlists/playlist_{}.list'.format(playlist_title), 'r+') as playlist_file:
    playlist = json.loads(playlist_file.read())

if not os.path.isdir("./download/{}".format(playlist_title)):
    mkdir("./download/{}".format(playlist_title))

def download_song(playlist_t, name, artist):
    cname = name
    illegal = ['NUL','\',''//',':','*','"','<','>','|']
 
    for i in illegal:
        cname = cname.replace(i, '')

    filename = "{} - {}.mp3".format(artist, cname)
    directory = "./download/{}/".format(playlist_t)
    try:
        if not filename in str(listdir(directory)):
            results = YoutubeSearch("{} by {} lyrics".format(name, artist), max_results=1).to_json()
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': 'download/' + playlist_t + '/current.%(etx)s',
                'quiet': False
            }
    
            print("Downloading: {}".format(filename))
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v={}'.format(json.loads(results)["videos"][0]["id"])])

            print("Renaming file to {}".format(filename))
            os.rename(
                "{}current.mp3".format(directory), 
                "{}{}".format(directory, filename)
                )

            print("Setting tags")
            f = music_tag.load_file(directory + filename)
            f["title"] = name
            f["artist"] = artist
            f.save()

        else:
            print("{} already exists".format(filename))
    
    except Exception as e:
        print(e)
        # if input("Try again? (yes / no) ") == "no":
        #     sys.exit()
        print("[Error] Trying again")
        download_song(playlist_title, unidecode.unidecode(name), artist)

for track in playlist:    
    download_song(playlist_title, track["name"], track["artist"])