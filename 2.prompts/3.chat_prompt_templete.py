#create dynamic templete

from langchain_core.prompts import ChatPromptTemplate
chat_templete=ChatPromptTemplate([
    ("system","you are a helpful {domain} expert"),
    ("human","Explain in simple terms what is {topic}")
])

prompt=chat_templete.invoke({
    "domain":"cricket",
    "topic":"players"
})

print(prompt)