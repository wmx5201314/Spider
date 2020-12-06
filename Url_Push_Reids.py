import redis
import datetime
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# https://trends.google.com/trends/api/widgetdata/comparedgeo?hl=zh-CN&tz=-480&req={"geo":{},"comparisonItem":[{"time":"2020-09-03 2020-12-03","complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":"中国"}]}}],"resolution":"COUNTRY","locale":"zh-CN","requestOptions":{"property":"","backend":"IZG","category":0}}&token=APP6_UEAAAAAX8m-lJaVGkdb-6z3OE3EPJyh_HASgHi6

def UrlPush(url_list):
    for url in url_list:
        print(r.rpush("explore_url", url))

def time_generate(start_date,end_date=None):
    #
    # if end_date is None:
    #     end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    #
    # # 转为日期格式
    # start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    end_year = datetime.datetime.now().strftime('%Y')
    date_list=[]
    while start_date<=int(end_year):
        if start_date==int(end_year):
            if datetime.datetime.strptime(end_date,'%Y-%m-%d') < datetime.datetime.strptime(str(end_year)+"-06-30",'%Y-%m-%d'):
                date_list.append([str(start_date)+"-01-01",end_date])
                return date_list
            else:
                date_list.append([str(start_date) + "-01-01", str(start_date) + "-06-30"])
                date_list.append([str(start_date) + "-06-30", end_date])
                return date_list
        date_list.append([str(start_date)+"-01-01",str(start_date)+"-06-30"])
        date_list.append([str(start_date)+"-07-1",str(start_date)+"-12-31"])
        start_date+=1
    return date_list
def url_generate(keyword,datelist):
    url_list=[]
    for timezone in datelist:
        url='https://trends.google.com/trends/api/explore?hl=zh-CN&tz=-480&req={"comparisonItem":[{"keyword":"'+keyword+'","geo":"","time":"'+timezone[0]+' '+timezone[1]+'"}],"category":0,"property":""}&tz=-480'
        url_list.append(url)
    return url_list
if __name__ == '__main__':
    datelist=time_generate(2013)
    with open("keyword (2).txt",'r',encoding="utf8")as f:
        for keyword in f:
            url_list=url_generate(keyword=keyword.strip(), datelist=datelist)
            UrlPush(url_list)

