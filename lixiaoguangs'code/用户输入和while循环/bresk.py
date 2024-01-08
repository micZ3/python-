msg1 ="Can i help you something?"
active = True#给active添加标志
msg = ""
while active:
    msg ==input(msg1)

    if msg == "quit":
        active = False
        break
    else:
        print(msg1)

while True:
    #以while True的循环将不断运行，直到break语句
    #任何python中都可以使用break语句来退出循环，或者是遍历列表或字典的for循环