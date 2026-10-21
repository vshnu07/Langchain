from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model=ChatOllama(model="llama3.2:latest")
message=[
    SystemMessage(content="You are an helpul AI assitant")
]
while True:
    user_inp=input('You: ')
    message.append(HumanMessage(content=user_inp))
    if user_inp=='exit':
        break;
    result=model.invoke(message)
    message.append(AIMessage(content=result.content))
    print("AI: ",result.content)
print(message)