# Zad. 2
# Napisz program, który za pomocą generatora pobierze dane ze stronicowanego API.
# Generator powinien pobierać dane z każdej strony i zwracać je do momentu, aż wszystkie strony zostaną przetworzone.
# Każdy element w danych powinien być zwrócony przez generator.

import requests

def pobierz_dane(url):
    page = 1  
    while True:
        response = requests.get(f"{url}?page={page}") 
        if response.status_code != 200: 
            print(f"Error: {response.status_code} for {url}")  
            break
        
        data = response.json()
        
# Tu wpisz kawałek kodu
#
#
#
        
        page += 1  



url = "https://dog.ceo/dog-api/"  
#Użyj generatora do iteracji po wynikach
#
#
#