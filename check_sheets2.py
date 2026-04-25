import urllib.request
import csv
import io

urls = [
    "https://docs.google.com/spreadsheets/d/1bujiO2NgtHlgqPlNvYAQf5_7ZcXARlIfNX5HNb9f8cI/export?format=csv",
    "https://docs.google.com/spreadsheets/d/1JItJnilmmSWjx9tAIr06cbTsyGjMMxEMhaebvn5qBHM/export?format=csv"
]

for i, url in enumerate(urls):
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        reader = csv.reader(io.StringIO(content))
        rows = list(reader)
        print(f"\n--- Link {i+1} ---")
        print("Total Rows:", len(rows))
        print("Headers:", rows[0] if rows else "Empty")
        print("Row 1:", rows[1] if len(rows) > 1 else "Empty")
    except Exception as e:
        print(f"Link {i+1} failed:", e)
