try:
    num = int(input())
    divisor = int(input())
    result = num / divisor
    print(result)
except ValueError:
    print("Error : num and divisor number must be integer number")
except ZeroDivisionError:
    print("Error : Divisor number can not be Zero")

print("Execution Done!")