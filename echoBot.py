import random

print("Wie geht es dir?")
while True:
    
    st = input()
    try:
        strr = st.split() [-1]
        if "fühle" in st or "fuehle" in st or "bin" in st:
            print("Wieso bist du " + strr +"?")
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
        
            