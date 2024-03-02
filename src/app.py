import os
from sqlalchemy import create_engine
import pandas as pd
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')



spot = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id,
                                                              client_secret = client_secret))
SW_uri = 'spotify:artist:7guDJrEfX3qb6FEbdPA5qi'

results = spot.artist_top_tracks(SW_uri)

top10_name= []
top10_duration_ms = []
top10_popularity = []
for track in results['tracks'][:10]:
    top10_name.append(track['name'])
    top10_duration_ms.append(round((track['duration_ms']/1000)/60, 2))
    top10_popularity.append(track['popularity'])
    
print(top10_duration_ms)
top10_df = pd.DataFrame(list(zip(top10_name, top10_popularity, top10_duration_ms)), columns=['nombre', 'popularidad', 'duracion_minutos'])
print(top10_df)

import seaborn as sbn

sbn.scatterplot(x='popularidad', y='duracion_minutos', data=top10_df)