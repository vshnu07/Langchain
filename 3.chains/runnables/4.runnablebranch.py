from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a report on a {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="summarise the following text \n {text}",
    input_variables=["text"]
)

model=ChatOllama(model="llama3.2:latest")
parser=StrOutputParser()

report_gen=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen,branch_chain)

print(final_chain.invoke({"topic":"USA VS IRAN"}))