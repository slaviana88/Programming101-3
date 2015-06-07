import requests
from bs4 import BeautifulSoup

ADRESS = "http://register.start.bg/"
r = requests.get(ADRESS)

soup = BeautifulSoup(r.text)

with open("links.txt", 'w') as f:
    for link in soup.find_all('a'):
        if str(link.get("href")).startswith("link"):
            f.write(link.get("href")+"\n")

with open("links.txt", 'r') as f:
    allLink = f.read().split()

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"

with open("servers.txt", "w") as f:
    for link in allLink:
        try:
            s = requests.get("http://register.start.bg/"+link, headers=headers, timeout=5)
            f.write(s.headers["server"] + "\n")
            print(s.headers["server"])
        except:
            pass
