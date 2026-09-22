def clean_text(text):

    text = text.replace("\n", " ")

    text = " ".join(text.split())

    return text


def create_chunks(text, chunk_size=3000):

    text = clean_text(text)

    chunks = []

    for i in range(
        0,
        len(text),
        chunk_size
    ):

        chunk = text[
            i:i + chunk_size
        ]

        chunks.append(chunk)

    return chunks