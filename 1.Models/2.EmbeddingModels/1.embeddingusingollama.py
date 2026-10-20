from langchain_ollama import OllamaEmbeddings

embedding=OllamaEmbeddings(model="nomic-embed-text:latest")

vector=embedding.embed_query("Delhi is the capital of India")
print(vector)