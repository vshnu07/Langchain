from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatOllama(model="llama3.2:latest")

prompt=PromptTemplate(
    template="Write a summary of a essay \n {essay}",
    input_variables=["essay"]
)
parser=StrOutputParser()

loader=TextLoader("./cricket.txt",encoding="utf-8")

docs=loader.load()



chain=prompt | model| parser

print(chain.invoke({"essay":docs[0].page_content}))