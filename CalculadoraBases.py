def Dec2Bin():  #Función que convierte de decimal a binario
    num=float(input("ingrese el numero a convertir: "))
    IntNum=int(num)
    FracNum=num-IntNum
    binNumInt=bin(int(num))
    binNumFrac=''
    while FracNum!=0:
        FracNum*=2
        BitFrac=int(FracNum)
        binNumFrac+=str(BitFrac)
        FracNum-=BitFrac
    resultado=(binNumInt+'.'+binNumFrac)
    result=print(f"el resultado es: {resultado}\n")
    return result

    
def Dec2Oct():      #Función que convierte de decimal a octal
    num=float(input("ingrese el numero a convertir: "))
    IntNum=int(num)
    FracNum=num-IntNum
    octNumInt=oct(int(num))
    octNumFrac=''
    while FracNum!=0:
        FracNum*=8
        OctFrac=int(FracNum)
        octNumFrac+=str(OctFrac)
        FracNum-=OctFrac
    resultado=(octNumInt+'.'+octNumFrac)
    result=print(f"el resultado es: {resultado}\n")
    return result

    
def Dec2Hex():      #Función que convierte de decimal a hexadecimal
    num=float(input("ingrese el numero a convertir: "))
    IntNum=int(num)
    FracNum=num-IntNum
    hexNumInt=hex(int(num))
    hexNumFrac=''
    while FracNum!=0:
        FracNum*=16
        HexFrac=int(FracNum)
        hexNumFrac+=str(HexFrac)
        FracNum-=HexFrac
    resultado=(hexNumInt+'.'+hexNumFrac)
    result=print(f"el resultado es: {resultado}\n")
    return result

    
def Bin2Dec():      #Función que converte de binario a decimal
    BinNum=input("ingrese un número binario: ")
    if '.' in BinNum:
        BinInt, BinFrac = BinNum.split('.')
        DecInt = int(BinInt, 2)
        DecFrac = sum(int(bit) * 2**(-i-1) for i, bit in enumerate(BinFrac))
        resultado = DecInt + DecFrac
    else:
        resultado = int(BinNum, 2)
    return print(f"El resultado es: {resultado}\n")

    
def Oct2Dec():      #Función que convierte de octal a decimal
    OctNum=input("ingrese un numero octal: ")
    if '.' in OctNum:
        OctInt, OctFrac = OctNum.split('.') 
        DecInt= int(OctInt, 8)
        DecFrac = sum(int(digito) * 8**(-i-1) for i, digito in enumerate(OctFrac))
        resultado= DecInt + DecFrac
    else:
        resultado = int(OctNum, 8)
    return print(f"El resultado es: {resultado}\n")


def Hex2Dec():      #Función que convierte de hexadecimal a decimal
    HexNum=input("ingresa un número hexadecimal (letras en mayuscula): ")
    if '.' in HexNum:
        HexInt, HexFrac = HexNum.split('.')  
        DecInt = int(HexInt, 16)
        DecFrac = sum(int(digito, 16) * 16**(-i-1) for i, digito in enumerate(HexFrac))
        resultado= DecInt + DecFrac
    else:
        resultado = int(HexNum, 16)

    return print(f"El resultado es: {resultado}\n")

#Menu Principal
while True:
    print("¿Qué operación desea realizar?\n 1.- decimal a binario\n 2.-decimal a octal\n 3.- decimal a hexadecimal\n 4.- binario a decimal\n 5.- octal a decimal\n 6.- hexadecimal a decimal\n 7.-salir del programa")
    opcion=int(input())
    if opcion ==1:
        conversion=Dec2Bin()
    elif opcion==2:
        conversion=Dec2Oct()
    elif opcion==3:
        conversion=Dec2Hex()
    elif opcion==4:
        conversion=Bin2Dec()
    elif opcion==5:
        conversion=Oct2Dec()
    elif opcion==6:
        conversion=Hex2Dec()
    elif opcion==7:
        break
    else:
        print("opcion no valida. Escoja una opcion valida por favor")

