import openai
from flask import request

# Define OpenAI API key 
openai.api_key =  # TRUNCATED




def summarize(para):
        prompt = "summarize in 5 lines: " + para
          



        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo", 
          messages=[{"role": "user", "content":prompt}]
        )
        #print(completion)
        res=(completion["choices"][0]["message"]["content"])
        #print(res)
         
        return res

