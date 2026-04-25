import fitz  # PyMuPDF

doc = fitz.open("New_Task Assignment _ AI Researcher Intern- Speech & Audio _ Josh Talks .pdf")
with open("links.txt", "w", encoding="utf-8") as f:
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        links = page.get_links()
        for link in links:
            if 'uri' in link:
                f.write(f"Page {page_num+1} Link: {link['uri']}\n")
