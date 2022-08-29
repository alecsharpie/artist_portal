


![Image]()

# Install

Clone the project and install it:

```bash
git clone git@github.com:alecsharpie/artist_portal.git
cd artist_portal
make install # or `pip install .`
```

# Examples

Download the data from the repository linked above and instantiate the class pointing to the sql db. Do it manually (eg with chrome) if curl isn't working


## Original Dataset Example

See original sheet here:
https://docs.google.com/spreadsheets/d/14xTqtuV3BuKDNhLotB_d1aFlBGnDJOY0BRXJ8-86GpA/edit


```python
from artist_portal.data import get_ddstudies_data, get_ddstudies_artists

df_all = get_ddstudies_data()

df_artists = get_ddstudies_artists()
```

here `df_all` & `df_artists` are `pd.DataFrame's`.


## Full Dataset Examples


```
Table : col1, col2, col3, ...
----------
survey  :  id, qid, rating
generations  :  id, sid, method, prompt, verified
images  :  id, gid, idx
paths  :  iid, path
ratings  :  sid, iid, rating, verified
upscales  :  iid, method
```

```
ds.get_image_paths_and_prompts()

ds.get_prompts_and_ratings()

ds.get_image_paths_and_prompts_and_ratings()
```
