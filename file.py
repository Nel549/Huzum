from api import secret_key

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS

from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.agents import create_csv_agent


import os

from langchain.llms import OpenAI

# secret_key = os.getenv("OPENAI_API_KEY")
# llm = OpenAI(openai_api_key=secret_key)

# reader = PdfReader('data_unstr/1.pdf')

# raw_text = ''
# for i, page in enumerate(reader.pages):
#     text = page.extract_text()
#     if text:
#         raw_text += text


# text_splitter = CharacterTextSplitter(        
#     separator = "\n",
#     chunk_size = 1000,
#     chunk_overlap  = 200,
#     length_function = len,
# )
# texts = text_splitter.split_text(raw_text)
# embeddings = OpenAIEmbeddings()
# docsearch = FAISS.from_texts(texts, embeddings)

# from langchain.chains.question_answering import load_qa_chain

# chain = load_qa_chain(OpenAI(), chain_type="stuff")

# query = "Combien de temps dure la fdv ?"
# docs = docsearch.similarity_search(query)
# m = chain.run(input_documents=docs, question=query)
# print(m)

import fitz  # PyMuPDF
pdf_document = fitz.open('data_unstr/1.pdf')
text = ''

for page in pdf_document:
    text += page.get_text()

pdf_document.close()
  
text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(text)

# print(texts)
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(texts, embeddings)

from langchain.chains.question_answering import load_qa_chain

chain = load_qa_chain(OpenAI(), chain_type="stuff")

query = "Quelle est l’histoire de la FDV ?"
docs = docsearch.similarity_search(query)
m = chain.run(input_documents=docs, question=query)
print(m)


agent = create_csv_agent(OpenAI(temperature = 0), ['data_unstr/TransUPD.csv', 'data_unstr/bathroom_location.csv'] , verbose = True )
# agent = create_csv_agent(OpenAI(temperature = 0), 'data_unstr/bathroom_location.csv' , verbose = True )
agent.run("Je veux l'emplacement de Gare (Nord)")


