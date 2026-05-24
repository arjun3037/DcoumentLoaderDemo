from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for following PDF document -\n {pdf_doc}',
    input_variables=['pdf_doc']
)

parser = StrOutputParser()

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

#print(chain.invoke({'pdf_doc':docs[0].page_content}))

print(docs[0].page_content)
print(docs[0].metadata)
print(len(docs))