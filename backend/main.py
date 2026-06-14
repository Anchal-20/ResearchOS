from pdf_processor import extract_text_from_pdf, chunk_text
from gemini_chat import ask_gemini


def main():

    pdf_path = "../data/sample.pdf"

    text = extract_text_from_pdf(pdf_path)

    chunks = chunk_text(text)

    print(f"\nTotal Chunks Created: {len(chunks)}")

    context = chunks[0]

    question = input("\nAsk a question about the PDF: ")

    answer = ask_gemini(context, question)

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    main()