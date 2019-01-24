import re
from bs4 import BeautifulSoup


def links(content):
    soup = BeautifulSoup(content, 'html.parser')
    divs = soup.findAll("div", {"class" : "game_type"})
    links = []
    for div in divs:
        try:
            link = div.find("a", {"href": re.compile("\\.sgf$")})['href']
            if link is None:
                continue
            links.append(link)
        except:
            continue
    return links