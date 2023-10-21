from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

# Set the secret key
secret_key = os.getenv("OPENAI_SECRET_KEY")

# Set the llm and chat models
llm = OpenAI(openai_api_key=secret_key)
chat_models = ChatOpenAI()

