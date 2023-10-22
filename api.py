from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

import pinecone

import os
from dotenv import load_dotenv
load_dotenv()

# Set the secret key
secret_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_enviroment_key = os.getenv("PINECONE_ENVIROMENT_KEY")

# Returns:
# ['quickstart'])

pinecone.init(api_key=pinecone_api_key, environment=pinecone_enviroment_key)

# Set the llm and chat models
llm = OpenAI(openai_api_key=secret_key)
chat_models = ChatOpenAI()

