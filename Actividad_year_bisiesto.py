# Actividad año bisiesto

year = int(input("ingrese año para saber si es bisiesto o no: "))

if year % 400 == 0:
    print("su año es bisiesto")
elif year % 4 == 0 and year % 100 != 0:
    print("su año es bisiesto")
else:
    print("su año no es bisiesto")