# -*- coding: gbk -*-
import ssl
import json
import urllib2
ssl._create_default_https_context =ssl._create_stdlib_context

while True:
    input_data = raw_input("请输入你的ip：")
    url="https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query="+input_data+"&co=&resource_id=6006"
    response_data=urllib2.urlopen(url=url).read().decode("gbk")

    json.loads(response_data)["data"][0]["location"]
    print json.loads(response_data)["data"][0]["location"]
