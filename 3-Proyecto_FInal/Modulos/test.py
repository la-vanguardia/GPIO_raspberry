dato = 0x00 + 32

if (dato>>7) == 1:
    dato = -1 * (dato & 0x7F)
    print(dato)
else:
    print(dato)