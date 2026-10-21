from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-3.8-flash")

class Review(TypedDict):
    summary:str
    sentiment:str

structed_model=model.with_structured_output(Review)

result=structed_model.invoke("The product is excellent, with great quality and fast delivery. I am very satisfied with my purchase.")
print(result)