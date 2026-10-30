from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("./Bot-Automation Questions.pdf")

doc=loader.load()

print(len(doc))

print(doc[0].page_content)