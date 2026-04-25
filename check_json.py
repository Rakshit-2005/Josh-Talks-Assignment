import urllib.request
import json

url = "https://storage.googleapis.com/upload_goai/967179/825780_transcription.json"
try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    print(type(data))
    print(data)
except Exception as e:
    print(e)
