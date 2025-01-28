def add(num1, num2, num3):
    num3 = 3000
    add = num1 + num2 + num3
    return("Result =" + str(add))

def sub(num1, num2):
    sub = num1 - num2
    return("Result =" + str(sub))

def mul(num1, num2):
    mul = num1 * num2
    return("Result =" + str(mul))

def div(num1, num2):
    div = num1 / num2
    return("Result =" + str(div))


print(add(5, 10, 500))
print(sub(100, 200))
print(mul(10000, 567384))
print(div(10, 5))