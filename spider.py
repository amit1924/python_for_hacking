import requests
from bs4 import BeautifulSoup
from urllib import *
from urllib.parse import urljoin


# url =https://amit1924.github.io/My_new_portfolio/

# 1.Method 1
# def get_page(url):
#     response = requests.get(url)

#     soup = BeautifulSoup(response.content, "html.parser")
#     tag = soup.find_all("a")
#     print(tag)
#     print("png : ", soup.find(src="gi.png"))

#     for t in tag:
#         urls2 = t.get("href")
#         print(f"href={url2}")


# get_page(input("What url you want to scrape: "))


# Method 2
# url=https://www.yahoo.com/
# keyword= portfolio
visited_urls = set()


def spider_urls(url, keyword):
    try:
        response = requests.get(url)

    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        anchor_tag = soup.find_all("a")

        urls = []

        for tag in anchor_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        print(f"URLS: {urls}")

        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(url)
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass


url = input("Enter url for scraping: ")
keyword = input("Enter the keyword for respected url: ")
spider_urls(url, keyword)
