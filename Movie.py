

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