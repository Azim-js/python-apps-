import json

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    else:
        return "please check the word again"
u_ip=input("enter the word :")

print(translate(u_ip))