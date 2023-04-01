

def gen_questions(para):
        #prompt = "summarize in 10 points: " + para
        prompt = "generate questions from: " + para
        #prompt = "generate multiple choice questions : " + para

        

        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo", 
          messages=[{"role": "user", "content":prompt}]
        )
        #print(completion)
        res=(completion["choices"][0]["message"]["content"])
        print(res)
        data={'result':res}
        #return jsonify(data)
 
