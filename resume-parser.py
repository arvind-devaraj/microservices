import fitz 
import json
from flask import request

import openai

openai.api_key = "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"


from pyresparser import ResumeParser

def parse_pdf(file_name):
    with fitz.open(file_name) as doc:
        text = ""
        for idx,page in enumerate(doc):
            text+= page.get_text()
        
        return(text)
        

def basic_info(file):
    data = ResumeParser(file).get_extracted_data()
    print("Name:" + data['name'])
    print("Email:" + data['email'])
    print("Mobile:" + data['mobile_number'])
    print("Roles:"+ ",".join(data['designation']))
    print("Pages:"+ str(data['no_of_pages']))



def summarize(file):
        text= parse_pdf(file)

        #prompt = "summarize in 10 points: " + para
        
        prompt = "extract entities like skills, companies, tools, education, city : " + para





        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo", 
          messages=[{"role": "user", "content":prompt}]
        )
        #print(completion)
        res=(completion["choices"][0]["message"]["content"])
        print(res)
    



if __name__ == "__main__":

    
    basic_info(file)
    summarize(file)

