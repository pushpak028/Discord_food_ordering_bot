import json



def load1(file_path):
    with open(file_path,'r') as file:
        data : dict =  json.load(file) 
    return data
def blockwords(message):
    block_words = ["fuck","f*ck","http://","https://"]
    for text in block_words:
        if message.lower() == text.lower():
            return 1
        else:
            return 0

