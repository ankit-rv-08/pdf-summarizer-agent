import fitz  # PyMuPDF
import os
import tiktoken

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def split_text_into_chunks(text, max_tokens=500):
    encoding = tiktoken.get_encoding("cl100k_base")
    words = text.split()
    chunks = []
    current_chunk = []
    tokens = 0

    for word in words:
        word_tokens = len(encoding.encode(word + " "))
        if tokens + word_tokens > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            tokens = word_tokens
        else:
            current_chunk.append(word)
            tokens += word_tokens

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# Test run
if __name__ == "__main__":
    text = extract_text_from_pdf("sample.pdf")
    chunks = split_text_into_chunks(text)
    print(f"Extracted {len(chunks)} chunks.")

    import openai
    import time

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"
# Optional: to avoid rate limit errors
def safe_gpt_request(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes academic content."},
                {"role": "user", "content": f"Summarize this text:\n\n{prompt}"}
            ],
            temperature=0.3
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Error: {e}")
        return ""

# Use this only if you already have your `chunks` list from earlier
summaries = []

print(f"Summarizing {len(chunks)} chunks...")
for i, chunk in enumerate(chunks):
    print(f"Summarizing chunk {i+1}/{len(chunks)}...")
    summary = safe_gpt_request(chunk)
    summaries.append(summary)
    time.sleep(1.5)  # Avoid hitting rate limits

# Combine summaries
final_summary = "\n\n".join(summaries)

# Print or save the summary
print("\n📄 Final Summary:\n")
print(final_summary)

# Optional: save to file
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(final_summary)
