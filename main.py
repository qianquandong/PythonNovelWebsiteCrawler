#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 11:15:08 2022

@author: jackqian
"""

import requests
from bs4 import BeautifulSoup

def get_novel_chapters(url):
    r = requests.get(url)
    #r.encoding = "UTF-8"
    soup = BeautifulSoup(r.text, "html.parser")
    
    data = []
    for div in soup.find_all("h3"):
        link = div.find("a")
        if not link:
            continue
        data.append((link['href'], link.get_text()))
    return data

def get_novel_name(url): 
    r = requests.get(url)
    #r.encoding = "UTF-8"
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.find("title").get_text()
    idx = ""
    for i , n in enumerate(title):
        if n == '-':
            idx = i
            break
    return title[0:idx]


def get_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    content = ""
    for p in soup.find_all("p"):
        con = p.get_text()
        content += con
        content += "\n"
    #return soup.find("div", id="post-body-986492738120677878").get_text()
    return content.replace("\t", '')

entire_novel = ""
url = "https://freewebnovel.com"
book_name = get_novel_name(url)
for chapter in get_novel_chapters(url):
    url, title = chapter
    entire_novel += "\n"
    entire_novel += title
    entire_novel += "\n"
    entire_novel += get_content(url)
    with open(book_name + ".txt", "w") as fout:
        fout.write(entire_novel)