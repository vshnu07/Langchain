from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding=OllamaEmbeddings(model="nomic-embed-text:latest")

documents = [
    "Artificial intelligence is transforming industries by helping computers perform tasks that normally require human intelligence.",

    "Machine learning is a branch of artificial intelligence that allows computers to learn patterns from data and make predictions.",

    "Deep learning uses neural networks with multiple layers to solve complex problems such as image recognition and natural language processing.",

    "Cricket is a popular sport played between two teams of eleven players using a bat and ball.",

    "Football is one of the most popular sports in the world and is played by two teams trying to score goals."
]

query="tell me about AI"

doc_embedding=embedding.embed_documents(documents)
query_embeding=embedding.embed_query(query)


score=cosine_similarity([query_embeding],doc_embedding)[0]

index, score = sorted(
    list(enumerate(score)),
    key=lambda x: x[1]
)[-1]


print("Index:", index)
print("Score:", score)
print("Document:", documents[index])