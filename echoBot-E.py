import random

def kor(tex):
    taul = {
        "am" : "are",
       
    }
    sen = ["cause"]
    wo = tex.split() # .lower()?
    erg = [taul.get(w, w) for w in wo if w not in sen]
    return " ".join(erg)

print("Hallo I'm Echo")
print("How are you?")