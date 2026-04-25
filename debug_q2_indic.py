from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

words = ["इंटरव्यू", "जॉब"]
for w in words:
    print(w, UnicodeIndicTransliterator.transliterate(w, "hi", "itrans").lower())
