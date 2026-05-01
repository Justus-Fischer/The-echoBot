import random
import time
word = ["-"] * 4
speed = 0
def gettime(tr):
    tims = (95**len(pas)) / tr
    if tims > 60:
        tims = tims / 60
        if tims > 60:
            tims = tims / 60
            if tims > 24:
                tims = tims / 24
                if tims > 365:
                    tims = tims / 365
                    if tims > 1000:
                        tims = tims / 1000
                        if tims > 1000000000:
                            tims = tims / 1000000000
                            if tims > 1000000:
                                return str("infinitely long")
                            else:
                                return str(str(round(tims,2)) + " trillion years")
                            
                        else:
                            if tims > 1000000:
                                tims = tims / 1000000
                                return str(str(round(tims,2)) + " billion years")
                            else:
                                return str(str(round(tims,2)) + " milenials")
                    else:
                        return str(str(round(tims,2)) + " years")
                else:
                    return str(str(round(tims,2)) + " days")
            else:
                return str(str(round(tims,2)) + " hours")
        else:
            return str(str(round(tims,2)) + " minutes")
    else:
        return str(str(round(tims,2)) + " seconds")
    
    
def bu(num, ausg):
    bword = []
    for i in range(num):
        sp = chr(random.randint(0, 150))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))
    
        bword.append(sp)
    if ausg == 1:    
        print(" ".join(bword))
        
        

        
#chplot(index, letter)
     
        
def simulate(length):
    boost = False
    word_index = [32] * length
    trysd = 0
    while True:

        word = [chr(n) for n in word_index]
        if "".join(word) == pas:
            return str("True " + str(trysd))
            
        
        else:
            trysd = trysd + 1
            if trysd < 50:
                #print("".join(word))
                bu(length,1)
                
            else:
                if boost == False:
                    print("Deactivate output to work faster")
                    boost = True
        
        
        
        word_index[0] = word_index[0] + 1
        if word_index[0] == 127:
            word_index[0] = 128
        
        
        for i in range(length):
            if word_index[i] > 129:
                
                if i == length - 1:
                    return 
                word_index[i] = 32
                word_index[i + 1] = word_index[i + 1] + 1
                if word_index[i] == 127:
                    word_index[i] = 128
                    
            else:
                break        
    
    
    
            
        
        
while True:
    
    print("Type in a password to be tested")
    print("Also test longer and shorter ones to see how the time to find it change")
    #print("(start with short passwords (2-4 characters long))")


    pas = input()
    if speed == 0:
        le = len(pas)
    
    if speed > 0 and ( le != len(pas)):
        print("The length of your password has changed")
        print("Would you like to start a new speed test? [YES/NO]")
        print("(otherwise, the speed is calculated )")
         
        
        if "Y" in input().upper():
            speed = 0

    if speed == 0:
        le = len(pas)
    
    boost = False
    trys = 0
    if speed == 0:
        print("Starting speedtest... (singlecore, duration: 10s)")
        print(" ")
        st = time.time()
        while time.time() - st < 10:
            
            
            trys = trys + 1
        trys = trys / 10
        speed = trys
        speedBL = speed * len(pas)
    else:
        trys = speed
        
    

    print("Your computer manages " +str(f"{speedBL / len(pas):,}" +" attemps per second. (singlecore)"))
    print("At this speed you would need up to " + gettime(trys)  + " to find the password. (singlecore)")
    print("statistically, however, only half the time")
    print(" ")
    time.sleep(5)
    print("But a hacker could find it in " + gettime(100000000000) +".") 
    print(" ")
    print("Would you like to let your computer try to find the password? [YES/NO]")

    if "Y" in input().upper():
        trys = 0
        
        st = time.time()
        while True:
            zs = simulate(len(pas))
            if "True" in zs:
                trys = int(zs[5:])
                break
    
        tg = time.time() - st
        print("Password found after "+ str(f"{trys:,}") +" trys and " + str(round(tg ,2)) + " seconds or "+ str((time.time()-st)//60) + " minutes.")
        
        print(str(f"{(trys / round(tg ,2)):,}"))
        
        print("Do you want to test another password? [YES/NO]")
        if "N" in input().upper():
            break
        
    else:
        print("Do you want to test another password? [YES/NO]")
        if "N" in input().upper():
            break 



