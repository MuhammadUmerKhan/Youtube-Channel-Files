inputOperationType = input("Which Type of function You want to perform:[+, -, *, /] ")
if(inputOperationType == '+'):
    firstNumber_sum = input("Enter First Number: ")
    secondNumber_sum = input("Enter Second Number: ")
    def sum(firstNumber_sum,secondNumber_sum):
        try:
            result = int(firstNumber_sum)+int(secondNumber_sum)
            print(result)
        except ValueError:
            print("Oye! Insan ka Puttar ban")
    sum(firstNumber_sum,secondNumber_sum)

elif(inputOperationType == '*'):
    firstNumber_multi = input("Enter First Number: ")
    secondNumber_multi = input("Enter Second Number: ")
    def multi(firstNumber_multi,secondNumber_multi):
        try:
            result = int(firstNumber_sum)*int(secondNumber_sum)
            print(result)
        except ValueError as e:
            print(e)
    multi(firstNumber_multi,secondNumber_multi)
elif(inputOperationType == '/'):
    firstNumber_div = input("Enter First Number: ")
    secondNumber_div = input("Enter Second Number: ")
    def divide(firstNumber_div,secondNumber_div):
        try:
            result = int(firstNumber_sum)/int(secondNumber_sum)
            print(result)
        except ValueError as e:
            print(e)
    divide(firstNumber_div,secondNumber_div)

elif(inputOperationType == '-'):
    firstNumber_sub = input("Enter First Number: ")
    secondNumber_sub = input("Enter Second Number: ")
    def subtract(firstNumber_sub,secondNumber_sub):
        try:
            result = int(firstNumber_sum)-int(secondNumber_sum)
            print(result)
        except ValueError as e:
            print(e)
    subtract(firstNumber_sub,secondNumber_sub)
else:
    print("Invalid Input...")