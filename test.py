print("Калькулятор")

while input("Продовжуємо? (0 - ні)") != "0":
    a = int(input("Перше число"))
    b = int(input("Друге число"))
    
    op = input("Введіть операцію")
    
    if op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b != 0:
            print("Результат:", a / b)
        else:
            print("На нуль ділити не можна!")
    elif op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    else:
        print("Неправильна операція!")