import json

movie_data = """{"Title": "",
              "Release Date": "",
              "Duration": "",
              "Genre": "",
              "Rated": "",
              "Movie Url": "",
              "user-agent": ""
              }"""

load = json.loads(movie_data)

print("JSON string = ", load)
print()

data = {}
with open('movie_dataset.json', "r") as data_set:
    data = json.loads(data_set.read())

sorted_data = sorted(data[:], key=lambda i: i["Rated"], reverse=True)

sorted_data = json.dumps(sorted_data, ensure_ascii=False, indent=4).encode('utf8')

with open('../imdb/sorted_dataset.json', "wb") as data_set:
    print('Sorting Movies by rating:')
    data_set.write(sorted_data)

