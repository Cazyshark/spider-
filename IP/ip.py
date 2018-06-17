# -*- coding: gbk  -*-
import ssl
import json
import urllib2
import sys

sys.path.append('D:\\wd\\venv\\Scripts\\python.exe')
reload(sys)

sys.setdefaultencoding('utf-8')
ssl._create_default_https_context =ssl._create_stdlib_context

while True:
    input_data = raw_input("请输入你要查询的城市：")
    url="https://www.sojson.com/open/api/weather/json.shtml?city="+input_data
    response_data=urllib2.urlopen(url=url).read().decode("utf-8")


    print "PM指数:"+str(json.loads(response_data)["data"]["pm10"])
    print "风向: "+json.loads(response_data)["data"]["yesterday"]["fx"]

    print "风力:"+json.loads(response_data)["data"]["yesterday"]["fl"]
    print "气温:"+json.loads(response_data)["data"]["yesterday"]["high"]
    print "日落时间: "+json.loads(response_data)["data"]["yesterday"]["sunset"]
    print "天气情况: "+json.loads(response_data)["data"]["yesterday"]["type"]
    print "更新时间: "+json.loads(response_data)["data"]["yesterday"]["date"]
    print "湿度: "+str(json.loads(response_data)["data"]["yesterday"]["aqi"])


