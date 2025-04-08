import requests

def pobierz_imiona(url):
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
            if 'name' in item: 
                yield item['name']
        
       
        if data['info']['next'] is None:
            break
        
        page += 1 


url = "https://rickandmortyapi.com/api/character"
for name in pobierz_imiona(url):
    print(name)