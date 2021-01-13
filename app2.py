import json

data=json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return "please check the word "

u_ip=input("enter the word : ")

print(translate(u_ip))