#############################
# Primer commit main App-Prueba
# *Subir a Github
# * Index.py
# ejecutable.exe
# release: 26/10/2022
# developer: Sergio Depetris
##############################
import openpyxl
import calendario_prueba

#main-resources

marca = "HIDROFA", "GAMMA", "KARCHER", "LUSQTOFF", "BLACK&DECKER", "NIWA", "ELECTROLUX", "DAEWO", "MOTOMEL", "ECHO", "STHILL"

presion = "100", "150", "200" 

#index
marca = input('ingrese marca')
print ('usted quiere, ' + marca)

presion = input('ingrese presion')
print ('usted quiere, ' + presion)

while True:
        marca = input('ingrese marca')
        if marca != "NIWA":
            print("Pone una marca valido")
        else:
            print("Genial")
            break
        continue

while True:
        presion = int(input('ingrese presion'))
        if presion != (100):
            print("elija una presion valido")
        else:
            print("Bien")
            break
        continue


#variableUsuario

#definimos la ubicacion del archivo
wb = openpyxl.load_workbook("C:\Desarrollo GIT\contactos\emails\excel-emails.xlsx")

print("wb.sheetname")

ws = wb.get_sheet_by_name("CLIENTE")

#fecha entrega

"calendar"



