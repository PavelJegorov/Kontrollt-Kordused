#3 вариант
#1

def linnumaja():
    print("   -----")
    print("  |  O  |")
    print("  !  -  !")

def linnumajas(num):
    for _ in range(num):
        linnumaja()
        print()  # Пустая строка

num_linnumajas = int(input("Введите количество скворечников (от 1 до 9): "))

# Вызываем функцию для отрисовки скворечников
linnumajas(num_linnumajas)

#2
kraadi = int(input("Введите показатель степени: "))
n = int(input("Введите число n: "))

#натуральные числа n, не превосходящие n**3
for i in range(kraadi + 1):
    tulemus = n ** i
    if tulemus <= n**3:
        print(f"(n)^(i) = (tulemus)")


#3