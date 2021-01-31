import scrapy
from firstblood.items import FirstbloodItem

class FirstSpider(scrapy.Spider):
    name = 'first'
   # allowed_domains = ['www.baidu.com']
    start_urls = ['https://job.dajie.com/qz1']

    # url的通用模板
    url_model = 'https://job.dajie.com/qz1-p%d/'
    page_number = 2

    def parse_detail(self,response):
        job_location = response.xpath('//*[@id="jp-app-wrap"]/div[2]/div[2]/div[5]/span[1]/text()')[0].extract()
        item = response.meta['item']
        item['job_location'] = job_location
        yield item




    def parse(self, response):

        # 请求网页 , 解析到li标签的列表
        li_list = response.xpath('//*[@id="content"]/div[1]/div[2]/div[3]/ul/li')

        # 循环体
        for li in li_list:
            # 实例化 item对象
            item = FirstbloodItem()

            # 解析到工作的名字, 生成对象
            job_name = li.xpath('./div[2]/p[1]/a/text()').extract_first()
            job_name = job_name.strip()

            # ?
            item['job_name'] = job_name

            # 解析到li标签内对应的详情页url
            detail_url = li.xpath('./div[2]/p[1]/a/@href').extract_first()


            # ?  请求传参
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})



        # 循环调用
        if self.page_number <= 5:

            # 生成下一个页面的url,页面变量自增1,递归调用parse
            new_url = format(self.url_model%self.page_number)
            self.page_number += 1
            yield scrapy.Request(new_url,callback=self.parse)



