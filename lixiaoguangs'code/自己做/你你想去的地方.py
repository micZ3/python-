place = {}
#添加标志
A = True
while A:
    名字 = input('\n你叫什么名字?bro')
    p = input('你最想去哪里呀？')
    place[名字] = p
    回答 = input("你希望别人来回答吗? (yes/no)")
    if 回答 == 'no':
        A = False
print('拜拜再见')
for 名字,p in place.items():
    print(名字 + "希望去"+p+"!")
    