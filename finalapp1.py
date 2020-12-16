import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]    
    elif len(get_close_matches(w,data.keys(),cutoff=0.7))>0:
        yn=input("did you mean this : %s instead ? press y for yes and n for no: " %get_close_matches(w,data.keys())[0])
        print(yn)
        if yn=="Y" or yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N" or yn=="n":
            return "please check your word !"
        else:
            return "didn't understand the query !"
    else:
        return "please ckech the word !"
while True:
    u_ip=input("enter the word: ")
    if u_ip=="\end":
        break
    output=translate(u_ip)
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output)        