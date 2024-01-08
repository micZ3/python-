pizza = {'crust':'thick',
         'toppiong':['mushrooms','extra cheese'],
         }
print("You ordered a "+pizza['crust'] + "-crust pizza"+"with the following topping:")
for                     topping in pizza['toppings']:
    print("\t" + topping)
