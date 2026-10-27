from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt=PromptTemplate(
    template="Generate 5 intresting things about {topic}",
    input_variables=["topic"]
)

model=ChatOllama(model="llama3.2:latest")

parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke({"topic":"cricket"})
print(result)