import random
import numpy as np
from PrepareText import preptext1


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

# With 1000 code groups there an absurdly huge number of possible keys. This
# implementation seeds the Mersenne Twister algorithm in order to randomize
# the meaning of the code groups. 

def createCodeGroups(n,decode=False):
    
    # Generate the code groups. Note that there is a space in this so that the
    # code groups will be visibly separated when written out.
    codegroups = ["{0:03} ".format(i) for i in range(1000)]
   
    # Use they key value n to randomize the codegroups in a predictable way
    random.seed(n)
    random.shuffle(codegroups)
    # Now reset the random seed
    random.seed()
    
    
    ## Our list of text symbols is taken from the Ngram data that we have
    ngrams1 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\1grams.csv', 'r')
    ngrams2 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\2grams.csv', 'r')
    ngrams3 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\3grams.csv', 'r')
    ngrams4 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\4grams.csv', 'r')
    
    codeDict = {}
    
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
        
    normalizingFactor = min(codeDict.values())//3
    
    for i in codeDict.items():
        codeDict[i[0]] = int(np.ceil(np.sqrt(i[1]//normalizingFactor)))

    codeDict[">"] = 30
    codeDict["_"] = 63

    if decode == False:
        for i in codeDict.items():
            L = []
            for j in range(i[1]):
                L.append(codegroups.pop())
            codeDict[i[0]] = L
        return codeDict
    

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

            numNulls = len(text)//20

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




#textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\Text2.txt','r')
#ptext = preptext1(textfile.readline())


#KEY = random.getrandbits(64)

#ctext = nomenclator(ptext,KEY)

#decoded = nomenclator(ctext,KEY,decode=True)
#print(decoded)
#print("\n\nDoes the Text Decode Correctly?",decoded == ptext)
