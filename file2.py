try:
    num1, num2=eval(input("enter two numbers, separated by coma: "))
    result=num1/num2
    print("result is", result)
except ZeroDivisionError:
    print("division by zero is error")
except SyntaxError:
    print("coma is missing.enter numbers separated by coma like 1, 2")
except:
    print("no exceptions")
finally:
    print("this will execute no matter what")            