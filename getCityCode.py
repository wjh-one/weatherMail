import requests
import re

class GetCityCode(object):
    def __init__(self, city):
        self.city = city

    def getCode(self):
        city = self.city

        url = 'http://toy1.weather.com.cn/search'
        param = {
            'cityname':'{}'.format(city)
        }
        ress = requests.get(url, param)
        htms = re.findall(r"\d{9}", ress.text)
        return htms[0]