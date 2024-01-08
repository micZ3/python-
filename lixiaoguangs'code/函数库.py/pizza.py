def make_pizza(size,*toppings):
    #size 用字符串更好，比较随意
    print("\nMaking a" + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
