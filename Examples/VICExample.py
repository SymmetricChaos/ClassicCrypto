from Ciphers import VIC

def VICExample():

    ptext = "WEAREPLEASEDTOHEAROFYOURSUCCESSINESTABLISHINGYOURFALSEIDENTITY.YOUWILLBESENTSOMEMONEYTOCOVEREXPENSESWITHINAMONTH."
    K = ["77651","74177","IDREAMOFJEANNIEWITHT",12]
    ctext = VIC(ptext,K)
    dtext = VIC(ctext,K,decode=True)
    print(ptext)
    print()
    print(ctext)
    print()
    print(dtext)
    
VICExample()