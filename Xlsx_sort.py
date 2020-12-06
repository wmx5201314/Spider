import pandas as pd

content=pd.read_excel("data/中国.xlsx")
content.sort_values(by="时间",inplace=True)
# content.drop(content[[0]],axis=1)
print(content[])

# content.to_excel("中国_sort.xlsx")