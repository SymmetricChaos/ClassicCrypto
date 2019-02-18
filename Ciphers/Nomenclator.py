import random
import numpy as np
from RNG.LFSR import LFSR
from RNG.FisherYates import fisherYatesShuffle

# A nomenclator is a cipher that operates on common pieces of language in order
# to defeat frequency analysis. The Great Cipher designed by Antoine Rossignol
# for the French in the 1600s mostly used syllables. It also has special
# symbols for distinctive words that showed up often like the names of various
# generals. In fact syllables could be written using any of several "code 
# groups". 
# This variant is designed for modern English and rather than syllables it 
# uses common letter groups. So a code group could indicate four letters or
# three or two or one. There are also "nulls" randomly inserted. These symbols
# don't translate to anything and are meannt to be ignored. There is also a
# supernull which means "ignore this character and the character that comes
# immediately after it".
# For every block of letters there are multiple code groups that can represent
# it in order to make frequency analysis even more difficult.


def createCodeGroups(n,decode=False):
    
    # Generate the code groups. Note that there is a space in this so that the
    # code groups will be visibly separated when written out.
    codegroups = ["{0:03} ".format(i) for i in range(1000)]
   
    
    # Use a LFSR to shuffle the code groups
    L = []
    for ctr,val in enumerate(LFSR(n,[5,6,8,9,11,15,19,31],32)):
        L.append(val)
        if ctr == 1000:
            break
    shuf = fisherYatesShuffle(1000,L)
    codegroups = [codegroups[i] for i in shuf]
    
    
    # There are a preposterously huge number of ways to shuffle the one thousand
    # code groups that exist. The 32 bit LFSR only provides about four billion
    # possible shuffles. While it can be operated by hand it isn't entirely
    # reasonable to pick a new key for every message. Fortunately nomenclator
    # type ciphers require a lot of text in order to mount an attack against them
    # and historically only had the key changed very rarely.
    
    # If working by hand isn't necessary a stronger modern algorithm can be used
    # to perform the shuffle.
    #random.seed(n)
    #random.shuffle(codegroups)
    # Now reset the random seed
    #random.seed()
    
    
    ## Our list of text symbols is taken from the Ngram data that we have
    ngrams1 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\1grams.csv', 'r')
    ngrams2 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\2grams.csv', 'r')
    ngrams3 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\3grams.csv', 'r')
    ngrams4 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\4grams.csv', 'r')
    
    codeDict = {}
    
    # Put letters and letter groups into the dictionary with each assigned to
    # a number that reflects how colmmon it is.
    for n,d in enumerate(ngrams1):
        L = d.split(",")
        codeDict[L[0]] = int(L[1])
    
    for n,d in enumerate(ngrams2):
        L = d.split(",")
        codeDict[L[0]] = int(L[1])
        if n > 50:
            break
    
    for n,d in enumerate(ngrams3):
        L = d.split(",")
        codeDict[L[0]] = int(L[1])
        if n > 40:
            break
    
    for n,d in enumerate(ngrams4):
        L = d.split(",")
        codeDict[L[0]] = int(L[1])
        if n > 30:
            break
    
    # Get the raw numbers into something more manageable. This is basically
    # arbitrary and could be done in a lot of ways.
    normalizingFactor = min(codeDict.values())//3
    for i in codeDict.items():
        codeDict[i[0]] = int(np.ceil(np.sqrt(i[1]//normalizingFactor)))
    # Put the supernulls and ordinary nulls into the list
    codeDict[">"] = 30
    codeDict["_"] = 63


    # When encoding we go through the dictionary and replace the number N with
    # the next N code groups in the sorted list.
    # This way we can quickly lookup a sequence of symbols and find all the
    # codegroups that are used for it.
    if decode == False:
        for i in codeDict.items():
            L = []
            for j in range(i[1]):
                L.append(codegroups.pop())
            codeDict[i[0]] = L
        return codeDict
    
    # When decoding we make a new dictionary and for each item in the code
    # dictionary make N new entries from the sorted code groups.
    # This way we can quickly lookup a codegroup and get what it decodes as.
    if decode == True:
        decodeDict = {}
        for i in codeDict.items():
            for j in range(i[1]):
                decodeDict[codegroups.pop()] = i[0]
        return decodeDict
        


def nomenclator(text,key=1,decode=False,usenulls=True,dictionary=False,showgroups=False):
    
    D = createCodeGroups(key,decode)
    if dictionary == True:
        return D

    
    if decode == False:
        codegroups = ["{0:03} ".format(i) for i in range(1000)]
        
        if usenulls == True:

            numNulls = len(text)//25

            ## Insert nulls to break up words
            for i in range(numNulls):
                r = random.randint(0,len(text))
                text = text[:r] + '_' + text[r:]
                
            for i in range(numNulls//3):
                r = random.randint(0,len(text))
                text = text[:r] + '>' + text[r:]
    
        # Replace the nulls
        while "_" in text:
            text = text.replace("_",D["_"][np.random.randint(0,63)],1)
        
        while ">" in text:
            gr = random.choice(codegroups)
            text = text.replace(">",D[">"][np.random.randint(0,30)]+gr,1)
        
        # Starting with the longer ngrams replace 
        for d in [i for i in D.keys() if len(i) == 4]:
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)

        for d in [i for i in D.keys() if len(i) == 3]:
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
            
        for d in [i for i in D.keys() if len(i) == 2]:
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
            
        for d in [i for i in D.keys() if len(i) == 1]:
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
        
         
        return text
    
    if decode == True:
        X = text.split(" ")
        X.pop()

        for pos,gr in enumerate(X):
            X[pos] = D[gr+" "]

        # Mainly for debugging but also illustrative if you want to see how a
        # given text translates directly into code groups.
        if showgroups == True:
            return X

        while ">" in X:
            pos = X.index(">")
            X[pos:pos+2] = ""

        while "_" in X:
            pos = X.index("_")
            X[pos] = ""

            
        return "".join(X)


def nomenclatorExample():
    
    from Ciphers.UtilityFunctions import preptext

    print("Example of the Nomenclator Cipher")

    textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\Text2.txt','r')
    ptext = preptext(textfile.readline(),silent=True)
    ptext = ptext[:200]
    
    #KEY = random.getrandbits(32)
    KEY = 3664080377
    
    ctext = nomenclator(ptext,KEY)
    dtext = nomenclator(ctext,KEY,decode=True)
    
    print("Plaintext is:\n{}\n\n".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))

    print("\n\nDoes the Text Decode Correctly?",dtext == ptext)

def PrintCodes(n,decode=False):
    
    D = createCodeGroups(n,decode=decode)
    
    if decode == False:
        for i,j in sorted(D.items()):
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and len(i) == 1:
                S = i + ": "
                for ctr,grp in enumerate(j,1):
                    S += grp
                    if ctr % 7 == 0 and grp != j[-1]:
                        S += "\n   "
                yield S
    
        for L in [2,3,4]:
            for i,j in sorted(D.items()):
                if len(i) == L:
                    S = i + ": "
                    for ctr,grp in enumerate(j,1):
                        S += grp
                        if ctr % 7 == 0 and grp != j[-1]:
                            S += "\n   " + " "*(L-1)
                    yield S
    
        S = "_: "
        for ctr,grp in enumerate(D["_"],1):
            S += grp
            if ctr % 7 == 0 and grp != j[-1]:
                S += "\n   "
        yield S
        
        S = ">: "
        for ctr,grp in enumerate(D[">"],1):
            S += grp
            if ctr % 7 == 0 and grp != j[-1]:
                S += "\n   "
        yield S
        
    if decode == True:
        ctr = 0
        S = ""
        for i,j in sorted(D.items()):
            if ctr % 3 == 0 and ctr != 0:    
                yield S
                S = ""
            S += "{}{:<4}  ".format(i,j)
            ctr += 1

#nomenclatorExample()
for i in PrintCodes(1,decode=True):
    print(i)
