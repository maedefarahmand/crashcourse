def make_album(singer, album_name, count_of_tracks=None):
    dict={"singer_name":singer, "album_name":album_name }
    if count_of_tracks:
        dict['count_of_tracks']=count_of_tracks
    print(dict)
    return dict



def user_albums():
    while True:
        c=input("enter singer name")
        if c=='q':
            break
        b=input("enter album name")
        if b=='q':
            break
        make_album(c, b)

user_albums()