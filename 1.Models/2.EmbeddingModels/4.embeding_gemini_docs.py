from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    output_dimensionality=32
)
documents=[
    "Hello everyone",
    "How are you?",
    "My name is vishnu"
]
result=embedding.embed_documents(documents)

print(str(result))