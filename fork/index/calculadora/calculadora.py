#############################
# Calculadora proyecto1
# Subir a Github
# release: 10/11/2022
# desarrollador: Sergio Depetris
##############################

number1=int(input("ingresa un numero:"))
number2=int(input("ingresa otro numero:"))

eleccion = 0

while eleccion != 2:
    print("""
    indique la operacion a realizar:
    
    1) suma
    2) resta
        """)

    eleccion = int(input())
    if eleccion == 1:
        print(" ")
        print("resultado:", number1,"+", number2,"=",number1+number2)
    if eleccion == 2:
        print(" ")
        print("resultado:", number1,"-", number2,"=",number1-number2)
    
    
