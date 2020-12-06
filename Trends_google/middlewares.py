# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import json
import random

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import requests
import time

class TrendsGoogleSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)





class TrendsGoogleDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    def __init__(self):
        self.proxy_data={}
    def get_ip(self):
        print("-----------------开始获取")
        response = requests.get(
            "http://api.ipproxy.info:8422/api/getIp?type=1&num=30&dataType=0&lineSeparator=0&noDuplicate=0&singleIp=0&unbindTime=180&orderId=O20120422034031928148&time=1607226654&sign=cc3eacc6f1d32ca48bf7e610a6834367&pid=1001006")
        get_time=time.time()
        if response.status_code==200:
            try:
                content_json =json.loads(response.text)
                data = content_json["data"]

                proxy_ips = []
                for i in data:
                    # ip_port=i.split(':')
                    ip = i['ip']
                    port = i['port']
                    proxy_ips.append("http://"+ip + ":" + str(port))
                return {get_time:proxy_ips}
            except Exception as e:
                print("api访问状态200，但是json解析错误，请检查ipset账号，或者是否在白名单，结果：",response.text)
                print(e)
                self.get_ip()
        else:
            print("获取代理api失败")
            self.get_ip()

        # print(proxy_ips)
    def return_ip(self):
        if len(self.proxy_data)==0:
            self.proxy_data=self.get_ip()
        if len(list(self.proxy_data.keys()))==0:
            print("休息5秒")
            time.sleep(5)
            self.proxy_data = self.get_ip()
        get_time=list(self.proxy_data.keys())[0]
        now_time=time.time()
        if now_time-float(get_time)>120:
            print("获取超过两分钟了，重新获取ip池")
            self.proxy_data = self.get_ip()
        return random.sample(self.proxy_data[get_time], 1)[0]
    def process_request(self, request, spider):
        # if 'proxy' not in request.meta:
        #     proxy_ip =  self.get_ip() # 这里需要导入那个函数
        # ruselt_ip=self.return_ip(proxy_ip)
        request.meta['proxy'] = self.return_ip()
        #print("这是代理",request.meta['proxy'])
        # request.meta['proxy'] ="47.241.22.26:14918"
        # print(request.meta)

        return None

    def process_response(self, request, response, spider):
        if response.status!=200:
            print("这个状态不是正常，休息2秒重新请求")
            time.sleep(2)
            self.process_request(request,spider)
            # print(response.status)
            print(response.text)
        # Called with the response returned from the downloader.
        # if 'proxy' not in request.meta:
        #     print("没代理了,需要检查")
        # print(request['proxy'])
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
