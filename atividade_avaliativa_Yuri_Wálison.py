import requests
from bs4 import BeautifulSoup


url = "https://tribunademinas.com.br/noticias/esportes"

response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

titulo = soup.find_all('h2', class_='title')


    
for t in (titulo):
    print(t.text)
    input()
        
