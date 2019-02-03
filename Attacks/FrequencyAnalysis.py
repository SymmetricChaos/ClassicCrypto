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


def frequencyTableExample():
    from Ciphers.UtilityFunctions import preptext
    textfile = open('text1.txt', 'r')
    ptext = preptext(textfile.readline(),silent=True)
    
    print("""
Example of frequency analysis of a body of text. Lets see what the most common
letters are. Then the most common bigrams and trigrams.       
""")
    
    for i,title in zip(range(1,4),["Letters","Bigrams","Trigrams"]):
        print("Most Common {}".format(title))
        tab = frequencyTable(ptext,n=i)
        T = tab[:7]
        for fr in T:
            print(fr[0]," ",fr[1])
        print()
    
#frequencyTableExample()