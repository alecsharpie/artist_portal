


![Image]()

# Install

Clone the project and install it:

```bash
git clone git@github.com:alecsharpie/artist_portal.git
cd artist_portal
make install # or `pip install .`
```

# Download SQL DB

Coming soon...

## Base Dataset Example

See original sheet here:
https://docs.google.com/spreadsheets/d/14xTqtuV3BuKDNhLotB_d1aFlBGnDJOY0BRXJ8-86GpA/edit


```python
from artist_portal.data import get_imgsynth_studies_artists

df_artists = get_imgsynth_studies_artists()
```

here `df_artists` is a `pd.DataFrame`.


## Wikipedia Dataset Examples

```python
from artist_portal.wikipedia_data import WikiGPT

wiki_gpt = WikiGPT(openai_api_key = os.getenv("OPENAI_API_KEY"))

json_artist = wiki_gpt.artist_to_json("Hilma_af_Klint")
```
here `artist_json` is a `dict`.

```
{'Name': 'Hilma af Klint',
 'Gender': 'She',
 'BirthYear': '1862',
 'DeathYear': ' 1944',
 'ArtStyle': 'Abstract',
 'ArtMovement': 'Abstract Art',
 'Location': 'Sweden',
 'Nationality': 'Sweden',
 'Occupation': 'Artist',
 'ArtSchool': 'Royal Academy of Fine Arts',
 'ArtistKey': 'Hilma_af_Klint',
 'WikipediaUrl': 'https://en.wikipedia.org/wiki/Hilma_af_Klint'}
 ```
