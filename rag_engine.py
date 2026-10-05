from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_chunks(text, chunk_size=500):

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        chunk_size
    ):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        if chunk.strip():

            chunks.append(chunk)

    return chunks


def create_vector_store(chunks):

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings.astype("float32")
    )

    return index, embeddings


def search_documents(
    query,
    chunks,
    index,
    top_k=3
):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        min(top_k, len(chunks))
    )

    results = []

    for index_number in indices[0]:

        if index_number < len(chunks):

            results.append(
                chunks[index_number]
            )

    return results
import requests


def generate_answer(question, context):
    prompt = f"""
You are a document question-answering assistant.

Answer the question using ONLY the information in the
document context below.

If the answer cannot be found in the context, say:
"I could not find the answer in the document."

Do not make up information.

DOCUMENT CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]