import openai

openai.api_key = "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"

#Mesajul care e trimis catre chat-gpt
message = "give me a hi five"

request = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "user",
            "content": message
        }
    ]
    )

#raspunsul lui chat gpt
response = request['choices'][0]['message']['content']

