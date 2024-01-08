prompt = "if you tell us who you are,we can personalize the messages you see."
prompt +="\nWhat is you first name?"
#=+在prompt末尾加上一个字符串


#跨两行使显示更清晰
name = input(prompt)
print("\nHello," + name + "!")