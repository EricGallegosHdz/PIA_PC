import re
import requests
from bs4 import BeautifulSoup as bs

def buscadorInfo(page):
    pg = requests.get(page) 
    try:
        regex = r'www.youtube.com/\w+/\w+'
        y = re.findall(regex, pg.text)
    except:
        print("error")
    return(y)   

def buscadorInfo2 (page):
    pg = requests.get(page)
    try:
        regex = r'\d{2} de \w+ de \d{4}'
        y = re.findall(regex, pg.text)
    except:
        print("error")
    return(y)

def buscadorInfo3 (page):
    pg = requests.get(page)
    regex = r'@werever\w+'
    y = re.findall(regex, pg.text)
    return(y)
