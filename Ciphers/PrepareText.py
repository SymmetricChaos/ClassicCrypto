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

def playfairPrep(text,mode="IJ"):

    if mode == "IJ":
        text = text.replace("J","I")
    if mode == "CK":
        text = text.replace("C","K")
    if mode == "KQ":
        text = text.replace("Q","K")
        
    # chn just checks if we changed anything
    # At the start of each while loop set it to zero assuming we won't change
    # anything. Then as we step through the text if we find a double letter
    # that might mess up playfair cipher fix it then start from the beginning.
    chn = 1
    while chn == 1:
        
        chn = 0
        for i in range(len(text)//2):
            x = text[i*2:i*2+2]
            if x[0] == x[1]:
                if x[0] != "X":
                    text = text[:i*2] + "X" + text[i*2:]
                    chn = 1
                    break
                else:
                    text = text[:i*2] + "Z" + text[i*2:]
                    chn = 1
                    break
                
    # Make sure the are an even number of letters
    if len(text) % 2 == 1:
        if text[-1] != "Z":
            text += "Z"
        else:
            text += "X"
    return text

    
