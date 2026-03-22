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

print("Hello I'm Echo / Hallo ich bin Echo")
print("Please choose your language / Bitte wähle deine Sprache")
print("Please type in: / Bitte gebe ein: [English/Deutsch]")
spr = input().upper()
if "DE" in spr:

    print("Wie geht es dir?")
    while True:
    
        st = str(input())
        try:
            strr = st.split() [-1]
            if "fühle" in st or "fuehle" in st:
                if "weil" in st:
                    tre = st.split("fühle") [0].strip()
                    print("Warum fühlst " + kor(tre) + "?")
                else:
                    stre = st.split("fühle") [-1].strip()
                    print("Warum fühlst du " + kor(stre) + "?")
        
        
            elif "bin" in st:
                if "weil" in st:
                    tre = st.split("bin") [0].strip()
                    print("Warum bist du " + kor(tre) + "?")
                else:
                    stre = st.split("bin") [-1].strip()
                    print("Warum bist du " + kor(stre) + "?")
            
            else:
                if "gut" in st:
                    print("Super! Was fühlst du sonst noch?")
                    continue
                
                alt = ["Erzähl mir mehr", "Warum?", "Bist du dir sicher?", "Wieso denkst du das?",
                       "Wenn du daran denkst - was kommt dir dann noch in den Kopf?"]
                
                print(random.choice(alt))
                
        except:
            print("")
            
else:
    print("Please wait - your language will be available soon")
        
            