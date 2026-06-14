from sentence_transformers import SentenceTransformer
import chromadb


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


client = chromadb.Client()

collection = client.get_or_create_collection(
    name="research_papers"
)


def store_chunks(chunks):

    for i, chunk in enumerate(chunks):

        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk]
        )


def search_chunks(query, top_k=3):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]