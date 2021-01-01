import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'your_client_id'
client_secret = 'your_client_secret'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

'''
This function retrieves the track IDs of each track in a given album
Input: Spotify Album ID/URI (e.g., for Drake's Thank Me Later - spotify:album:6jlrjFR9mJV3jd1IPSplXU)
Output: List with track IDs
'''
def getAlbumIDs(album_id):
    song_ids = []
    results = sp.album_tracks(album_id,offset=0)
    for songs in results['items']:
        song_ids.append(songs['id'])
    return song_ids

'''
This function retrieves the track IDs of each track in a given playlist
Input: User ID of Playlist Creator and Play List ID/URI
Output: List with track IDs 
'''
def getPlaylistTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)

    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

'''
Get the track name for a given track ID
Input: Track ID/URI
Output: Name of track
'''
def getTrackName(id):

    meta = sp.track(id)
    return meta['name']

'''
This function returns the features (e.g., loudness, acousticness, instrumentalness, etc.) and
metadata (e.g. name, artist, album, popularity, etc.) of a given track
Input: Track ID/URI
Output: Lists with features/metadata
'''
def getTrackFeatures(id):

    meta = sp.track(id)
    features = sp.audio_features(id)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    ids = meta['id']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    valence = features[0]['valence']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    key = features[0]['key']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, ids, release_date, popularity, length, danceability, acousticness,
             energy, instrumentalness, liveness, valence, loudness, speechiness, tempo, key, time_signature]

    columns = ['name', 'album', 'artist', 'id', 'release_date', 'popularity', 'length', 'danceability',
               'acousticness', 'energy', 'instrumentalness','liveness', 'valence', 'loudness', 'speechiness',
               'tempo', 'key', 'time_signature']

    return track,columns