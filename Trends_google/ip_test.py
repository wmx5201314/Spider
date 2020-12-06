#coding=utf-8
import requests

#请求地址
targetUrl = "http://124.71.41.168/"
# requests.get(targetUrl)
#代理服务器
with open("ips.txt",'r',encoding="utf8")as f:
    for i in f:
        print(i.strip())
        # ip_port=i.strip().split(':')
        # proxyHost = ip_port[0]
        # proxyPort = ip_port[1]
        #
        # proxyMeta = "http://%(host)s:%(port)s" % {
        #
        #     "host" : proxyHost,
        #     "port" : proxyPort,
        # }
        proxyMeta="http://"+i.strip()
        print(proxyMeta)


        proxies = {

            "http"  : proxyMeta,
            "https"  : proxyMeta
        }
        print(proxies)
        try:
            resp = requests.get(targetUrl, proxies=proxies,timeout=3)
            print(resp.status_code)
            print(resp.text)
        except Exception as e:
            print("异常",e)
            continue