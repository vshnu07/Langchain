from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
model=ChatOllama(
    model="llama3.2:latest"
)
parser=StrOutputParser()
message=model.invoke("Tell me a joke")
print(message)
result=parser.invoke(message)
print(result)
