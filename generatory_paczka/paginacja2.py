import requests

def pobierz_strony(url):
    page = 1
    while True:
        response = requests.get(f"{url}?page={page}")
        if response.status_code != 200:
            print(f"Error: {response.status_code} for {url}")
            break
        
        data = response.json()  
        if not data['results']: 
            break
        
        for item in data['results']:
            yield item
        
        page += 1


url = "https://swapi.dev/api/people/"
for person in pobierz_strony(url):
    print(person)
