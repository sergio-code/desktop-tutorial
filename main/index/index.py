#############################
# Primer commit main App-Prueba
# *Subir a Github
# * Index.py
# ejecutable.exe
# release: 26/10/2022
# developer: Sergio Depetris
##############################

from tkinter import N, Y
import openpyxl
import calendario_prueba
#importación de archivos.py
#main-resources

marca_input = "HIDROFA", "GAMMA", "KARCHER", "LUSQTOFF", "BLACK&DECKER", 
"NIWA", "ELECTROLUX", "DAEWO", "MOTOMEL", "ECHO", "STHILL"
presion = 100, 150, 200 

quiereComenzar = Y,N
continuar = Y,N
Comenzar = Y, N

#Variable de compra
cuentaMarca = 0
cuentaPresion = 0
cuentaMarcaTotal = cuentaMarca
cuentaPresionTotal = cuentaPresion

def quiereComenzar():
 while True:
    Comenzar = input("¿Seguro?")
    if Comenzar != N:

     while True:
        marca = input('ingrese marca')
        if marca != "HIDROFA" and marca != "GAMMA" and marca != "KARCHER" and marca != "LUSQTOFF" and   marca != "BLACK&DECKER" and marca != "NIWA" and marca !="ELECTROLUX" and marca != "DAEWO" and marca != "MOTOMEL" and marca != "ECHO" and marca != "STHILL":
            print("Pone una marca valido")
        else:
            print("Genial")
            break
        continue

     while True:
        presion = int(input('ingrese presion'))
        if presion != 100 and presion != 150 and presion != 200:
           print("Ponga una presion valida")
        else:
            print("Excelente")
            break
        continue


     #variableUsuario
     #variableUsuario

     #definimos la ubicacion del archivo
     #wb = openpyxl.load_workbook("C:\Desarrollo GIT\contactos\emails\excel-emails.xlsx")
     #definimos la ubicacion del archivo
     #print("wb.sheetname")
     #ws = wb.get_sheet_by_name("CLIENTE")
     #fecha entrega

     #"calendar"
       
     cuentaMarca = 0
     cuentaPresion = 0
            
     while True:
        if marca == "HIDROFA" or marca == "GAMMA" or marca == "KARCHER" or marca == "LUSQTOFF" or marca == "BLACK&DECKER" or marca == "NIWA" or marca == "ELECTROLUX" or marca == "DAEWO" or marca == "MOTOMEL" or marca == "ECHO" or marca == "STHILL":
            cuentaMarca+=1
            print(cuentaMarca)
            break
        continue
     while True:    
            if presion == 100 or presion == 150 or presion == 200:
                cuentaPresion+=1
                print(cuentaPresion)
                break
            else:
                print ("estamos indesiso")
                break
    else:
        print("que queres?")
    break
    continue





while True:
    continuar = input("¿Agregar al carrito?")
    if continuar != N:
        quiereComenzar() 
    else:
        print("Gracias Totales")
        break
    continue