import pandas as pd

url1 = "https://docs.google.com/spreadsheets/d/1bujiO2NgtHlgqPlNvYAQf5_7ZcXARlIfNX5HNb9f8cI/export?format=csv"
try:
    df1 = pd.read_csv(url1)
    print("Link 1 Shape:", df1.shape)
    print(df1.head())
except Exception as e:
    print("Link 1 failed:", e)

url2 = "https://docs.google.com/spreadsheets/d/1JItJnilmmSWjx9tAIr06cbTsyGjMMxEMhaebvn5qBHM/export?format=csv"
try:
    df2 = pd.read_csv(url2)
    print("\nLink 2 Shape:", df2.shape)
    print(df2.head())
except Exception as e:
    print("Link 2 failed:", e)
