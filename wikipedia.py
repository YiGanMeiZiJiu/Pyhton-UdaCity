import requests
import time
import urllib
from bs4 import BeautifulSoup

#页面=一个随机起始页
#article_chain = []
#而页面标题不是“哲学”，而且我们还没有发现循环：
#    将页面添加到 article_chain
#    下载页面内容
#    在内容中查找第一个链接
#    页面=该链接
#    暂停片刻

def continue_crawl(search_history,target_url,max_steps=25):
    if search_history[-1] == target_url:
        print("最近文章就是当前文章")
        return False
    elif len(search_history) >= max_steps:
        print("列表超过25个url还没到达哲学")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("列表中的url陷入了循环")
        return False
    else:
        return True

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")

    first_relative_link = None

    content_div = soup.find(id = "mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p",recursive=False):
        if element.find("a",recursive=False):
            first_relative_link = element.find("a",recursive=False).get("href")
            break

    if not first_relative_link:
        return
    #短链转长链
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/',first_relative_link)

    return first_link

start_url = "http://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [start_url]

while continue_crawl(article_chain,target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        break
    
    article_chain.append(first_link)
    #放慢程序，避免抓取数据速度太快被误认为攻击网站
    time.sleep(2)