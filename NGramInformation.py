# http://norvig.com/mayzner.html
# Uses Google data
ngrams1 = open('1grams.csv', 'r')
ngrams2 = open('2grams.csv', 'r')
ngrams3 = open('3grams.csv', 'r')
ngrams4 = open('4grams.csv', 'r')
ngrams5 = open('5grams.csv', 'r')
ngrams6 = open('6grams.csv', 'r')
ngrams7 = open('7grams.csv', 'r')
ngrams8 = open('8grams.csv', 'r')
ngrams9 = open('9grams.csv', 'r')

for i in [ngrams2,ngrams3,ngrams4,ngrams5,ngrams6,ngrams7,ngrams8,ngrams9]:
    print(str(i.name),"has length",len(i.readlines()))

print()

# If we don't move the cursors back to the beginning of ngrams2 it would
# still be at the end from having read all the lines previously
ngrams2.seek(0)
for i,line in enumerate(ngrams2):
    L = line.split(",")
    print(L[0],end = " ")
    if (i + 1)%20 == 0:
        print()
print("\n")
        
ngrams1.seek(0)
N = ngrams1.readlines()
letters = [i.split(",")[0] for i in N]
print("".join(letters))