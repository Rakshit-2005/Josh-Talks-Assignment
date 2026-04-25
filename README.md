# Josh Talks Assignment - AI Researcher Intern (Speech & Audio)

This repository contains solutions for the Josh Talks AI Researcher Intern assignment focusing on speech, audio, and natural language processing tasks.

## 📋 Project Overview

This project addresses challenges in Hindi language processing, including:
- **Hindi Number Normalization**: Converting spoken Hindi numbers to digits
- **English Transliteration Detection**: Identifying English words transliterated to Hindi
- **Hindi Spelling Classification**: Classifying words as correctly or incorrectly spelled in Hindi

## 📁 Project Structure

```
├── Ques2.ipynb                          # Question 2: Hindi Number Normalization & English Detection
├── Ques3.ipynb                          # Question 3: Hindi Spelling Classification
├── Question3_Spelling_Classification.csv # Output dataset from Question 3
├── check_headers.py                     # Utility to check Google Sheets headers
├── check_json.py                        # Utility to validate JSON data
├── check_sheets.py                      # Utility to fetch and verify Google Sheets data
├── check_sheets2.py                     # Extended sheet verification utility
├── check_sheets_full.py                 # Full sheet analysis utility
├── debug_q2.py                          # Debugging script for Question 2
├── debug_q2_2.py                        # Extended debugging for Question 2
├── debug_q2_indic.py                    # IndicNLP debugging for Question 2
├── get_links.py                         # Extract links from PDF documents
├── get_links2.py                        # Alternative link extraction method
├── get_links3.py                        # Enhanced link extraction utility
├── links.txt                            # Extracted links from assignment PDF
├── hi.dic                               # Hindi dictionary file
├── New_Task Assignment _ AI Researcher Intern- Speech & Audio _ Josh Talks .pdf # Original assignment
└── README.md                            # This file
```

## 🎯 Key Solutions

### Question 2: Hindi Number Normalization & English Transliteration

**File**: `Ques2.ipynb`

**Objectives**:
1. **Hindi Number Normalization**: Convert spoken Hindi numbers (e.g., "बीस" = 20) to digits
2. **English Word Detection**: Tag words in Hindi text that are English words transliterated to Devanagari script

**Key Features**:
- Comprehensive mapping of Hindi spoken numbers (0-99) and multipliers (सौ, हज़ार, लाख, करोड़)
- Handles multiple spellings and transliterations of Hindi numbers
- English word detection using NLTK English word corpus
- Safe punctuation stripping that preserves Hindi character diacritics (matras)
- Uses IndicNLP library for transliteration verification

**Libraries Used**:
- `nltk` - English word corpus
- `indic-nlp-library` - Hindi transliteration
- Python regex for pattern matching

---

### Question 3: Hindi Spelling Classification

**File**: `Ques3.ipynb`

**Objectives**:
- Classify 1,77,000 Hindi words as correctly or incorrectly spelled
- Provide confidence scores and reasoning for each classification

**Key Features**:
- **Multi-layer Validation**:
  1. Standard dictionary lookup using Hunspell dictionaries
  2. Phonotactic/formatting constraints validation
  3. English transliteration detection
- **Confidence Levels**: High, Medium, Low
- **Detailed Reasoning**: Each classification includes an explanation
- Uses LibreOffice Hindi dictionaries (`hi_IN.aff`, `hi_IN.dic`)

**Libraries Used**:
- `pandas` - Data processing
- `spylls` - Hunspell spell-checking
- `indic-nlp-library` - Hindi text processing
- `nltk` - English word validation

**Output**:
- `Question3_Spelling_Classification.csv` - Classification results with columns:
  - `Word`: The input Hindi word
  - `Classification`: "correct spelling" or "incorrect spelling"
  - `Confidence Score`: High/Medium/Low
  - `Reason`: Explanation for the classification

---

## 🔧 Utility Scripts

