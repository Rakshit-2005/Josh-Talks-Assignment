import urllib.request
import csv
import io

url = "https://docs.google.com/spreadsheets/d/1bujiO2NgtHlgqPlNvYAQf5_7ZcXARlIfNX5HNb9f8cI/export?format=csv"
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
reader = csv.reader(io.StringIO(content))
rows = list(reader)

print("Headers:", rows[0])
for row in rows[1:3]:
    print("Row:", row)
