test = '$HOLA$hola $$$ como $test_2$ andas $cosa$'


comando_enable = False
lista_letras = []
cmd = ''
for letra in test:
    
    if letra == '$':
        comando_enable = ~comando_enable
        if ~comando_enable:
            lista_letras.append(cmd)
            cmd = ''
    else: 
        if comando_enable:
            cmd += letra
        else:
            lista_letras.append(letra)

print(lista_letras)