### Data Verification Scripts
- **`check_headers.py`**: Fetches and displays headers from Google Sheets
- **`check_sheets.py`**: Reads data from Google Sheets and displays structure
- **`check_sheets2.py`**: Extended sheet verification with additional validation
- **`check_sheets_full.py`**: Complete sheet analysis with full content preview

### Link Extraction
- **`get_links.py`**: Extracts links from PDF using PyPDF2 with regex fallback
- **`get_links2.py`**: Alternative link extraction method
- **`get_links3.py`**: Enhanced link extraction utility

### Debugging Scripts
- **`debug_q2.py`**: Debug utilities for Question 2 solutions
- **`debug_q2_2.py`**: Extended debugging and testing
- **`debug_q2_indic.py`**: IndicNLP-specific debugging

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas spylls indic-nlp-library nltk PyPDF2
```

### Running the Notebooks

1. **Question 2 - Hindi Number Normalization**:
   ```bash
   jupyter notebook Ques2.ipynb
   ```
   - Install required tools via first cell
   - Follow through data processing pipeline
   - Results show normalized numbers and English word tags

2. **Question 3 - Hindi Spelling Classification**:
   ```bash
   jupyter notebook Ques3.ipynb
   ```
   - Downloads English and Hindi dictionaries
   - Loads 1,77,000 word dataset from Google Sheets
   - Runs classification pipeline
   - Generates results CSV

---

## 📊 Dataset Information

### Question 3 Dataset
- **Source**: Google Sheets (https://docs.google.com/spreadsheets/d/17DwCAx6Tym5Nt7eOni848np9meR-TIj7uULMtYcgQaw/export?format=csv)
- **Size**: ~1,77,000 unique Hindi words
- **Format**: CSV with word column

### External Data Sources
- **English Dictionary**: NLTK words corpus
- **Hindi Dictionary**: LibreOffice hi_IN dictionary files
  - Format: Hunspell (.aff and .dic files)
  - Source: https://github.com/LibreOffice/dictionaries

---

## 💡 Technical Highlights

### Hindi Text Processing Challenges Addressed

1. **Character Encoding**: Proper handling of Devanagari script and Unicode
2. **Matra Preservation**: Safe punctuation stripping without damaging Hindi diacritics
3. **Transliteration**: Converting between Devanagari and Latin script representations
4. **Number Parsing**: Complex rules for Hindi number composition (e.g., "पचास" = 50)
5. **Spell Checking**: Multi-layer validation combining dictionary lookup and linguistic rules

### Code Quality Features
- Comprehensive error handling with try-except blocks
- Clear function documentation and logic comments
- Modular pipeline design for easy maintenance
- Safe string operations that preserve linguistic integrity

---

## 📈 Results & Output

### Question 2
- Normalized text with Hindi numbers converted to digits
- Tagged words showing English transliterations in Hindi text
- Preserved original text structure and flow

### Question 3
- Classification of all 1,77,000 words
- Confidence scores for each classification
- Detailed reasoning for transparency and debugging
- CSV export for further analysis

---

## 🔍 Key Libraries & Tools

| Library | Purpose |
|---------|---------|
| `pandas` | Data manipulation and CSV handling |
| `nltk` | English word corpus and NLP utilities |
| `indic-nlp-library` | Hindi transliteration and text processing |
| `spylls` | Hunspell dictionary integration |
| `PyPDF2` | PDF parsing and link extraction |
| `urllib` | Remote file and sheet fetching |
| `regex` | Pattern matching for text processing |

---

## 📝 Notes

- All Google Sheets are accessed via CSV export URLs
- Hindi dictionaries are downloaded from LibreOffice repositories on first run
- Dictionary downloads are cached locally to improve performance
- Scripts include error handling for network issues and missing dependencies

---

## 👤 Author

**Rakshit Modanwal**  
AI Researcher Intern - Josh Talks

---

## 📄 License

This project is part of the Josh Talks internship program.

---

## 🤝 Contributing

For questions or improvements related to this assignment, please contact the project maintainer.

---

**Last Updated**: April 2026  
**Status**: Assignment Complete ✓
