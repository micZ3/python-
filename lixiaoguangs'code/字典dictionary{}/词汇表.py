词汇表={'del':'删除',
        'append':'添加',
        'pop':'后值添加',
        'print':'打印',
        'sort':'永久排序',
        'len':'长度',
        'remove':'移动',
        'reverse':'反转',
        'range':'循环有几个',
        'keys':'名字',
        'insert':'插入',
        'pop':'删除末尾名字'}
print(词汇表)
print('我学习的第一个词汇是'+词汇表['append']+'意思是append')
#利用for 循环来遍历列表（for   (定义的数值名)  (定义的数值名).items():
#for循环不要忘记假冒号
#注意末尾缩进

for english, chinese in 词汇表.items():
    print('\n我学习的英语词汇'+english)
    print('他们的汉语意思'+chinese)
#方法keys()只能遍历字典中的名字，也就是第一个
for name in 词汇表.keys():
    print(name.title())
#加入大写
词汇表['title'] = '大写'
词汇表['str'] = '整个字符串'
print(词汇表)
favorite = ['sort','append','reverse']
for name in 词汇表:
    print(name.title)


    if name in favorite:
        print('This is my favorite words!')
#sorted()顺序遍历字典中的所有键（字母顺序遍历字典）
for name in sorted(词汇表.keys()):
    print("\n"+name.title()+" Congratulations to learning a new word!")
    print("马勒戈壁66666666啊 你在狗叫什么")
#values提取字典中的每个值
#set()集合，会使字典中的值变得独一无二






