import urllib
import expanddouban
import Movie
import pandas
import codecs
from bs4 import BeautifulSoup

def getMovieUrl(category,location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category,location)
    return url

#电影类
class Movie:
    #构造函数？
    def __init__(self,name,rate,location,category,info_link,cover_link):
        self.name = name #电影名称
        self.rate = rate #电影评分
        self.location = location #电影地区
        self.category = category #电影类型
        self.info_link = info_link #电影页面链接
        self.cover_link = cover_link #电影海报图片链接
    def to_string(self):
        return "name={},rate={},location={},category={},info_link={},cover_link={}".format(
            self.name,self.rate,self.location,self.category,self.info_link,self.cover_link
        )

def getMovies(category,location):
    movies = []
    url = getMovieUrl(category,location)
    html = expanddouban.getHtml(url,True,2)
    soup = BeautifulSoup(html,"html.parser")
    content_div = soup.find(class_ = "list-wp")
    for movie in content_div.find_all("a",recursive = False):
        if movie:
            info_link = movie.get("href") #电影首页链接
            name = movie.find(class_ = "title").string #电影名称
            rate = movie.find(class_ = "rate").string #电影评分
            # cover_link = movie.find("div",recursive = False).find("span",recursive = False).find("img",recursive = False).get("src")
            cover_link = movie.find(class_ = "pic").find("img",recursive = False).get("src")#电影海报链接
            movies.append(name)
            movies.append(rate)
            movies.append(category)
            movies.append(location)
            movies.append(info_link)
            movies.append(cover_link)
    return movies

#获取三种类型，三个地区的电影信息并合并结果到一个列表
movies3 = getMovies("喜剧","美国")
movies2 = getMovies("爱情","大陆")
movies1 = getMovies("犯罪","香港")
movies1.extend(movies2)
movies1.extend(movies3)

#抽离电影名称，电影评分等单独成为六个列表，方便写入csv文件
# names = []
# rates = []
# categorys = []
# locations = []
# infoLinks = []
# coverLinks = []
# for i in range(len(movies1)):
#     if i%6 == 0:
#         names.append(movies1[i])
#     elif i%6 == 1:
#         rates.append(movies1[i])
#     elif i%6 == 2:
#         categorys.append(movies1[i])
#     elif i%6 == 3:
#         locations.append(movies1[i])
#     elif i%6 == 4:
#         infoLinks.append(movies1[i])
#     elif i%6 == 5:
#         coverLinks.append(movies1[i])

# 写入csv文件
# dataFrame = pandas.DataFrame({'电影名称':names,'电影评分':categorys,'电影类型':rates,'电影地区':locations,'电影首页链接':infoLinks,'电影海报链接':coverLinks})
# dataFrame.to_csv("movies.csv",index = False,sep = ',')

#另外一种写入csv文件的方式（列表中6条信息为一部电影，所以写入csv6次换行）
#codecs防乱码
with codecs.open('movies.csv','w','utf_8_sig') as w:
    for i in range(len(movies1)):
        if i%6 == 5:
            w.write(movies1[i]+'\n')
        else:
            w.write(movies1[i]+',')

#从网页上获取所有地区
def getLocations():
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    html = expanddouban.getHtml(url)
    soup = BeautifulSoup(html,"html.parser")
    locations = []
    #获取所有地区的第一种方式
    # content_div = soup.find("div",class_ = "tags")
    # i = 0
    # for ul in content_div.find_all("ul",recursive = False):
    #     if i == 2:
    #         for li in ul.find_all("li",recursive = False):
    #             location = li.find("span",class_ = "tag").string
    #             locations.append(location)
    #     i += 1

    #获取所有地区较为简洁的方式
    for child in soup.find(class_ = "tags").find(class_ = "category").next_sibling.next_sibling:
        location = child.find(class_ = "tag").get_text()
        if location != '全部地区':
            locations.append(location)
    return locations

#分别统计出爱情，战争，喜剧三种类型的电影在每个地区有多少部并将结果放在字典中
def getMoviesOfLocation(category,locations):
    moviesOfLocation = {}
    for location in locations:
        movies = getMovies(category,location)
        #求出总共有多少部电影
        num = len(movies)//6
        moviesOfLocation[location] = num
    return moviesOfLocation

#分别获取三种电影类别中数量排名前三的地区信息并打印
def getResult(category):
    locations = []#数量最大的三个地区的地区名
    movieList = []#各个地区该种电影类型的数量列表
    result = {}#最终结果
    sum = 0
    movies = getMoviesOfLocation(category,getLocations())
    for m in movies:
        movieList.append(movies[m])
        sum += movies[m]
    #将各个地区的电影数量排序并取出最大的三个
    movieList = sorted(movieList)[-3:]
    for num in movieList:
        for m in movies:
            if num == movies[m]:
                #从字典中移除已经取到的值，以免相同结果取到重复值
                movies.pop(m)
                result[m] = num 
                break
    for location in result:
        locations.append(location)
    message = "{}电影类别中，数量排名前三的地区有{},{},{},他们分别占此类电影总数的百分比为{},{},{}".format(
        category,locations[0],locations[1],locations[2],str(round(movieList[0]/sum*100,2)),str(round(movieList[1]/sum*100,2)),str(round(movieList[2]/sum*100,2))
    )
    return message

#将最终结果写入txt文件
categorys = ["爱情","战争","剧情"]
messages = []
for category in categorys:
    messages.append(getResult(category))
with open('output.txt','w',encoding="utf-8") as w:
        for message in messages:
            w.write(message+'\n')