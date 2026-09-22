import streamlit as st
import pymupdf

from summarizer import summarize_text


# ==========================================
# PDF PROCESSOR
# ==========================================

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


# ==========================================
# TEXT CLEANING
# ==========================================

def clean_text(text):

    text = text.replace("\n", " ")

    text = " ".join(text.split())

    return text


# ==========================================
# TEXT CHUNKING
# ==========================================

def create_chunks(text, chunk_size=3000):

    text = clean_text(text)

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


# ==========================================
# STREAMLIT CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI PDF Summarizer",
    page_icon="📄",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("📄 AI PDF Summarizer")

st.write(
    "Upload a PDF to extract, process, and summarize its content using AI."
)


# ==========================================
# PDF UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


# ==========================================
# MAIN PROCESS
# ==========================================

if uploaded_file:

    st.success("PDF uploaded successfully!")

    # Process PDF
    pdf_data = process_pdf(uploaded_file)

    pages = pdf_data["pages"]
    page_count = pdf_data["page_count"]
    total_characters = pdf_data["total_characters"]

    # Combine pages
    full_text = "\n".join(pages)

    # Create chunks
    chunks = create_chunks(full_text)


    # ==========================================
    # PDF INFORMATION
    # ==========================================

    st.subheader("📊 PDF Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Pages", page_count)

    with col2:
        st.metric("Characters", total_characters)

    with col3:
        st.metric("Chunks", len(chunks))


    # ==========================================
    # NO TEXT
    # ==========================================

    if total_characters == 0:

        st.warning(
            "No text was extracted from this PDF."
        )

        st.info(
            "This may be a scanned or image-based PDF. "
            "OCR support can be added later."
        )


    # ==========================================
    # TEXT AVAILABLE
    # ==========================================

    else:

        st.subheader("📄 Extracted Text")

        st.text_area(
            "PDF Content",
            full_text,
            height=300
        )


        # ==========================================
        # AI SUMMARY
        # ==========================================

        st.subheader("🤖 AI Summary")

        if st.button(
            "Generate Summary",
            type="primary"
        ):

            with st.spinner(
                "Generating summary..."
            ):

                summary = summarize_text(
                    chunks[0]
                )

            st.success(
                "Summary generated successfully!"
            )

            st.markdown(summary)