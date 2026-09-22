import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()


# Get API key
api_key = os.getenv("GROQ_API_KEY")


# Create Groq client
client = Groq(
    api_key=api_key
)


def summarize_text(text):

    prompt = f"""
You are an expert document summarizer.

Summarize the following document clearly
and accurately.

Rules:

- Keep the important information.
- Remove unnecessary repetition.
- Do not invent information.
- Use simple language.
- Present the summary using bullet points.
- Focus only on information present in the document.

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


    summary = (
        response
        .choices[0]
        .message
        .content
    )


    return summary