from getCityCode import GetCityCode
from weather import Weather
from sendEmail import SendEmail

# city = '上海'
city = '西安'
msg_to = ['827110171@qq.com', '18829069704@163.com', '1545525016@qq.com']
# msg_to = ['827110171@qq.com']
msg_from = 'wjh_dan@163.com'
password = 'VCGSSUCOBYXVORQN'

code = GetCityCode(city).getCode()
print(code)
result = Weather().getWea(code)
print(result)
SendEmail(result, msg_to, city, msg_from, password).send()