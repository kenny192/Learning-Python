#coding:utf-8
"""
统计文本中每个字母出现的次数
"""
text = "Nothing is more important than the health and safety of our employees and customers. For that reason, in-person tours of our Seattle campus and fulfillment centers are on pause during the COVID-19 pandemic."

frequency = { }
for a in text:
    frequency[a] += 1

print(text)
print(frequency)