#生成所有的6位随机数字密码
import string

# 生成数字字符集
digits = string.digits

# 打开文件，以写入模式写入数据
with open('passwords.txt', 'w') as file:
    # 嵌套循环生成所有的 6 位数字密码
    for digit1 in digits:
        for digit2 in digits:
            for digit3 in digits:
                for digit4 in digits:
                    for digit5 in digits:
                        for digit6 in digits:
                            password = digit1 + digit2 + digit3 + digit4 + digit5 + digit6
                            # 将密码写入文件
                            file.write(password + '\n')