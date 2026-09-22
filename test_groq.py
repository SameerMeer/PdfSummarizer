from summarizer import summarize_text


text = """
Artificial intelligence is a field of computer science
that focuses on creating systems capable of performing
tasks that normally require human intelligence.
"""


summary = summarize_text(text)


print("\nSUMMARY:\n")

print(summary)