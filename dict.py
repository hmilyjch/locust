#count:计算某元素出现次数
# t=['to', 'be', 'or', 'not', 'to', 'be'].count('to')
# print(t)
#extend
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print (a)
# # index # 根据内容找位置
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang', ['wuchao', 'jinxin']]
first_lg_index = a.index("ligang")
little_list = a[first_lg_index+1:]
second_lg_index = little_list.index("ligang")
second_lg_index_in_big_list = first_lg_index + second_lg_index +1
print (second_lg_index_in_big_list)
# # reverse
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang']
a.reverse()
print (a)
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print (x)
a = ['wuchao', 'jinxin', 'Xiaohu','Ligang', 'sanpang', 'ligang']
a.sort()
print (a)





dic={1:'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
dic={'age':'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
#字典两大特点：无序，键唯一
#字典的创建
a=list()
dic={'name':'alex'}
dic1={}
dic2=dict((('name','alex'),))
dic3=dict([['name','alex'],])
dic1={'name':'alex'}
dic1['age']=18
#键存在，不改动，返回字典中相应的键对应的值
ret=dic1.setdefault('age',34)
#键不存在，在字典中中增加新的键值对，并返回相应的值
ret2=dic1.setdefault('hobby','girl')
#查 通过键去查找
# dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'}
print(dic3['name'])
print(list(dic3.keys()))
print(list(dic3.values()))
print(list(dic3.items()))



li=[1,2,34,4]
li[2]=5
dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'}
dic3['age']=55
dic4={'age': 18, 'name': 'alex', 'hobby': 'girl'}
dic5={'1':'111','2':'222'}
dic5={'1':'111','name':'222'}
dic4.update(dic5)
dic5 = {'name': 'alex', 'age': 18, 'class': 1}
# dic5.clear() # 清空字典
del dic5['name'] #删除字典中指定键值对
# print(dic5.pop('age')) #删除字典中指定键值对，并返回该键值对的值
ret=dic5.pop('age')
a = dic5.popitem() #随机删除某组键值对，并以元组方式返回值
# del dic5 #删除整个字典
#5 其他操作以及涉及到的方法
dic6=dict.fromkeys(['host1','host2','host3'],'test')
dic6['host2']='abc'
dic6=dict.fromkeys(['host1','host2','host3'],['test1','tets2'])
dic6['host2'][1]='test3'
print(dic6)




av_catalog = {
                "欧美":{
                "www.yyy.com": ["很多","质量一般"],
                "www.zzz.com": ["很多","质量高点"],
                "llll.com": ["多是很多","资源不多"],
                "xyz.com":["质量","全部收费"]
                },
                "日韩":{
                "hhh":["质量,个了","收费的"]
                },
                "大陆":{
                "1024":["全部免费","服务器在国外,慢"]
                }
                }
av_catalog['欧美']["www.yyy.com"][1]='安保处'
print(av_catalog)
dic={5:'555',2:'666',4:'444'}
# dic.has_keys(5)
print(5 in dic)
print(sorted(dic.items()))
dic5={'name': 'alex', 'age': 18}
for i in dic5:
    print(i,dic5[i])
for i,v in dic5.items():
    print(i,v)