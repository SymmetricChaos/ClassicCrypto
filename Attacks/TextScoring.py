## Takes the list of bigrams from file and assigns
## a values to each of them based on how common they are.
ngrams2 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\2gramScores.csv', 'r')
ngrams3 = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\NGrams\\3gramScores.csv', 'r')
bigrams = {}
trigrams = {}

# Select the log probabilities from the file
for line in ngrams2:
    L = line.split(" ")
    bigrams[L[0]] = int(L[2])

for line in ngrams3:
    L = line.split(" ")
    bigrams[L[0]] = int(L[2])

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
