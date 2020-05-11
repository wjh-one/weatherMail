from getCityCode import GetCityCode
from weather import Weather
from sendEmail import SendEmail

city = '上海'
# city = '西安' # 要查询的城市地址
msg_to = ['', '']  # 收件人邮箱，可以写多个。
msg_from = ''   # 发件人邮箱
password = ''  # 发件人邮箱授权码

code = GetCityCode(city).getCode()
print(code)
result = Weather().getWea(code)
print(result)
SendEmail(result, msg_to, city, msg_from, password).send()