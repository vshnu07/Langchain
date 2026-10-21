from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

prompt=ChatPromptTemplate([
    ("system","you are a helpful AI assistant"),
    MessagesPlaceholder("history"),
    ("human","{question}")
])

result=prompt.invoke({
    "history":[("human","what is 5+2"),("ai","5 + 2 is 7")],
    "question":"Now multiply it with 4"
})

print(result)