firstNumber_sum = input("Enter First Number: ")
secondNumber_sum = input("Enter Second Number: ")
def sum(firstNumber_sum,secondNumber_sum):
    try:
        result = int(firstNumber_sum)+int(secondNumber_sum)
        print(result)
    except ValueError as e:
        print(e)
sum(firstNumber_sum,secondNumber_sum)