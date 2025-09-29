from bs4 import BeautifulSoup as soup
import pyperclip as clip_bord
import requests as req


#aria-label= name of lising
#price = is price
def main():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
    url = clip_bord.paste()

    if url[:4] != "http" :
        print("Invalid URL")
        return
    
    response = req.get(url,headers=headers)
    page_soup = soup(response.text, 'html5lib')
    print(f"response code:{response.status_code}")

    print(f"html parse: \n {page_soup.prettify()[:300]} ...")

    with open("my_page.html", "w") as f:
        f.write(page_soup.prettify())

main()         