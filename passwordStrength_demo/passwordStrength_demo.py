import random
import time
word = []
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
    
    
def bu(num):
    for i in range(num):
        sp = chr(random.randint(0, 150))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))
    
        word.append(sp)
        
        

        
        
    
    
    
            
        
        
while True:
    
    print("Type in a password to be tested")
    print("Also test longer and shorter ones to see how the time to find it change")
    #print("(start with short passwords (2-4 characters long))")


    pas = input()


    
    boost = False
    trys = 0
    if speed == 0:
        print("Starting speedtest... (singlecore, duration: 10s)")
        print(" ")
        st = time.time()
        while time.time() - st < 10:
            bu(len(pas))
            if "".join(word) == "§":
                print("Unexpected ERROR - please restart")
                break
            word = []
            trys = trys + 1
        trys = trys / 10
        speed = trys
    else:
        trys = speed

    print("Your computer manages " +str(f"{trys:,}" +" attemps per second. (singlecore)"))
    print("At this speed you would need up to " + gettime(trys)  + " to find the password. (singlecore)")
    print("statistically, however, only half the time")
    print(" ")
    time.sleep(5)
    print("But a hacker could find it in " + gettime(100000000000) +".")
    print(" ")
    print("Would you like to let your computer try to find the password? [YES/NO]")

    if "Y" in input().upper():
        trys = 0
        fi = False
        st = time.time()
        while fi == False:
            bu(len(pas))
            if "".join(word) == pas:
                break
            else:
                trys = trys + 1
                if trys < 500:
                    print("".join(word))
                else:
                    if boost == False:
                        print("Deactivate output to work faster")
                        boost = True
                word = []
        
        print("Password found after "+ str(f"{trys:,}") +" trys and " + str(time.time() - st) + " seconds or "+ str((time.time()-st)//60) + " minutes.")
        print("Do you want to test another password? [YES/NO]")
        if "N" in input().upper():
            break
        
    else:
        print("Do you want to test another password? [YES/NO]")
        if "N" in input().upper():
            break 


