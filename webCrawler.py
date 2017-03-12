"""
    STRUCTURE OF MY INDEX
    NEEDED: keywords, appropriate links,
    HOW: capture words in each page. when a user types a word should
         get all the links that contains that word

        index = all words mapped to appropriate links
            {word1:{url1:[count, rank],
                    url2:[count, rank],
                    url3:[count, rank]},
             word2:[links],
             word3:[links],
                    .....} ==>

"""
from urllib.request import urlopen

index = {}

def get_links(page):
    links = []
    while True:
        pos = page.find('<a href')
        if pos == -1:
            break
        page = page[pos+8:]
        start = page.find('"')
        links.append(page[start+1:page.find('"',start+1)])
    return links

def get_page(url):
    return urlopen(url).read()


def add_to_index(words,
