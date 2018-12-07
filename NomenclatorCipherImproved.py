import random
import numpy as np
from PrepareText import preptext

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def createCodeGroups(n,decode=False):
    
    # Use they key value n to randomize the codegroups in a predictable way
    codegroups = ["{0:03} ".format(i) for i in range(1000)]
    random.seed(n)
    random.shuffle(codegroups)
    # Now reset the random seed
    random.seed()
    
    
    ## Our list of text symbols is taken from the Ngram data that we have
    ngrams1 = open('1grams.csv', 'r')
    ngrams2 = open('2grams.csv', 'r')
    ngrams3 = open('3grams.csv', 'r')
    ngrams4 = open('4grams.csv', 'r')
    
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

    codeDict["<"] = 18
    codeDict[">"] = 18
    codeDict["_"] = 57

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
        


def nomenclator(text,key=1,decode=False):

    D = createCodeGroups(key,decode)
    
    ngrams1 = open('1grams.csv', 'r')
    ngrams2 = open('2grams.csv', 'r')
    ngrams3 = open('3grams.csv', 'r')
    ngrams4 = open('4grams.csv', 'r')
    ngrams4.seek(0)
    ngrams3.seek(0)
    ngrams2.seek(0)
    ngrams1.seek(0)
    
    if decode == False:
    
        ## Insert nulls to break up words
        for i in range(len(text)//11):
            r = random.randint(0,len(text))
            text = text[:r] + '_' + text[r:]
        #for i in range(len(text)//35):
        #    r = random.randint(0,len(text))
        #    text = text[:r] + '<' + text[r:]
        #for i in range(len(text)//35):
        #    r = random.randint(0,len(text))
        #    text = text[:r] + '>' + text[r:]
    
        while "_" in text:
            text = text.replace("_",D["_"][np.random.randint(0,53)],1)
        #while "<" in text:
        #    text = text.replace("<",D["<"][np.random.randint(0,30)],1)
        #while ">" in text:
        #    text = text.replace(">",D[">"][np.random.randint(0,30)],1)

        for n,d in enumerate(ngrams4):
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
            if n > 30:
                break

        for n,d in enumerate(ngrams3):
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
            if n > 40:
                break
            
        for n,d in enumerate(ngrams2):
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
            if n > 50:
                break
            
        for n,d in enumerate(ngrams1):
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
 
        return text,D
    
    if decode == True:
        for T in D.items():
            while T[0] in text:
                text = text.replace(T[0],D[T[0]])
        while "_" in text:
            text = text.replace("_","")
        return text,D
            


textfile = open('text2.txt', 'r')
ptext = preptext(textfile.readline())

KEY = random.getrandbits(64)

ctext,D = nomenclator(ptext,KEY)
print(ctext)

decoded,D = nomenclator(ctext,KEY,decode=True)
print("\n\nDoes the Text Decode Correctly?",decoded == ptext)
#print(decoded)
