import requests
from bs4 import BeautifulSoup


class scrappingService:
    def GetInfo(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        parrafos = soup.find_all('p')
        # Unir todos los párrafos en un solo string
        resultado = ''
        for parrafo in parrafos:
            resultado += parrafo.text + ' '
        return resultado.strip()