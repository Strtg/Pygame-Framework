import random

def liczserie():
    seria = 0
    wynik = False
    rekord = 0
    while True:
        # global wynik, seria, rekord
        wynik = random.choice([1, 0])
        # print wynik, seria
        if wynik == 1:
            # print 'wynik 1'
            seria += 1
            # print 'seria', seria
        else:
            if seria > rekord:
                rekord = seria
            print seria, '('+ str(rekord) + ')'
            seria = 0

liczserie()