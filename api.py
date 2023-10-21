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
from langchain import ChatOpenAI
from langchain.prompts import PromptTemplate
llm = OpenAI(openai_api_key="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")

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
prompt.format(product="colorful socks")


chat_model = ChatOpenAI()


text = "what is a good name for my pet who is a dog?"
chat_model.add_message(text)