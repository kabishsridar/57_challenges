from requests import get
r = get('https://pokeapi.co/api/v2/pokemon/1')
data = r.json()
# print(data.keys())
# print(data['abilities']) # the abilities is a list
# print(data['base_experience']) # it is integer (only 64 is returned)
# print(data['cries']) # it is a dictionary
# print(data['forms']) # it is a  list
# print(data['game_indices']) # it is a list
# print(data['height']) # integer (7)
# print(data['held_items']) # empty list
# print(data['id']) # integer (1)
# print(data['is_default']) # it is a boolean (True)
# print(data['location_area_encounters']) # it is a string (link :https://pokeapi.co/api/v2/pokemon/1/encounters)
# print(data['moves']) # it is a list
print(data['sprites']) # it is in the png format