import fitz  # PyMuPDF

doc = fitz.open("New_Task Assignment _ AI Researcher Intern- Speech & Audio _ Josh Talks .pdf")
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    links = page.get_links()
    for link in links:
        if 'uri' in link:
            print(f"Page {page_num+1} Link: {link['uri']}")
