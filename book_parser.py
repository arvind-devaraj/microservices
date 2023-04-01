import fitz # install using: pip install PyMuPDF

 

import json,sys

output = {}

#book="jesc101"
file_name=sys.argv[1]

doc = fitz.open(f"books/{file_name}.pdf") 
text = ""
for idx,page in enumerate(doc):
    text = page.get_text()
    #text=process(text)
    print(text)
    key=file_name+str(idx)
    output[key]=text


fp = open(f"data/{file_name}.json","w")
json.dump(output,fp,indent=4)

