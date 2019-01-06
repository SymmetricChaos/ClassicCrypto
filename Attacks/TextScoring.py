## Takes the list of bigrams from file and assigns
## a values to each of them based on how common they are.
ngrams1 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\1gramScores.csv', 'r')
ngrams2 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\2gramScores.csv', 'r')
ngrams3 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\3gramScores.csv', 'r')
monograms = {}
bigrams = {}
trigrams = {}

# We use the log probabilities since they are additive
for line in ngrams1:
    L = line.split(" ")
    monograms[L[0]] = int(L[2])

for line in ngrams2:
    L = line.split(" ")
    bigrams[L[0]] = int(L[2])

for line in ngrams3:
    L = line.split(" ")
    trigrams[L[0]] = int(L[2])

def monogramScore(text):
    score = 0
    for i in range(len(text)-1):
        score += monograms[text[i]]
    return score

def bigramScore(text):
    score = 0
    for i in range(len(text)-1):
        score += bigrams[text[i:i+2]]
    return score

def trigramScore(text):
    score = 0
    for i in range(len(text)-1):
        score += trigrams[text[i:i+2]]
    return score