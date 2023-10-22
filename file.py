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

embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(texts, embeddings)

from langchain.chains.question_answering import load_qa_chain

chain = load_qa_chain(OpenAI(), chain_type="stuff")
input_main = input('Your question is : ')
query = f"{input_main}"
docs = docsearch.similarity_search(query)
m = chain.run(input_documents=docs, question=query)
print(m)

agent = create_csv_agent(OpenAI(temperature = 0), ['data_unstr/TransUPD.csv', 'data_unstr/bathroom_location.csv'] , verbose = True )
# agent = create_csv_agent(OpenAI(temperature = 0), 'data_unstr/bathroom_location.csv' , verbose = True )
agent.run("Je veux l'emplacement de Gare (Nord)")


