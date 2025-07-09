import json
from pathlib import Path

movies = [
    {"id":1 , "Title":"Titanic" },
    {"id":2 , "Title":"Kindergaden" }

]

data = json.dumps(movies)
print(data)

Path("movies.json").write_text(data)