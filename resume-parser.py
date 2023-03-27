import openai
from flask import request

# Define OpenAI API key 
openai.api_key = "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"


from pyresparser import ResumeParser


def basic_info(file):
    file="data/Abhishek-Bisht-DS.pdf"
    data = ResumeParser(file).get_extracted_data()
    print("Name:" + data['name'])
    print("Email:" + data['email'])
    print("Mobile:" + data['mobile_number'])
    print("Roles:"+ ",".join(data['designation']))
    print("Pages:"+ str(data['no_of_pages']))


def summarize(para):
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

    basic_info(None)
    fp=open("data/resume1.txt")
    text= fp.read()
    summarize(text)

