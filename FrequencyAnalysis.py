from collections import Counter

def frequencyTable(text,n=1):
    if n == 1:
        D = Counter(text)

    else:
        L = []
        for i in range(len(text)-(n-1)):
            L.append(text[i:i+n])
        D = Counter(L)

    return D.most_common()


def FrequecyAnalysisTest():
    from Monoalphabetic import substitution
    from PrepareText import preptext1
    textfile = open('text1.txt', 'r')
    ptext = preptext1(textfile.readline())
    
    ctext = substitution(ptext,"ZEBRA")
    for i in frequencyTable(ctext,2)[:5]:
        print(i)
    print()
    for i in frequencyTable(ctext,1)[:5]:
        print(i)
    
    dtext = ctext
    #ctext = ctext.replace("SFA","the")
    #ctext = ctext.replace("GLD","ing")
    for i,j in zip("SF","th"):
        dtext = dtext.replace(i,j)
    for i,j in zip("A","e"):
        dtext = dtext.replace(i,j)
    
    print(ptext[:63])
    print(ctext[:63])
    print(dtext[:63])
    
    
