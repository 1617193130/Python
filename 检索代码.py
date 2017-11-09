Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.sleep(5)
>>> y = 'localpath C:\code\cnkiCrawl'
>>> import re
>>> re.findall('[a-zA-Z]',y)
['l', 'o', 'c', 'a', 'l', 'p', 'a', 't', 'h', 'C', 'c', 'o', 'd', 'e', 'c', 'n', 'k', 'i', 'C', 'r', 'a', 'w', 'l']
>>> re.findall('[a-zA-Z]:',y)
['C:']
>>> re.findall('[a-zA-Z]:\S+',y)
['C:\\code\\cnkiCrawl']
>>> y = 'Hello Kitty Hello Hello Kitty Kitty Hello Kitty'
>>> re.findall('Hello',y)
['Hello', 'Hello', 'Hello', 'Hello']
>>> re.findall('(Hello){2}',y)
[]
>>> re.findall('(Hello ){2}',y)
['Hello ']
>>> re.findall('(:?Hello ){2}(Kitty)',y)
[('Hello ', 'Kitty')]
>>> re.findall('(:?Hello ){2}(:?Kitty ){2}',y)
[('Hello ', 'Kitty ')]
>>> re.findall('(:?Hello ){2}(Kitty ){2}',y)
[('Hello ', 'Kitty ')]
>>> re.findall('(?:Hello ){2}(?:Kitty ){2}',y)
['Hello Hello Kitty Kitty ']
>>> y = 'aabaaabaaaab'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> y = 'aabaaabaaaab'
>>> re.findall('a*?b',y)
['aab', 'aaab', 'aaaab']
>>> re.findall('a{,2}b',y)
['aab', 'aab', 'aab']
>>> 
