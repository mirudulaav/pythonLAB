#Menu Driven with a Dictionary for words and their meanings
import json
from difflib import get_close_matches
data=json.load(open("dict.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean % s instead? Enter Y if yes, or N if no: "% get_close_matches(w,data.keys())[0])
        yn=yn.lower()
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The Word doesn't exist.Please double check it."
word=input("Enter word: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
       print(output)
input("Press ENTER to exit")
