filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming!")

with open("programming.txt") as f:#一次读取一行
    res = f.readline
print(res)
with open("programming.txt") as f:#一次全部读取
    resd = f.readlines
print(resd)

with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can eun in a browser.\n")
    