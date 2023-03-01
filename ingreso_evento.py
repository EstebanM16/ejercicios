""""
edad= 18
edad_fan =22
while
edad_fan<edad 



boleta=True
"""



#EJERCICIO

empleados="pedro"
empleado_2="juan"
empleado_3="yahir"
empleado_4="esteban"

hora_A=20000
hora_B=10000
horax=5000
hora_exA=(hora_A/100*0.6+horax)*3
hora_exB=(hora_B/100*0.6+horax)*3
hora_ex=(horax*6/100 + horax)*3

salario_A=((hora_A*8)*30)
salario_B=((hora_B*8)*30)
salario_otro=((horax*8)*30)



if empleados=="pedro":
    print("EMPLEADOS EN PROYECTO A",)
    print(empleados)
    print("con un pago por hora de",": $",hora_A)

if salario_A > 1500000:
    print("el salario es mayor al tope maximo")
    print("con un salario mensual de ",salario_A)
else :
     print("pagarle al empleado por concepto de horas extras:")
     print( hora_exA)
     
print("")



if empleado_2=="juan":
    print("EMPLEADOS EN PORYECTO B",)
    print(empleado_2)
    print(empleado_3)
    print("con un pago por hora de",": $",hora_B)

if salario_B > 1500000:
    print("el salario es mayor al tope maximo")
    print("con un salario mensual de ",salario_B)
else :
     print("pagarle al empleado por concepto de horas extras:")
     print( hora_exB)

print("")

if empleado_4=="esteban":
    print("EMPLEADOS EN OTRO",)
    print(empleado_4)
    print("con un pago por hora de",": $",horax)

if salario_otro > 1500000:
    print("el salario es mayor al tope maximo")
    print("con un salario mensual de ",salario_otro)
else :
     print("con un salario mensual de ",salario_otro)
     print("pagarle al empleado por concepto de horas extras:")
     print( hora_ex)




    




