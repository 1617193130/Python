import urllib
import urllib2
import re


url = 'http://www.hbsc.cn/searchjob/index.aspx?JobName=%C7%EB%D1%A1%D4%F1%D6%B0%CE%BB%C0%E0%B1%F0&AreaText=%C7%EB%D1%A1%D4%F1%B9%A4%D7%F7%B5%D8%B5%E3&q=%BB%E1%BC%C6&bclass=&cclass=&prvc=&city=&area='
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.3.0.1000 Chrome/30.0.1599.101 Safari/537.36'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
content = response.read().decode('gb2312')
pattern = re.compile('<input type="checkbox" rel=.*?>.*?<a.*?>(.*?)</a>.*?<.*?></span><a.*?>(.*?)</a>.*?<span class="jobSalary"><label></label><span>(.*?)</span>',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2]
