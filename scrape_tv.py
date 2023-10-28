# Location: C:\Users\Kin\All_programming_projects\VSCode projects\discord bot
#scrape_tv.py

# Updated location: 

import requests
from bs4 import BeautifulSoup as bs
import os
import io

# 1. Get the 


def load_dynamic_page_locally(direct):
    print(direct)
    file: io.TextIOWrapper = open(direct, "r", encoding="utf-8")
    print(type(file))
    return file


def parse_soup(soup, tag, tagname):
    soup.find_all(tag,tagname)
    cards = soup.find_all('a','tv-pine-reference-toc-item')

    result = {}

    for elt in cards:
        result[elt['data-name']] = elt['data-href']
        #result.append([elt['data-name'], elt['data-href']])
        #print(elt['data-name'], elt['data-href'])
    return result

if __name__ == '__main__':
    
    location = r"C:\Users\Kin\All_programming_projects\VSCode projects\discord bot\Manual"
    direct = f"{location}\pinescriptmanual.html"
    test_file = load_dynamic_page_locally(direct)
    
    soup = bs(test_file,'html.parser')
    tag = 'a'
    tagname = 'tv-pine-reference-toc-item'
    
    result = parse_soup(soup, tag, tagname)
    print(result)