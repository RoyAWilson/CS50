'''

Apis intro

'''

import sys
import requests
import json

## User needs to type the name of the band at the prompt.
## or exit the program to the command line prompt

if len(sys.argv) !=2:
    sys.exit()

# send a request to apple

response = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=' + sys.argv[1])
# print(json.dumps(response.json(), indent= 2))

o = response.json()

for result in o['results']:
    print(result['trackName'])
# Note if the capitlisation is incorrect but name of the key trackName will print the whole of the json