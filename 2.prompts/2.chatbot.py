from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

model=ChatOllama(model="llama3.2:latest")
chat_history=[
    SystemMessage(content='Youre an tutor to teach me langchain in detail')
]
while True:
    user_inp=input('You: ')
    chat_history.append(HumanMessage(content=user_inp))
    if user_inp=='exit':
        break;
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)
print(chat_history)
