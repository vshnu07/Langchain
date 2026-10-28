from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Tell me a joke about {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Explain the joke in details {text}",
    input_variables=["text"]
)

model=ChatOllama(model="llama3.2:latest")

parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({"topic":"movie"}))