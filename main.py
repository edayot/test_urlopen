from urllib.request import Request, urlopen

URL = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f8/Lectern_JE2_BE1.png'

x = Request(URL)
print("Method:", x.get_method())
print("Full URL:", x.full_url)
print("Headers:", dict(x.headers))
print("Data:", x.data)

response = urlopen(x)

print("Method:", x.get_method())
print("Full URL:", x.full_url)
print("Headers:", dict(x.headers))
print("Data:", x.data)

print(response)
