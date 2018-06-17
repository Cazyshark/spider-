import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [


        "http://mp.weixin.qq.com/s?src=11&timestamp=1524979013&ver=845&signature=2y9zjQYeihq5ZyUMvHj*06J*JGC0eksrdWJXaCnugLOXZ7zLjR9gp*e*WtNRLMuUlU0xKLLiyw1hXnBCowDjrTNg85SgfY1pIj*tEluYP7IyuZz4*l9*ZyIYfa5eTNtB&new=1",
        "http://mp.weixin.qq.com/s?src=11&timestamp=1524979171&ver=845&signature=lFVjgrDkncjBdLk4p8xkgqWbwYB3OqXPPeO4zgT2ZQiMcTcc9lActjh8EWInF1UR3LPprolSvpmDIJcHSjCX476k-tPFlBFR3QxxUshMsUKB1M9vmh1gxZX7w939waak&new=1",
        "http://mp.weixin.qq.com/s?src=11&timestamp=1524979171&ver=845&signature=xIRVn6EIZhMk3C*ZxvJyWUOJi0q*vgzYQqyEt5XOeQDhVWasd5aEyGja6pI6yovS5fltvxTWwncd9wxnD72avMlfb9PHZ0ByRROKbyVwuxBOjfuxTl5FroghTubZHB93&new=1"

    ]

    def parse(self, response):
        filename = response.url.spilt('/')[-2]+ '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)