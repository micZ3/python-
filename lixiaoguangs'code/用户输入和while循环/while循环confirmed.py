#for循环不应该修改列表，while循环可以
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
#验证每一个用户
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    #pop删除末尾的名字
    print('Verifying user:' + current_user.title())
    confirmed_users.append(current_user)
    #显示所有已经雅正的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())