requested_toppings=['mshrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping =='green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding"+requested_topping+".")

print("\nFinished making your pizza!")
#注意缩进
#if,else对齐

requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding"+requested_topping+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    