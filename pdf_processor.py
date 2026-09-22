import pymupdf


def process_pdf(pdf_file):

    pdf_bytes = pdf_file.getvalue()

    document = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    pages = []
    total_characters = 0

    for page in document:

        text = page.get_text().strip()

        pages.append(text)

        total_characters += len(text)

    page_count = len(pages)

    document.close()

    return {
        "pages": pages,
        "page_count": page_count,
        "total_characters": total_characters
    }