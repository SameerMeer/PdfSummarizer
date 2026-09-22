import os

from dotenv import load_dotenv
from groq import Groq


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()


# ==========================================
# GROQ CLIENT
# ==========================================

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key
)


# ==========================================
# SUMMARIZE TEXT
# ==========================================

def summarize_text(text):

    prompt = f"""
You are an expert document summarizer.

Summarize the following document section
clearly and accurately.

Rules:

- Keep the important information.
- Remove unnecessary repetition.
- Do not invent information.
- Use simple language.
- Present the summary using bullet points.
- Focus only on information present in the text.

Document:

{text}
"""

    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    return (
        response
        .choices[0]
        .message
        .content
    )


# ==========================================
# SUMMARIZE ONE CHUNK
# ==========================================

def summarize_chunk(text):

    return summarize_text(text)


# ==========================================
# SUMMARIZE FULL DOCUMENT
# ==========================================

def summarize_document(chunks):

    chunk_summaries = []

    for i, chunk in enumerate(chunks):

        print(
            f"Summarizing chunk {i + 1} "
            f"of {len(chunks)}..."
        )

        summary = summarize_chunk(chunk)

        chunk_summaries.append(summary)


    # Combine all chunk summaries

    combined_summary = "\n\n".join(
        chunk_summaries
    )


    # ==========================================
    # FINAL SUMMARY PROMPT
    # ==========================================

    final_prompt = f"""
You are an expert document summarizer.

The following are summaries of different
sections of the same document.

Create one final summary of the entire document.

Rules:

- Combine related information.
- Remove duplicate information.
- Keep the most important points.
- Do not invent information.
- Use simple and clear language.
- Present the final answer using bullet points.
- Focus only on the information provided below.

Section summaries:

{combined_summary}
"""


    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],

        temperature=0.2
    )


    return (
        response
        .choices[0]
        .message
        .content
    )