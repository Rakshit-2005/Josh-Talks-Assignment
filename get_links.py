import PyPDF2

def extract_links(pdf_path):
    links = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            if '/Annots' in page:
                for annot in page['/Annots']:
                    annot_obj = annot.get_object()
                    if '/A' in annot_obj and '/URI' in annot_obj['/A']:
                        links.append(annot_obj['/A']['/URI'])
    return links

try:
    links = extract_links("New_Task Assignment _ AI Researcher Intern- Speech & Audio _ Josh Talks .pdf")
    for link in links:
        print("LINK FOUND:", link)
except Exception as e:
    print("PyPDF2 might not be installed or error:", e)
    import re
    # Fallback to crude regex
    with open("New_Task Assignment _ AI Researcher Intern- Speech & Audio _ Josh Talks .pdf", 'rb') as f:
        content = f.read()
    urls = re.findall(b'URI \((http.*?)\)', content)
    for u in urls:
        print("LINK FOUND (regex):", u.decode('utf-8'))
