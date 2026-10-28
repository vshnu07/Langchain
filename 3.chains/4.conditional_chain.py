from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough

model = ChatOllama(model="llama3.2:latest", temperature=0)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template=(
        "You are a sentiment classifier.\n"
        "Classify the feedback as positive or negative.\n"
        "If it expresses praise or satisfaction, return positive.\n"
        "If it expresses criticism or dissatisfaction, return negative.\n"
        "Example: 'This is a good smartphone' -> positive\n"
        "Example: 'This is a terrible smartphone' -> negative\n"
        "Return only the category word.\n\n"
        "Feedback: {feedback}"
    ),
    input_variables=["feedback"]
)

classifier_chain = prompt1 | model | parser

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (
        lambda x: x["sentiment"]== "positive",
        prompt2 | model | parser
    ),
    (
        lambda x: x["sentiment"]== "negative",
        prompt3 | model | parser
    ),
    RunnableLambda(lambda x: "Could not determine sentiment")
)

chain = (
    RunnablePassthrough.assign(sentiment=classifier_chain)
    | branch_chain
)

result = chain.invoke({
    "feedback": "This is a bad smartphone"
})

print(result)
