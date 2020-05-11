import requests                 #用来抓取网页上html的源代码
from bs4 import BeautifulSoup   #抓取源代码中标签的内容

class Weather(object):
    def GetContent(self, url):
        '''
        获得页面的html
        :param url:
        :return:
        '''
        header={
           'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
           'Accept - Encoding': 'gzip, deflate',
           'Accept - Language': 'zh - CN, zh;q = 0.9',
           'User - Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 68.0.3440.106 Safari/537.36'
        }
        res = requests.get(url,headers=header)
        res.encoding = 'utf-8'
        return res.text

    def GetData(self, html_text):
        '''
        获取最高温度与最低温度及天气状况
        :param html_text:
        :return:
        '''
        final = []
        bs = BeautifulSoup(html_text,"html.parser") # 创建BeautifulSoup对象
        body = bs.body #获取body内容
        data = body.find('div',{'id':'7d'})  #找到id为7d的div
        ul = data.find('ul')
        li = ul.find_all('li')  #获取所有的li

        for day in li: #对每1个li标签中的内容进行遍历
            temp = []
            date = day.find('h1').string #找到日期，具体哪一天
            temp.append(date)    #追加日期

            inf = day.find_all('p')
            temp.append(inf[0].string)    #追加天气状况

            if inf[1].find('span') is None:
                temperature_highest = None  #如果p标签中不包含span标签，则最高温度为空
            else:
                temperature_highest = inf[1].find('span').string #取最高温度

            temperature_lowest = inf[1].find('i').string  # 取最高温度
            temp.append(temperature_highest)
            temp.append(temperature_lowest)

            final.append(temp)
        return final

    def getWea(self, code):

        url = "http://www.weather.com.cn/weather/{}.shtml".format(code)
        html = self.GetContent(url)
        result = self.GetData(html)
        return result


