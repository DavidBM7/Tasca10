# Binario a Decimal

binario = int(input("número en binario: "))

decimal = 0
i = 0
while (binario>0):
    digito  = binario%10
    binario = int(binario//10)
    decimal = decimal+digito*(2**i)
    i = i+1
# SALIDA
print("en decimal: ",decimal)
