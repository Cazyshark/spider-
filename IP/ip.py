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
    input_data = raw_input("��������Ҫ��ѯ�ĳ��У�")
    url="https://www.sojson.com/open/api/weather/json.shtml?city="+input_data
    response_data=urllib2.urlopen(url=url).read().decode("utf-8")


    print "PMָ��:"+str(json.loads(response_data)["data"]["pm10"])
    print "����: "+json.loads(response_data)["data"]["yesterday"]["fx"]

    print "����:"+json.loads(response_data)["data"]["yesterday"]["fl"]
    print "����:"+json.loads(response_data)["data"]["yesterday"]["high"]
    print "����ʱ��: "+json.loads(response_data)["data"]["yesterday"]["sunset"]
    print "�������: "+json.loads(response_data)["data"]["yesterday"]["type"]
    print "����ʱ��: "+json.loads(response_data)["data"]["yesterday"]["date"]
    print "ʪ��: "+str(json.loads(response_data)["data"]["yesterday"]["aqi"])


