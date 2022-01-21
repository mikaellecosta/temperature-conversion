print("""Você deseja converter de:
a) Celsius para Fahrenheit""")

choice = str(input())

while choice != "a":
    print("variavel invalida. tente novamente!")
    choice = str(input())

numero = int(input("escolha uma temperatura: "))
if choice == "a" and numero >-273:
 resultado =((9/5)*numero+32)
 cs = "°C"
 fb = "°F"
 print("{}{} equivale a {}{}.".format(numero, cs, resultado, fb))
 
else:
     print("estude mais fisica!")
     





