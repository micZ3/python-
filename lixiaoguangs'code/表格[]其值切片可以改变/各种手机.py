#表格 大制作 by 李正光6666
phone=['s10','s20','s20fe','s20+','s20uatral','s21','s21+','s21untral','s21fe']
msg="my first phone is "+phone[2]+"!"+" I very like it!"
print(msg)
#找最后一个s22，差1性，0123，这样子
print(phone[-1])
#末尾添加s22
phone.append('s22')
print(phone)
#插入s9
phone.insert(0,'s9')
print(phone)
#不能删0？？？？？？？
del phone[1]
print(phone)
#随意删，想删就删，哈哈哈
del phone[3]
print(phone)
#pop()可以任意删并保存位置
first_one=phone.pop(5)
#再次打印用pop()的就消失了，但可以根据first_one进行索引
print("My favorite phone is "+first_one+"666")
print(phone)
#删了还要用就得用pop()
#删了不用就del()
phone.remove('s22')
#remove()也可以删
print(phone)
too_expensive='s22'
print("\nA "+too_expensive+" is too expensive for me.")
print("\nI want buy s22 too.")
print("\nBut")
print("\nA "+too_expensive+" is too expensive for me.")
#sort可对表格永久排序（按字母排序）
phone.sort()
print(phone)                       
#sort(reverse=True)字母逆顺序排序（永久）
phone.sort(reverse=True)
print(phone)
#sorted()对列表进行临时排序
#反转元素排列列表用reverse(逆转)
phone.reverse()
print(phone)
phone.reverse()
print(phone)
len(phone)