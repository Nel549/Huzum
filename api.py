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

llm = OpenAI(openai_api_key="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")
chat_model = ChatOpenAI()


text = "what is a good name for my pet who is a dog?"

print(chat_model.predict(text))