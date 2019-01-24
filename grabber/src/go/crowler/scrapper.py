import os
import requests
import sys

from src.go.soup import gokifu


def download(url):
    print(url)
    response = requests.get(url, stream=True)
    filename = url[url.rfind("/") + 1:]
    with open(directory + "/" + filename, "wb") as handle:
        for data in response.iter_content():
            handle.write(data)


gokifuUrl = "http://gokifu.com"

print("Start scraping " + gokifuUrl)

page = 1

directory = "./data/"
if len(sys.argv) > 1:
    directory = sys.argv[1]

if not os.path.exists(directory):
    os.makedirs(directory)

while True:
    html = requests.get(gokifuUrl, {'p': page})
    links = gokifu.links(html.content)
    if not links:
        break
    for link in links:
        download(link)
    page += 1


print("Done scraping " + gokifuUrl)




