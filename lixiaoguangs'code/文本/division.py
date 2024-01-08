print("Give me two number, and I'lldivide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    #编写健壮的程序善用try-except防止错误及抵御攻击
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can;t divide by 0!")
    else:
        print(answer)