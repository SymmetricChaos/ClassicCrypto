import re

def preptext1(text):
    print("REMOVING SPACES")
    print("REMOVING NON-ALPHANUMERIC CHARACTERS")
    print("DIGITS REPLACED WITH NAMES")
    T = re.sub(r'[^a-zA-Z0-9]', '', text)
    for i,j in zip(range(10),["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]):
        T = re.sub(r'[{}]'.format(i), j, T)
    T = T.upper()
    return T

def preptext2(text):
    print("REMOVING SPACES")
    print("REMOVING NON-ALPHANUMERIC CHARACTERS")
    T = re.sub(r'[^a-zA-Z0-9]', '', text)
    T = T.upper()
    return T

def preptext3(text):
    print("REMOVING NON-ALPHANUMERIC CHARACTERS")
    T = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    T = T.upper()
    return T

def playfairPrep(text):

    chn = 0
    while chn == 0:
        chn = 1
        for i in range(len(text)//2):
            x = text[i*2:i*2+2]
            if x[0] == x[1]:
                if x[0] != "X":
                    text = text[:i*2] + "X" + text[i*2:]
                    chn = 0
                    break
                else:
                    text = text[:i*2] + "Q" + text[i*2:]
                    chn = 0
                    break
    return text