# Napisz program, który za pomocą iteratora odczytuje linie z pliku logów.
# Program powinien:
# - Liczyć, ile razy występuje data i godzina w formacie "YYYY-MM-DD HH:MM:SS" w pliku,
# - Wydrukować wszystkie linie, które zawierają daty w tym formacie.
# Wykorzystaj iterator do odczytu pliku linia po linii.

import re

class LogLineIterator:
    def __init__(self, filepath):
         self.file = open(filepath, 'r')   

    def __iter__(self):
        return self

    def __next__(self):
        pass    # Tu zamiast pass wpisz kawałek kodu 
                #
                #
                
def process_logs(filepath):
    

    date_count = 0
    date_lines = []
 
    date_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' # Wyrażenie regularne do dopasowania daty w formacie YYYY-MM-DD HH:MM:SS
# Tu  wpisz kawałek kodu
#
#    
    
    
    for line in iterator:

        pass    #Tu zamiast pass wpisz kawałek kodu
                #
                #
    print(f"Liczba dat: {date_count}")
    print("Linie z datami:")
    for date_line in date_lines:
        print(date_line)

if __name__ == "__main__":
    filepath = "log2.txt"  
    process_logs(filepath)  