from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a tweet about a {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Generate a linkdin post about {topic}",
    input_variables=["topic"]
)

model=ChatOllama(model="llama3.2:latest")

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    "tweet":RunnableSequence(prompt1,model,parser),
    "linkdin":RunnableSequence(prompt2,model,parser)
})

print(parallel_chain.invoke({"topic":"Cricket"}))