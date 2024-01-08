import traceback


def greet_user(username):
    """显示简单问候语"""
    print("Hello," + username.title() +"!")
greet_user('李小光')
#username是一个形参
#李小光是实参，及函数调用时传递的信息
#注意()和:
def make_shirt(saise,name):
    print(name + 'in the '+ saise +' T!')
make_shirt('A','李晓光')

def describe_city(city,A):
    """描述城市所在的国家"""
    print('The '+city + ' in the ' +A +' .')
describe_city('Beijing','China')

