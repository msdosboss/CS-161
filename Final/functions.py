def GAVW():                                             #GAVW means Get and Verify Word
    x = True
    while x == True:
        word = input()
        if word.isalpha() == True:
            x = False
            return(word)
        print("that is not a word try again")
def GAVT():                                             #GAVT means Get and Verify type
    x = True
    while x == True:
        word = input()
        if word in "wWFfGg":
            x = False
            return(word)
        print("that is not a type try again")
def GAVN():                                             #GAVN means Get and Verify number
    x = True
    while x == True:
        word = int(input())
        if word == 1 or word == 2:
            x = False
            return(word)
        print("that is not a number try again")
def attack(health,attack,armor):
        health = health - (attack - armor) 
        return (health)

def listitem(playerinv):
    print("which item would you like to use")
    y = 1
    for x in playerinv:
        print (y,":",x)
        y = y + 1


def encounter(roomnumber,enemyhealth,playerhealth,enemyattack,playerattack,enemyaromor,playerarmor,enemyname,playerinv,enemyitem):
    print("you have encounterd a ",enemyname)
    while enemyhealth > 0 and playerhealth > 0:
        print("If you would like to attack press 1,If you would like to see your items press 2")
        flag = GAVN()
        if (flag == 1):
            enemyhealth = attack(enemyhealth,playerattack,enemyaromor)
            playerhealth = attack(playerhealth,enemyattack,playerarmor)
            print ("your have",playerhealth,"remaining")
            print ("the enemy has",enemyhealth,"remaining")
        if (flag == 2):
            print("test")                              
            listitem(playerinv)
    if (playerhealth > 0 and enemyhealth < 1):
        playerinv.append(enemyitem)
        roomnumber = roomnumber + 1
        return (playerhealth)
            























#********ITEMS*********** To be added 

def potion(health):
    health = health + 10
    return(health)

def devstick(attack):
    attack = attack + 10000 

def firestick(attack,type):
    if type in "fF":
        attack = attack + 10
        return(attack)

def waterstick(attack,type):
    if type in "Ww":
        attack = attack + 10
        return(attack)

def grassstick(attack,type):
    if type in "Gg":
        attack = attack + 10
        return(attack)