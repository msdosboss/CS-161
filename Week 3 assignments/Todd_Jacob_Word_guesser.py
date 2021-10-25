def GAVW():                                             #GAVW means Get and Verify Word
    x = True
    while x == True:
        word = input()
        if word.isalpha() == True:
            x = False
            return(word)
        print("that is not a word try again")
def GAVL():                                             #GAVL means Get and Verify letter
    x = True
    while x == True:
        word = input()
        if word.isalpha() == True and len(word) == 1:
            x = False
            return(word)
        print("that is not a single letter try again")


def GTW(word):                                                 #GTW means Guess the Word
    w = True
    while (w == True):
        print("what do you think the secret word is?")
        y = GAVW()
        if word == y:
            print("you have won")
            w = False
        else:
            wordlength = len(word)
            print(wordlength)
            flag = 0
            while wordlength > flag:
                if y[flag] == word[flag]:
                    print(y[flag])
                else:
                    print("*")
                flag = flag + 1


def GTL(word):
    w = True
    z = ""
    attempt = 0 
    while attempt < 6:
        print("What letter are you going to guess?")
        wrong = 0 
        for x in word:
            if x in z:
                print(x)
            else:
                print("*")
                wrong = wrong + 1
        flag = True
        if wrong == 0:
            print ("you win")
            return
        while flag == True:
            y = GAVL()
            if y not in word:
                print("wrong")
                attempt = attempt + 1
            else:
                flag = False
        z = y + z



def main():
    print("what is the secret word")
    x = GAVW()
    GTL(x)

if __name__=="__main__":
    main()