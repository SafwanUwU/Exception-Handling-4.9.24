def enterage(age):

    if age <0:
        raise ValueError("Only positive integers are allowed")

    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is Odd")


try:
    num = int(input("Enter your age: "))
    enterage(num)


except Value15Error:
    print("Only positive integers are allowed")