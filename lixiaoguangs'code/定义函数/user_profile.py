def build_profile(first, last,**user_info):
    #let 2 ** is set dectionr - user_info,fist last in it储存在一个叫user的字典中

    profile = {}
    #set a dectiona
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key]= value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)