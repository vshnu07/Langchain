from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())
prompt=PromptTemplate(
    template="Tell me a joke about {topic}",
    input_variables=["topic"]
)

model=ChatOllama(model="llama3.2:latest")

parser=StrOutputParser()

joke_gen=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "word_count":RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_gen,parallel_chain)

print(final_chain.invoke({"topic":"Cricket"}))