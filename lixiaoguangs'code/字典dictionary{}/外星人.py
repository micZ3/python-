#字典中使用花括号{}
alien_0 = {'color':'green','points':'5'}
#指定字典名字用方括号[]
print(alien_0['color'])
#绿色小外星人666
new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!")
#str()是表示很好用的字符串

#添加字典
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#四个键值对
#使用del语句删除键-值对
del alien_0['points']
print (alien_0)
