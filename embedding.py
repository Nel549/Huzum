from api import secret_key, pinecone_api_key, pinecone_enviroment_key
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
# create a loader
loader = PyPDFLoader("data/FAQ_FDV_Zenko_V1.2.pdf")

# load your data
data = loader.load()

print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[0].page_content)} characters in your document')
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

print (f'Now you have {len(texts)} documents')
from langchain.vectorstores import  Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

embeddings = OpenAIEmbeddings(openai_api_key=secret_key)
index_name = "elix"

docsearch = Pinecone.from_existing_index(index_name, embeddings)



llm = OpenAI(temperature=0, openai_api_key=secret_key, model_name='gpt-3.5-turbo')
chain = load_qa_chain(llm, chain_type="stuff")
input_main = input('Your question is : ')
query = f"{input_main}"
print (f'Your question is : {query}')
docs = docsearch.similarity_search(query)
print(chain.run(input_documents=docs, question=query))