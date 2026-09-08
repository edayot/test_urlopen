import requests

url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f8/Lectern_JE2_BE1.png'

# Create a request object without sending it
req = requests.Request('GET', url, headers={
    'User-Agent': 'Mozilla/5.0'
})

# Prepare it to see what will be sent
prepared = req.prepare()

# Print everything
print("URL:", prepared.url)
print("Method:", prepared.method)
print("Headers:", dict(prepared.headers))
print("Body:", prepared.body)





from urllib.request import urlopen

URL = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f8/Lectern_JE2_BE1.png'

urlopen(URL)


