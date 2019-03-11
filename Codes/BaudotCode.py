E = {'T': '00001',
    '5': '00001',
    'O': '00011',
    '9': '00011',
    ' ': '00100',
    'H': '00101',
    '$': '00101',
    'N': '00110',
    ',': '00110',
    'M': '00111',
    '.': '00111',
    'L': '01001',
    ')': '01001',
    'R': '01010',
    '4': '01010',
    'G': '01011',
    '&': '01011',
    'I': '01100',
    '8': '01100',
    'P': '01101',
    '0': '01101',
    'C': '01110',
    ':': '01110',
    'V': '01111',
    ';': '01111',
    'E': '10000',
    '3': '10000',
    'Z': '10001',
    '"': '10001',
    'D': '10010',
    'B': '10011',
    '?': '10011',
    'S': '10100',
    'Y': '10101',
    '6': '10101',
    'F': '10110',
    '!': '10110',
    'X': '10111',
    '/': '10111',
    'A': '11000',
    '-': '11000',
    'W': '11001',
    '2': '11001',
    'J': '11010',
    "'": '11010',
    'U': '11100',
    '7': '11100',
    'Q': '11101',
    '1': '11101',
    'K': '11110',
    '(': '11110'
}

D = {'00000' : ["",""],
    '00001' : ["T","5"],
    '00010' : ["CR","CR"],
    '00011' : ["O","9"],
    '00100' : [" "," "],
    '00101' : ["H", "$"],
    '00110' : ["N", ","],
    '00111' : ["M", "."],
    '01000' : ["LF","LF"],
    '01001' : ["L",")"],
    '01010' : ["R","4"],
    '01011' : ["G","&"],
    '01100' : ["I","8"],
    '01101' : ["P","0"],
    '01110' : ["C",":"],
    '01111' : ["V",";"],
    '10000' : ["E","3"],
    '10001' : ["Z",'"'],
    '10010' : ["D","ENC"],
    '10011' : ["B","?"],
    '10100' : ["S","BEL"],
    '10101' : ["Y","6"],
    '10110' : ["F","!"], 
    '10111' : ["X","/"],
    '11000' : ["A","-"],
    '11001' : ["W","2"],
    '11010' : ["J","'"],
    '11011' : ["FS","FS"],
    '11100' : ["U","7"],
    '11101' : ["Q","1"],
    '11110' : ["K","("],
    '11111' : ["LS","LS"]
}



ctrlCodeE = {'CR': '00010',
            'LF': '01000',
            'ENC': '10010',
            'BEL': '10100',
            'FS': '11011',
            'LS': '11111'}

ctrlCodeD = {'00010' : "CR",
             '01000' : "LF",
             '11011' : "FS",
             '11111' : "LS",
             '10010' : "ENC",
             '10100' : "BEL"}


def baudot(text,decode=False):
    if decode == False:
        T = list(text)
        out = []
        # Pop characters from the beginning one by one until none are left
        while len(T) > 0:
            char = T.pop(0)
            # If we get a normal character just encode it
            if char != "\\":
                out.append(E[char])
            # But if we got a \ then we need to find a corresponding control code
            # To do this we keep taking characters until we get a known control code
            # Once we do we encode that
            else:
                ctrl = ""
                while ctrl not in ctrlCodeE:
                    ctrl += T.pop(0)
                out.append(ctrlCodeE[ctrl])
        
        return " ".join(out)
    
    if decode == True:
        out = []
        text = text.split(" ")
        md = 0
        for i in text:
            
            t = D[i][md]

            if t == "FS":
                md = 1
                continue
            
            if t == "LS":
                md = 0
                continue
            
            out.append(t)
            
        return "".join(out)

ptext = "FOX\FS01 \BEL7\LS ABC"
ctext = baudot(ptext)
dtext = baudot(ctext,decode=True)

print(ctext)
print(dtext)