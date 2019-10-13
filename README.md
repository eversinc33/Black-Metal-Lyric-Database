# Black Metal Lyrics JSON Database

Database of Black Metal lyrics in .JSON format to be used for computer-assisted lyric analysis projects, collected from https://lyrics.fandom.com with additional metadata from https://www.metal-archives.com/ for my sociological bachelor thesis on Ideology and Black Metal.

Artists: 334

Albums: 1408

Songs: 11189

## Usage

Use your prefered JSON-parser or [jsonpickle](https://jsonpickle.github.io/) in Python3 and the classes provided in `/classes` to import the data. 

Example using jsonpickle:
```python3
# if not already installed: $ pip3 install jsonpickle
import jsonpickle

with open("./black_metal.json") as f:
    json_data = f.read()
    artists = jsonpickle.decode(json_data)
    
# you can then cycle through the objects:
for artist in artists:
    for release in artist.releases:
        for song in release.songs:
            print(song.lyrics)
```

## Structure

Example data:

```
[
   {
      "country":"SE",
      "current_label":"Century Media Records",
      "name":"Marduk",
      "py/object":"classes.artist.Artist",
      "releases":[
         {
            "name":"Panzer_Division_Marduk_",
            "py/object":"classes.album.Album",
            "release_year":"1999",
            "released_by":"Marduk",
            "songs":[
               {
                  "lyrics":"Storming forth with dreadful guns\nTo obliterate the chosen ones\nLucifer legions under the banner of the horns\nSlaying and crushing as the infidel mourns\nCrushing with metallic\nBehold us with fright as we storm through the night\n\nBlooddawn\n\nStorming forth with dreadful guns\nTo obliterate the chosen once\nHear our war cry as we reign the battlefield\nNow you can't hide behind no shelter nor shield\nThe heavens will bleed when the angels fall\nGunned down by the soldiers who have heard our call\n\nBlooddawn\n\nStorming forth with dreadful guns\nTo obliterate the chosen ones\nOur killing spree is thrilling me\nAnd by our guns you'll blasted be\nLost are those who worshipped the liar\nPanzer division Marduk engulfs you in fire\n\nBlooddawn",
                  "name": "Blooddawn",
                  "py/object":"classes.song.Song"
               }
            ]
         }
     ]
  }
]
```

## Disclaimer

I do not own these lyrics, nor do they represent my views. I collected them for educational purposes.
