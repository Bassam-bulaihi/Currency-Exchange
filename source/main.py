from bs4 import BeautifulSoup as soup
import pyperclip as clip_bord
import requests as req

def main():
 
    url = clip_bord.paste()

    if url[:4] != "http" :
        print("Invalid URL")
        return
    
    response = req.get(url)
    page_soup = soup(response.text, 'html5lib')
    print(f"response code:{response.status_code}")

    print(f"html parse: \n {page_soup.prettify()[:2000]} ...")

main()         