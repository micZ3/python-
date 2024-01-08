with open('文本\pai_.txt') as file_object:
#with让python找时机关闭，不用写close
    contents = file_object.read()
    print(contents)
#rstrip()删除字符串末尾的空白
    print(contents.rstrip())
    #逐行读取
    filename = '文本\pai_.txt'
    #进行读取文件储存为filename
    with open(filename) as file_object:
        for line in file_object:
            print(line)
            #remove the gap
            print(line.rstrip())
    #reserve in a list and print it
    with open(filename) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
        #删除左边空格用strip(),右边用rstrip()
    
    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(pi_string)
    print(len(pi_string))
    #int()数据转换成整数，float()转换成浮点数
    #假如有1万个小数
    print(pi_string[:52] + "...")
    