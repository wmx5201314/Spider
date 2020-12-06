# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import os
class TrendsGooglePipeline:
    def process_item(self, item, spider):
        # print("---------------------------------------------------------------")
        keyword=[]
        if len(item["time"])==0:
            print(item["keyword"] +"  没有数据")
            return
        for i in range(len(item["time"])):
            keyword.append(item["keyword"])

        data=pd.DataFrame.from_dict({"keyword":keyword,"time":item["time"],"value":item["value"]})

        if not os.path.exists("data/"+item["keyword"]):
            os.mkdir("data/"+item["keyword"])
        data.to_excel("data/"+item["keyword"]+"/"+item["keyword"]+item["time"][0].replace("/","")+".xlsx")
        print(item["keyword"]+item["time"][0].replace("/","")+".xlsx","  ok")
        return item


