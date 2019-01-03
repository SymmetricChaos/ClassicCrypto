from UtilityFunctions import groups

def playfairCipher(text):
    if len(text) % 2 == 1:
        text += "X"
    G = groups(text,2)
    for i in G:
        if i[0] == i[1]:
            print("!")
    print(G)

playfairCipher("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGJAZZ")