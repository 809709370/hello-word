import re
import urllib
import urllib.request
import os
#encoding="utf-8"
class spider1:
    """这是一个基础的爬虫类"""
    i = 0
    def __init__(self):
        self.url = ""
        self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        self.data = None
        self.path = ""
    #获取网页源码
    def get_info(self,url,str):
        self.url = url
        self.str = str
        request = urllib.request.Request(url = self.url,headers= self.header)
        respone = urllib.request.urlopen(request)
        dataTm = respone.read()
        self.data = dataTm.decode("utf-8")
        express = re.compile(self.str, re.S)
        self.info = re.findall(express, self.data)
    def info_save(self,path):
        for item in self.info:
            items = item.replace("\n", "").replace("<br/>", "\n")
            self.path = path
            if not os.path.exists(self.path):
                os.mkdir(path=self.path)
            filename = self.path + "/" + str(spider1.i) + ".txt"
            fp = open(filename, "w", encoding='utf-8')
            fp.write(items)
            fp.close()
            spider1.i += 1





if __name__ == "__main__":

    #1.获取豆瓣网书评的网页代码
    # i = 0
    # print("开始爬取信息")
    # for page in range(1,14):
    #     url = "https://www.qiushibaike.com/8hr/page/" + str(page) +"/"
    #     print(url)
    #     header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    #     requests = urllib.request.Request(url = url,headers= header)
    #     respone = urllib.request.urlopen(requests)
    #     data = respone.read()
    #     data = data.decode('utf-8')
    #     #print(data)
    #     #print(respone.read())
    #     #2.提取所需要的信息
    #     express = re.compile("<div class=\"content\">.*?<span>(.*?)</span>",re.S)
    #     info = re.findall(express,data)
    #     #print(info)
    #     #3.将获取到的信息保存至文件中
    #     for item in info:
    #         items = item.replace("\n","").replace("<br/>","\n")
    #         path = "info"
    #         if not os.path.exists(path):
    #             os.mkdir(path=path)
    #         filename = path +"/"+ str(i) +".txt"
    #         fp = open(filename,"w",encoding='utf-8')
    #         fp.write(items)
    #         fp.close()
    #         i += 1

    print("爬取开始")

    spide = spider1()
    for page in range(1,14):
        url = "https://www.qiushibaike.com/8hr/page/" + str(page) +"/"
        str1 = "<div class=\"content\">.*?<span>(.*?)</span>"
        spide.get_info(url,str1)
        spide.info_save("info1")

    print("爬取结束")
