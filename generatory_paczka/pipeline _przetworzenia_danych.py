
def czytaj(plik):
    with open(plik, 'r', encoding='utf-8') as f:
        for linia in f:
            yield linia


def filtruj(linie):
    for linia in linie:
        if linia.strip():  
            yield linia


def transformuj(linie):
    for linia in linie:
        yield linia.upper() 


def zapisz(linie, plik_wyj):
    with open(plik_wyj, 'w', encoding='utf-8') as f:
        for linia in linie:
            f.write(linia)

plik_wej = 'wejsciowy.txt'  
plik_wyj = 'wyjsciowy.txt' 


linie = czytaj(plik_wej)
przefiltrowane = filtruj(linie)
przeksztalcone = transformuj(przefiltrowane)
zapisz(przeksztalcone, plik_wyj)
