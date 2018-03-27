import json
import os

from productai import Client

access_key_id = os.environ['ACCESS_KEY_ID']
access_key_secret = os.environ['ACCESS_KEY_SECRET']
service_id = os.environ['SERVICE_ID']
image_url = os.environ['IMAGE_URL']

cli = Client(access_key_id, access_key_secret)
api = cli.get_image_search_api(service_id)

# Specifies the maximum number of results, defaults is 20
resp = api.query(image_url, count=10)

json_data = json.loads(resp.text)

print(json_data)
