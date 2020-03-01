print ("Hi I am a calculator")
while True:
    operation =  input("Choose a operation.")
    if operation == "Add":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        Add=a+b
        print(Add)
    elif operation == "Subtract":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        Subtract=a-b
        print(Subtract)
    elif operation == "Divide":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        Divide=a/b
        print(Divide)
    elif operation == "Multiply":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        Multiply=a*b
        print(Multiply)
    elif operation== "quit":
        break

