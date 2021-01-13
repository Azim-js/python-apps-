import json

data=json.load(open("data.json"))

def translate(w):
    return(data[w])

u_ip=input("enter the word : ")
print(translate(u_ip))    