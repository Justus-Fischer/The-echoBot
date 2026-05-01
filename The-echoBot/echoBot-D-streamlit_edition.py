import streamlit as strem
import random


strem.title("The echoBot")
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
        "brauche" : "brauchst",
        "werde" : "wirst",
    }
    sen = ["weil"]
    wo = tex.split() # .lower()?
    erg = [taul.get(w, w) for w in wo if w not in sen]
    return " ".join(erg)

#print("Hallo ich bin Echo")
#print("Wie geht es dir?")

    
if "messages" not in strem.session_state:
    strem.session_state.messages  = []
        
for message in strem.session_state.messages:
        
    with strem.chat_message(message["role"]):
        strem.markdown(message["content"])
    
    #st = str(input())


    
if st := strem.chat_input("Beschreibe was du gerade fühlst"):
        
    strem.session_state.messages.append({"role": "user", "content": st})
    with strem.chat_message("user"):
        strem.markdown(st)
    start = False
            

try:
    strr = st.split() [-1]
    if "fühle" in st or "fuehle" in st:
        if "fühle" in st:
            if "weil" in st:
                tre = st.split("fühle") [0].strip()
                ant = str("Warum fühlst " + kor(tre) + "?")
                    #print("Warum fühlst " + kor(tre) + "?")
            else:
                stre = st.split("fühle") [-1].strip()
                ant = str("Warum fühlst du " + kor(stre) + "?")
                    
        if "fuehle" in st:
            if "weil" in st:
                tre = st.split("fuehle") [0].strip()
                ant = str("Warum fühlst " + kor(tre) + "?")
            else:
                stre = st.split("fuehle") [-1].strip()
                ant = str("Warum fühlst du " + kor(stre) + "?")
                
                
                
    elif "möchte" in st or "moechte" in st:
        if "möchte" in st:
            if "weil" in st:
                tre = st.split("möchte") [0].strip()
                ant = str("Warum willst " + kor(tre) + "?")
            else:
                stre = st.split("möchte") [-1].strip()
                ant = str("Warum möchtest du " + kor(stre) + "?")
                    
        if "moechte" in st:
            if "weil" in st:
                tre = st.split("moechte") [0].strip()
                ant = str("Warum möchtest " + kor(tre) + "?")
            else:
                stre = st.split("moechte") [-1].strip()
                ant = str("Warum möchtest du " + kor(stre) + "?")
        
        
    elif "bin" in st:
        if "weil" in st:
            tre = st.split("bin") [0].strip()
            ant = str("Warum bist du " + kor(tre) + "?")
        else:
            stre = st.split("bin") [-1].strip()
            b = kor(stre)
            ant = str("Warum bist du " + b + "?")
            
                
                
        
        
            
    else:
        we = random.randint(0, 4)
        
        if we == 0:
            ant = str("Erzähl mir mehr")
        elif we == 1:
            ant = str("Warum?")
        elif we == 2:
            ant = str("Bist du dir sicher?")
        elif we == 3:
            ant = str("Wieso denkst du das?")
        else:
            ant = str("Wenn du daran denkst - was kommt dir dann noch in den Kopf?")
                
        
        
                
except:
    ant = str("")
        
response = ("Echo: " + str(ant))
    
with strem.chat_message("assistant"):
    strem.markdown(response)
        
strem.session_state.messages.append({"role": "user", "content": st})
strem.session_state.messages.append({"role": "assistant", "content": ant})