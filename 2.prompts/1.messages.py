from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

model=ChatOllama(model="llama3.2:latest")

message=[
    SystemMessage(content='Youre an tutor to teach me langchain in detail'),
    HumanMessage(content='What is langchain?')
]

result=model.invoke(message)

message.append(AIMessage(content=result.content))

print(message)