def make_album(singer, album_name, count_of_tracks=None):
    dict={"singer_name":singer, "album_name":album_name }
    if count_of_tracks:
        dict['count_of_tracks']=count_of_tracks
    print(dict)
    return dict
make_album('mahdi', 'hasti', 4)
make_album('samir', 'rare')
