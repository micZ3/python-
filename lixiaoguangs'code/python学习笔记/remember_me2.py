import json#储存了用户名就加载他
def hi_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name?")
        with open(filename,"w") as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back," + username + "!")
    else:
        print("Welecome back," + username + "!")
        #两个文件合并了
hi_user()
