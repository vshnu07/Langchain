from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage

model=ChatOllama(model="llama3.2:latest")
message=[]
while True:
    user_inp=input('You: ')
    if user_inp=='exit':
        break;
    message.append(HumanMessage(content=user_inp))
    result=model.invoke(message)
    message.append(AIMessage(content=result.content))
    print("AI: ",result.content)
