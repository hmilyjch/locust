import re
# print(re.findall('e','alex have dream') ) #['e', 'e', 'e'],返回所有满足匹配条件的结果,放在列表里
# print(re.search('e','alex have dream').group()) #e,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用
# group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
# print(re.match('e','alex have dream')) #None,同search,不过在字符串开始处进行匹配,完全可以用search+^代替match
#
# print(re.match('a','alex have dream'))
# print((re.match('a','alex have dream')).group())

print(re.split('[,]','a,b,c,d'))
print(re.split('[ab]','abcd')) #['', '', 'cd']，先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割

# print('===>',re.sub('a','A','alex have dream')) #===> Alex have dream，不指定n，默认替换所有
# print('===>',re.sub('a','A','alex have dream',1)) #===> Alex have dream
# print('===>',re.sub('a','A','alex have dream',2)) #===> Alex have dream
# print('===>',re.sub('^(\w+)(.*?\s)(\w+)(.*?\s)(\w+)(.*?)$',r'\5\2\3\4\1','alex have dream')) #===> love make alex
# print('===>',re.subn('a','A','alex have dream')) #===> ('Alex have dream', 2),结果带有总共替换的个数
obj=re.compile('\d{2}')
print(obj.search('abc123eeee').group()) #12
print(obj.findall('abc123eeee')) #['12'],重用了obj


print(re.split('/','http://www.sogou.com/docs/terms.htm?v=1'))


print('http://www.sogou.com/docs/terms.htm?v=1'[20:])
