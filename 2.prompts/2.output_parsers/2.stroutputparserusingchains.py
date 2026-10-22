from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model=ChatOllama(model="llama3.2:latest")

template1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]

)

template2=PromptTemplate(
    template="write 5 line summary {text}",
    input_variables=["text"]

)

parser=StrOutputParser()

chain=template1| model| parser| template2| model| parser

result=chain.invoke({"topic":"black hole"})
print(result)