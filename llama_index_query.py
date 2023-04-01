
from gpt_index import GPTSimpleVectorIndex

# load from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')

print(index.query("what is a periodic table?"))
