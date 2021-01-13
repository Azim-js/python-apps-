#to read the type and display the key value of .jason file
import json as js

data=js.load(open("data.json"))

print(type(data),"\n")
u_i=input("enter the word: ")
if isinstance(u_i,str):
    for item in data[u_i]:
        print(item)

print("auscultation means:  ",data["auscultation"])