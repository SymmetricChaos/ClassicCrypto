def vigenere(text,key,decode=False):

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
        "Q","R","S","T","U","V","W","X","Y","Z"]
    T = []
    kLen = len(key)
    
    # convert the keys to lists of numbers
    K = []
    
    for i in key:
        K.append(alphabet.index(i))
    

    for ind,let in enumerate(text):
        N = alphabet.index(let)

        if decode == False:
            N = (N+K[ind%kLen])%26
        else:
            N = (N-K[ind%kLen])%26
        
        T.append(N)
        
    for t in range(len(T)):
        T[t] = alphabet[T[t]]
        
    return "".join(T)

def multiVigenere(text,keys=["A"],decode=False):
    
    ctext = text
    for i in keys:
        ctext = vigenere(ctext,i,decode=decode)
    
    return ctext

def vigenereAutokey(text,key,decode=False):

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
        "Q","R","S","T","U","V","W","X","Y","Z"]
    T = []
    
    # convert the keys to lists of numbers
    K = []
    
    for i in key:
        K.append(alphabet.index(i))
    
    if decode == False:
        for i in text:
            K.append(alphabet.index(i))

    for ind,let in enumerate(text):
        N = alphabet.index(let)

        if decode == False:
            N = (N+K[ind])%26
        else:

            N = (N-K[ind])%26
            K.append(N)

            
        T.append(N)
        
    for t in range(len(T)):
        T[t] = alphabet[T[t]]
        
    return "".join(T)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def affineVigenere(text,key1,key2,decode=False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"
    T = []
    kLen1 = len(key1)
    kLen2 = len(key2)
    
    if "#" in key2:
        raise Exception('cannot use # symbol in multiplicative key')
    
    # convert the keys to lists of numbers
    K1, K2, = [],[]
    for i in key1:
        K1.append(alphabet.find(i))
    
    for i in key2:
        K2.append(alphabet.find(i))

    for ind,let in enumerate(text):
        N = alphabet.index(let)

        if decode == False:
            N = (N+K1[ind%kLen1])%37
            N = (N*(K2[ind%kLen2]+1))%37
        else:
            inv = modinv(K2[ind%kLen2]+1,37)
            N = (N*inv)%37
            N = (N-K1[ind%kLen1])%37
        
        T.append(N)
    
    for t in range(len(T)):
        T[t] = alphabet[T[t]]
        
    return "".join(T)