# pdf-summarizer-agent
A simple ChatGPT-powered agent that summarizes PDF content into clean, readable bullet points using prompt chaining.

# PDF Summarizer Agent (v1)

This is a minimalist AI agent built using ChatGPT to convert PDF content into summarized bullet points. Ideal for quick content review, reports, or presentation prep.

## 🔍 What It Does

- Accepts input from a text-extracted PDF.
- Uses a custom prompt to summarize the content into clear bullet points.
- (Optional) Converts bullet points to slide-style formatting.

## 📂 Files

- `prompts/`: Prompt files for summarization and formatting
- `sample_data/`: Example input and output summaries
- `logic/summary_pipeline.md`: System flow and chaining logic
- `notes/design_notes.md`: Observations, tuning details, and future ideas

## 🚀 How to Use

1. Copy any PDF text into the format of `sample_input.txt`.
2. Use ChatGPT with the prompt in `summarization_prompt.txt`.
3. Review or refine output using `slide_style_prompt.txt`.

---

## 📌 Status

✅ MVP completed  
🛠 AutoDeck version coming soon (slideshow builder + PDF parser + automation)

## ✍️ Author

Built during an 1800-hour AI mastery journey to develop expert-level AI agents and tools.
