import requests

def testuj_api(lista_url):
    for url in lista_url:
        try:
            response = requests.get(url)
            if response.status_code != 200:
                yield url, response.status_code  
            else:
                yield url, "200 OK"  #status 200 oznacza sukces
        except requests.exceptions.RequestException as e:
            yield url, f"Błąd połączenia: {e}" 


lista_url = [
    "https://dog.ceo/api/breeds/image/random",  
    "https://jsonplaceholder.typicode.com/posts",   
    "https://nonexistentwebsite.com",  #niedziałający URL
]

for url, status in testuj_api(lista_url):
    print(f"url: {url}, status: {status}")



