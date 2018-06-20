def b9876543210(valor): #Ok
    dec = int(valor/10)
    uni = valor%10
    if dec > 0:
        resultado = 10*'0' + 10*dec*'0'
        resultado = list(resultado)
        resultado[(-dec*10)-uni-1] = '1'
        resultado = ''.join(resultado)
    else:
        resultado = 10*'0'
        resultado = list(resultado)
        resultado[-uni-1] = '1'
        resultado = ''.join(resultado)

    return resultado

def bcd8642(valor): #Ok
    uni = valor%10
    uni = bin(uni)
    uni = uni[2:]
    dec = int(valor/10)

    if dec > 0:
        resultado = bin(dec) + ' ' + uni
        resultado = resultado[2:]
    else:
        resultado = uni

    return resultado

def aiken(valor):
    pass

def bcd8642v(valor):
    pass

def ibm(valor): #Ok
    uni = valor%10
    if uni == 0:
        uni = '1010'
    else:
        uni = bin(uni)
        uni = uni[2:]
    dec = int(valor/10)

    if dec > 0:
        resultado = bin(dec) + ' ' + uni
        resultado = resultado[2:]
    else:
        resultado = uni

    return resultado

def excesso3(valor): #Ok
    uni = valor%10
    uni = bin(uni)
    uni = bin(int(uni,2)+3)

    dec = int(valor/10)
    if dec > 0:
        dec = bin(dec)
        dec = bin(int(dec,2)+3)
        resultado = dec + ' ' + uni[2:]
        resultado = resultado
    else:
        resultado = uni

    return resultado[2:]

def gray(valor): #ok
#https://www.youtube.com/watch?v=cF-Q5j7RUEw
    bin_ori = bin(valor)
    bin_ori = bin_ori[2:]
    resultado = []
    resultado.append(bin_ori[0])
    for i in range(len(bin_ori)-1):
        if bin_ori[i] == bin_ori[i+1]:
            resultado.append('0')
        else:
            resultado.append('1')
    resultado = ''.join(resultado)

    return resultado


def johnson(valor): #Ok
    if valor == 0: return '0'

    resultado = 50*'0'
    resultado = list(resultado)

    if valor <= 50:
        for i in range(valor):
            resultado[-i-1] = '1'
    else:
        dif = valor - 50
        for i in range(50):
            resultado[-i-1] = '1'
        for i in range(dif):
            resultado[-i-1] = '0'

    resultado = ''.join(resultado)

    return resultado

#print(nome_da_funcao(valor))
