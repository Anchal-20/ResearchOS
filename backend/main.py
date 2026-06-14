from pathlib import Path

from pdf_processor import extract_text_from_pdf, chunk_text
from gemini_chat import ask_gemini
from vector_store import store_chunks, search_chunks


def main():

    BASE_DIR = Path(__file__).resolve().parent.parent

    pdf_path = BASE_DIR / "data" / "sample.pdf"

    text = extract_text_from_pdf(str(pdf_path))

    chunks = chunk_text(text)

    store_chunks(chunks)

    print(f"\nTotal Chunks Created: {len(chunks)}")

    question = input("\nAsk a question about the PDF: ")

    relevant_chunks = search_chunks(question)

    context = "\n\n".join(relevant_chunks)

    answer = ask_gemini(context, question)

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    main()