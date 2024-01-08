#“%”，他将两个数相除并返回余数
4 % 3
#只显示余数
#可以用来判别是奇数还是偶数
number = input("enter a nummber,and i will tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(str(number)+" is even")
else:
 print(str(number)+" is odd!")
 #if,for,语句都要加冒号，而且注意缩进
 
