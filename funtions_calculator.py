def addNumbers(num1,num2):
    answer_add = num1+num2
    print(answer_add)
     
def subtractNumbers(num1,num2):
    answer_subtract = num1-num2
    print(answer_subtract)

def DivideNumbers(num1,num2):
    answer_Divide = num1/num2
    print(answer_Divide)

def MultiplyNumbers(num1,num2):
    answer_Multiply = num1*num2
    print(answer_Multiply)


print ("Hi I am a calculator")
while True:
    operation =  input("Choose a operation.")
    if operation == "Add":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        addNumbers(a,b)
        #Add=a+b
        #print(Add)
    elif operation == "Subtract":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        subtractNumbers(a,b)
        #Subtract=a-b
        #print(Subtract)
    elif operation == "Divide":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        DivideNumbers(a,b)
        #Divide=a/b
        #print(Divide)
    elif operation == "Multiply":
        a=float(input("Enter number."))
        b=float(input("Enter another number."))
        MultiplyNumbers(a,b)
        #Multiply=a*b
        #print(Multiply)
    elif operation== "quit":
        break

