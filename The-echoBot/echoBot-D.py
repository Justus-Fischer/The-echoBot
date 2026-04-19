import random

def kor(tex):
    taul = {
        "bin" : "bist",
        "mich" : "dich",
        "mir" : "dir",
        "ich" : "du",
        "fühle" : "fühlst",
        "fuehle" : "fühlst",
        "möchte" : "willst",
        "moechte" : "willst",
        "brauche" : "brauchst";
        "werde" : "wirst";
    }
    sen = ["weil"]
    wo = tex.split() # .lower()?
    erg = [taul.get(w, w) for w in wo if w not in sen]
    return " ".join(erg)

print("Hallo ich bin Echo")
print("Wie geht es dir?")
while True:
    
    st = str(input())
    try:
        strr = st.split() [-1]
        if "fühle" in st or "fuehle" in st:
            if "fühle" in st:
                if "weil" in st:
                    tre = st.split("fühle") [0].strip()
                    print("Warum fühlst " + kor(tre) + "?")
                else:
                    stre = st.split("fühle") [-1].strip()
                    print("Warum fühlst du " + kor(stre) + "?")
                    
            if "fuehle" in st:
                if "weil" in st:
                    tre = st.split("fuehle") [0].strip()
                    print("Warum fühlst " + kor(tre) + "?")
                else:
                    stre = st.split("fuehle") [-1].strip()
                    print("Warum fühlst du " + kor(stre) + "?")
                
                
                
        elif "möchte" in st or "moechte" in st:
            if "möchte" in st:
                if "weil" in st:
                    tre = st.split("möchte") [0].strip()
                    print("Warum willst " + kor(tre) + "?")
                else:
                    stre = st.split("möchte") [-1].strip()
                    print("Warum möchtest du " + kor(stre) + "?")
                    
            if "moechte" in st:
                if "weil" in st:
                    tre = st.split("moechte") [0].strip()
                    print("Warum möchtest " + kor(tre) + "?")
                else:
                    stre = st.split("moechte") [-1].strip()
                    print("Warum möchtest du " + kor(stre) + "?")
        
        
        elif "bin" in st:
            if "weil" in st:
                tre = st.split("bin") [0].strip()
                print("Warum bist du " + kor(tre) + "?")
            else:
                stre = st.split("bin") [-1].strip()
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