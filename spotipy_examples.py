from getspotifydata import *
import pandas as pd

# example with playlist...

# 'creamy' by Spotify - https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXdgz8ZB7c2CP
# URI = spotify:user:spotify:playlist:37i9dQZF1DXdgz8ZB7c2CP

# from the URI above...
playlist_user = 'spotify'
playlist_id = '37i9dQZF1DXdgz8ZB7c2CP'

# get ID of each track in the creamy playlist
track_ids = getPlaylistTrackIDs(playlist_user, playlist_id)

# get track name of each track in the creamy playlist
for each in track_ids:
    print(getTrackName(each))
