import json

c_imp = input("command: ")
playlist = []
ptitle = ""

while c_imp != "close":
    if c_imp == "load":
        with open('./playlists/playlist_{}.list'.format(input("playlist: ")), 'r+') as pls:
            playlist = json.loads(pls.read())
            pls.close()
    if c_imp == "title":
        ptitle = input("enter playlist title: ")
    if c_imp == "add":
        title = input("title: ")
        artist = input("artist: ")
        playlist.append({
            "name": title,
            "artist": artist
        })
    if c_imp == "save":
        with open('./playlists/playlist_{}.list'.format(ptitle), 'w+') as p_file:
            p_file.write(json.dumps(playlist))
            p_file.close()
    
    c_imp = input("command: ")