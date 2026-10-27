from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a detail report {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Generate a 5 line summary from following text \n {text}",
    input_variables=["text"]
)

model=ChatOllama(model="llama3.2:latest")

parser=StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({"topic":"Virat Kohli"})

print(result)