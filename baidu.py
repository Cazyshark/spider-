import selenium.webdriver
import time
import request.parse

diver =selenium.webdriver.Firefox()
url="http://tianqi.2345.com/"
diver.get(url)
for ava in request.xpath(/html/body/div[5]/div[3]/div[5]/div[1]/div/div[2]/div[2]/text()):

 print(ava)


diver.quit()
