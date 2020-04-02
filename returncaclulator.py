def addNumbers(num1,num2):
    answer_add = num1+num2
    return answer_add
     
def subtractNumbers(num1,num2):
    answer_subtract = num1-num2
    return answer_subtract


def DivideNumbers(num1,num2):
    answer_Divide = num1/num2
    return answer_Divide

def MultiplyNumbers(num1,num2):
    answer_Multiply = num1*num2
    return answer_Multiply

print ("Hi I am a calculator")
while True:
    operation =  input("Choose a operation.")
    if operation == "Add":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        global_add = addNumbers(a,b)
        print(global_add)
    elif operation == "Subtract":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        global_subtract = subtractNumbers(a,b)
        print(global_subtract)
    elif operation == "Divide":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        global_Divide = DivideNumbers(a,b)
        print(global_Divide)
    elif operation == "Multiply":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        global_Multiply = MultiplyNumbers(a,b)
        print(global_Multiply)
    elif operation== "quit":
        break

