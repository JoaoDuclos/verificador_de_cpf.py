while True:
    cpf = input('Digite o seu cpf: ')
    final = cpf[9:11]
    final_ver = []
    comeco = cpf[:9]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += int(cpf[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            final_ver += str(d)
    if final == ''.join(final_ver):
        print('Válido')
    else:
        print('Inválido')