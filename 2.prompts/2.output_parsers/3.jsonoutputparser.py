from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
model=ChatOllama(model="llama3.2:latest")
parser=JsonOutputParser()


templete=PromptTemplate(
    template="Give me a name,age and a city of a fictional character \n {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain=templete| model| parser

result=chain.invoke({})
print(result)