# Scrapy settings for Trends_google project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Trends_google'

SPIDER_MODULES = ['Trends_google.spiders']
NEWSPIDER_MODULE = 'Trends_google.spiders'

REDIS_HOST = '124.71.41.168'
REDIS_PORT = 6379
LOG_LEVEL="WARNING"

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 启用去重功能
# 默认的scrapy-redis请求队列形式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mono (+http://www.yourdomain.com)'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8


RETRY_ENABLED = True  #打开重试开关
RETRY_TIMES = 3  #重试次数
RETRY_HTTP_CODES = [429]  #重试
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'en',
  'cookie': '__utmz=10102256.1606824942.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=10102256.186310438.1606824942.1607075836.1607080502.13; __utmc=10102256; __utmt=1; __utmb=10102256.1.10.1607080502; HSID=AYpUkADQ43-VSmDmA; SSID=ASeE_eTruTWMUK2YK; APISID=YV6CqzoK1EtFQp5l/ADgSnu0Xq3SryNIoy; SAPISID=3WadvE7L_wAxmitj/AmvRzFnOMlTDPWm88; __Secure-3PAPISID=3WadvE7L_wAxmitj/AmvRzFnOMlTDPWm88; SEARCH_SAMESITE=CgQIz5AB; SID=3QdTEsCyDhxMW0VFlXcX2kTyzYCIV_Uzbn7i4bwMuTcu5xiZoUp16eIxlTNU-qNJ1CSqHg.; __Secure-3PSID=3QdTEsCyDhxMW0VFlXcX2kTyzYCIV_Uzbn7i4bwMuTcu5xiZiFS3gmn5Df7dvMdk2FVFvA.; ANID=AHWqTUkwF-32KZ3strLvQbG-z7LAisUx8KqlPUapBYQGCUei_XL6U9CZ1rHknTLx; 1P_JAR=2020-12-02-13; NID=204=IYXvSoAvpqIQUl-2nBnlErJkD66GXTBivnoYfVxN7d0HIlwdpV14Yhrs-oLaQfFevzDh6ggB3URhdMcStUZCr90-CqI_InXqOxgZ6Wibba0phLXHuXPpkTRKWXgWqEKxD_jPs7ZlMrzaN-rUs-EPT2_Mjn1wTxGrQvCWHFFDBVE8kPTUbnxRPteCvMJ23O2p6t7rbsCu7HGIAHgJhpsOBA; SIDCC=AJi4QfFCQbulTyWZX_EdweUw50VCh2jPtBj4PEnajBgD8OPgsEKXaT3C-nI4In0vWDY_loTuWg; __Secure-3PSIDCC=AJi4QfG11ikjTaKmu1FI8dn6I0_VhE898wbzZZ22qDhXr68C3WFD8qtytz2WzQmBRUr3Xldw5w',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Trends_google.middlewares.TrendsGoogleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'Trends_google.middlewares.TrendsGoogleDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Trends_google.pipelines.TrendsGooglePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
