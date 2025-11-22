import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
r = requests.get(url)
d = r.json()
print(d["text"])
