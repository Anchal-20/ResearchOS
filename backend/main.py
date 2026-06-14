from pdf_processor import extract_text_from_pdf
from vector_store import create_chunks


def main():
    pdf_path = "../data/sample.pdf"

    text = extract_text_from_pdf(pdf_path)

    chunks = create_chunks(text)

    print(f"\nTotal Chunks Created: {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0])


if __name__ == "__main__":
    main()