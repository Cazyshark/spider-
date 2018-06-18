import requests

#
# url='http://api.giuhub.com/evernts'
# # r = requests.get('http://www.baidu.com')
# # print(r.headers)
# # # print(r.text)
# # # print(r.status_code)
# # # print(r.headers)
# r=requests.get('http://api.giuhub.com/evernts')
# payload={'key1':'value1','key2':'value2'}
# r=requests.get(url=url,params=payload)
# # print(r.cookies)
#
# # print(r.url)
# # print(r.text)
# print(r.raw)
# print(r.raw.read(11))

# url='http://ww.baidu.com'
# r=(requests.get(url=url))
# r.status_code == requests.codes.ok
# print(bool(r.status_code))
# print(r.headers['Connection'])

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookies/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)
requests.get('https://github.com', verify='/path/to/certfile')

