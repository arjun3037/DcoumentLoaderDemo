from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

Prompt = PromptTemplate(
    template='Write a summary for following web document -\n {web_doc}',
    input_variables=['web_doc']
)

parser = StrOutputParser()



url = 'https://www.amazon.in/gp/aw/d/817992162X/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=180c223c131500d87dabe946a80a1e43&hsa_cr_id=5099793710102&qid=1779602775&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&aref=BVUKL696W2&ref_=sbx_s_sparkle_sbtcd_asin_0_title&pd_rd_w=Expml&content-id=amzn1.sym.9269eab1-ae85-443b-9ec2-b2fa4ebaad05%3Aamzn1.sym.9269eab1-ae85-443b-9ec2-b2fa4ebaad05&pf_rd_p=9269eab1-ae85-443b-9ec2-b2fa4ebaad05&pf_rd_r=X127NCEBV39ECNBJKH7S&pd_rd_wg=xRjCI&pd_rd_r=dedfc500-5d38-4aaf-a758-f4479b28fb53'

loader = WebBaseLoader(url)

docs = loader.load()
 
print(len(docs))
print(type(docs))
#print(docs[0].page_content)



chain = Prompt | model | parser

print(chain.invoke({'web_doc':docs[0].page_content}))