import re

def preptext(text):
    T = re.sub(r'[^a-zA-Z0-9]', '', text)
    for i,j in zip(range(10),["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]):
        T = re.sub(r'[{}]'.format(i), j, T)
    T = T.upper()
    return T

def preptextwithnums(text):
    T = re.sub(r'[^a-zA-Z0-9]', '', text)
    T = T.upper()
    return T