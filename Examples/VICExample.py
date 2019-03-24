from Ciphers import VIC

def VICExample():

    ptext = "WEAREPLEASEDTOHEAROFYOURSUCCESSINESTABLISHINGYOURFALSEIDENTITY.YOUWILLBESENTSOMEMONEYTOCOVEREXPENSESWITHINAMONTH."
    ctext = VIC(ptext,["77651","74177","IDREAMOFJEANNIEWITHT",12])
    dtext = VIC(ctext,["77651","74177","IDREAMOFJEANNIEWITHT",12],decode=True)
    print(ptext)
    print()
    print(ctext)
    print()
    print(dtext)
    
VICExample()