import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),cutoff=0.7)) > 0:
        return "did you mean this : %s ?? " %(get_close_matches(w,data.keys())[0])
    else:
        return "please check the word again "

u_ip=input("enter the word : ")
print(translate(u_ip))