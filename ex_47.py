from requests import get # importing get from requests module 
r = get('http://api.open-notify.org/astros.json') # get the data in the url and store it to response object
data = r.json() # store in dictionary format
print("NAME                 |  Craft")
print("-" * 30)
for person in data['people']: # for each person in data print the name and craft
    print(f"{person['name']:<20} |  {person['craft']:<10}") # :<20 and :<10 is used for alignment
