import random

def kor(tex):
    taul = {
        "bin" : "bist",
        "mich" : "dich",
        "mir" : "dir",
        "ich" : "du",
        "fühle" : "fühlst",
        "fuehle" : "fühlst"
    }
    sen = ["weil"]
    wo = tex.split() # .lower()?
    erg = [taul.get(w, w) for w in wo if w not in sen]
    return " ".join(erg)


print("Wie geht es dir?")
while True:
    
    st = str(input())
    try:
        strr = st.split() [-1]
        if "fühle" in st or "fuehle" in st:
            stre = st.split("fühle") [-1].strip()
            print("Warum fühlst du " + kor(stre) + "?")
            
        elif "bin" in st:
            stre = st.split("ich bin") [-1].strip()
            print("Warum bist du " + kor(stre) + "?")
            
        else:
            we = random.randint(0, 4)
        
            if we == 0:
                print("Erzähl mir mehr")
            elif we == 1:
                print("Warum?")
            elif we == 2:
                print("Bist du dir sicher?")
            elif we == 3:
                print("Wieso denkst du das?")
            else:
                print("Wenn du daran denkst - was kommt dir dann noch in den Kopf?")
                
    except:
        print("")
        
            