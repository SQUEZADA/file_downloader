import requests
import pathlib
import json

#auth_token = 'your-authentication-token' 
destination = '' # output file location

session = requests.Session() #init request session
#session.headers.update({'Authorization': f'Bearer {auth_token}'})

images = open("directus_files 20230329-155710.json", "r") # I use a list of files
fileName = ""
for x in images:
  fileInfo = json.loads(x)
  for y in fileInfo:
    url = f'https://it3nvwv1.directus.app/assets/{y["id"]}'
    response = session.get(url)
    with open(pathlib.Path(destination, y["filename_download"]), 'wb') as f:
        f.write(response.content)
    print(f'Download complete: {pathlib.Path(destination, y["filename_download"]).exists()}')
images.close()

