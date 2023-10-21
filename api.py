#import openai

#openai.api_key = "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"

#Mesajul care e trimis catre chat-gpt
#message = "give me a hi five"

#request = openai.ChatCompletion.create(
 #   model = "gpt-3.5-turbo",
  #  messages = [
    #    {
   #        "role": "user",
    #        "content": message
     #   }
   # ]
   # )

#raspunsul lui chat gpt
#response = request['choices'][0]['message']['content']

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY")  # Replace "API_KEY" with the name of your API key variable in .env file




chat_model = ChatOpenAI()


