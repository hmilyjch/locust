'''
a=['wuchao','jinxin','xiaohu','sanpang','ligang',['wuchao','jinxin']]
#添加 append insert
a.append('xuepeng') #默认插到最后一个位置
print (a)
a.insert(1,'xuepeng') #将数据插入到任意一个位置
print (a)
#修改
a[1]='haidilao'
print (a)
a[1:3]=['a','uuu']
print(a)
# 删除 remove pop del
a.remove(a[0])
print(a)
b=a.pop(1)  #把第1个pop出来 赋值给b，第1个也从列表a中删除了
print(a)
print (b)
del a[0]
print(a)
# del a   #列表全部删除

a.remove(['wuchao','jinxin'])
print(a)

'''


#count:计算某元素出现次数
# t=['to', 'be', 'or', 'not', 'to', 'be'].count('to')
# print(t)
#extend
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)
# print(b)
# index # 根据内容找位置
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang', ['wuchao', 'jinxin']]
first_lg_index = a.index("ligang")
print(first_lg_index)
little_list = a[first_lg_index+1:]
print(little_list)
second_lg_index = little_list.index("ligang")
print(second_lg_index)
second_lg_index_in_big_list = first_lg_index + second_lg_index +1
print(second_lg_index_in_big_list)
# reverse
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang']
a.reverse()
print(a)
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)
a = ['wuchao', 'jinxin', 'Xiaohu','Ligang', 'sanpang', 'ligang']
a.sort()
print (a)




