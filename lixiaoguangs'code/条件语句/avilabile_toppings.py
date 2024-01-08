from zoneinfo import available_timezones


available_toppings=['mushrooms','olives','green peppers','pepperoni','poneapple','extra cheese']
requested_toppings=['mushroom','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding"+requested_topping+",")
    else:
        print("Sorry,we don't have"+requested_topping+".")
print("Finished making your pizza!")
