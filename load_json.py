import json



def load1(file_path):
    with open(file_path,'r') as file:
        data : dict =  json.load(file) 
    return data


