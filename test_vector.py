from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return model.encode(text).tolist()

# Example
log = "ORA-01555 snapshot too old error during query execution"
embedding = get_embedding(log)

print(len(embedding))  # should be 384
