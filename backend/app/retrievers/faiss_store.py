import faiss

import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

stored_errors = []


def add_error_embedding(
    error_text,
    embedding
):

    vector = np.array(
        [embedding],
        dtype="float32"
    )

    index.add(vector)

    stored_errors.append(error_text)


def search_similar_errors(
    embedding,
    top_k=3
):

    vector = np.array(
        [embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(stored_errors):

            error = stored_errors[idx]

            if error not in results:

             results.append(error)

    return results