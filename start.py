# print("Hello World")

# name = "Tomas"

# print("Name =>", name)

# a = 5
# b = "10"

# print(a + b)

# exit = False

# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# elif a == b:
#     print("a = b")

# name = int(input("What is your name? "))
# print("Hi", name)
# print("Type", type(name))





# a = int(input(("Enter first number: ")))
# b = int(input(("Enter second number: ")))
# operator = input("Operator: + - * /    ")

# if operator == "+":
#     print(a + b)
# elif operator == "-":
#     print(a - b)
# elif operator == "*":
#     print(a * b)
# elif operator == "/":
#     print(a / b)
# elif operator == "/":
#     if b == 0:
#         print("Dovision on zero")



# month = int(input("Enter month:  "))

# if month == 1 or month == 2 or month == 12:
#     print("Winter")
# elif month == 3 or month == 4 or month or month == 5:
#     print("Spring")
# elif month == 6 or month == 7 or month == 8:
#     print("Summer")
# elif month == 9 or month == 10 or month == 11:
#     print("Autumn")












#_____________________________________________________________________________



# clock = int(input("Enter o'clock: "))

# if clock >= 6 and clock <= 11:
#     print("Good morning")
# elif clock >= 12 and clock <= 17:
#     print("Good day")
# elif clock >= 18 and clock <= 23:
#     print("Good evening")
# else:
#     print("Good night")


unit = int(input("Enter your unit, inch = 1 or cm = 0: "))
converter = int(input("Enter number: "))

inch = 1
cm = float(2.54)

if unit == 1:
    res = converter * cm
    print("Inch", res)
elif unit == 0:
    res = converter / cm
    print("Centimetrs", res)
else:
    ("Enter a valid number!")


#_________________________________________________________________________________












# import colorama
# from colorama import Fore, Back, Style
# colorama.init()

# # Обчислення споживання пального Вашого авто!


# car = input("Введіть марку вашого авто: ")  # для стилізації результату
# # перша змінна
# distance = float(input("Введіть відстань до пункту призначення в км.: "))
# # друга змінна
# fuel = float(input("Кількість споживання палива /100км: "))


# def result(distance, fuel):  # Функція обчислення
#     res = distance / 50 * fuel
#     print("Ваш автомобіль", Fore.LIGHTRED_EX + car.upper(), Fore.RESET + "витратить",
#           Fore.YELLOW + str(res),Fore.RESET+ "л. пального в дві сторони!")


# result(distance, fuel)



















