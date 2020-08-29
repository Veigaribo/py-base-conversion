def to_base(val, origbase, newbase):

    # define funcoes interessantes

    def __get_decimal_value(charnumber):

        charnumber = charnumber[0].upper()

        if charnumber >= '0' and charnumber <= '9':
            return int(charnumber)
        else:
            if charnumber >= 'A' and charnumber <= 'Z':
                return 10 + ord(charnumber) - 65
            else:
                raise ValueError('Algarismo "{}" nao reconhecido'.format(charnumber))

    def __get_symbol(number):

        if number >= 0 and number <= 9:
            return str(number)
        else:
            if number <= 35:
                return chr(number - 10 + 65)
            else:
                raise ValueError('Numero {} nao representavel'.format(number))

    # converte valor original para base "10"

    decval = 0
    origbase_exp = len(val) - 1

    for char in val:
        # decimal_value corresponde a um unico digito
        decimal_value = __get_decimal_value(char)

        if decimal_value < origbase:
            decval += decimal_value * ( origbase ** origbase_exp )
            origbase_exp -= 1
        else:
            raise ValueError('Algarismo {} nao faz sentido para origbase {}'.format(char, origbase))

    # converte valor base 10 para nova base

    if newbase == 10:
        return decval, 10

    numarr = []

    aux = decval
    while aux >= newbase:
        numarr.append(aux % newbase)
        aux //= newbase

    numarr.append(aux)

    returnstr = ''.join([__get_symbol(n) for n in numarr[::-1]])

    return returnstr, newbase

# como os outros devem fazer algoritmos com entrada, processamento e saida, fiz isso.
if __name__ == '__main__':
    
    number = input('Numero, por favor: ').upper()
    base = int(input('Base original: '))
    print()

    print('Numero {}({}).'.format(number, base))
    print()

    newbase = int(input('Para qual base agora? '))
    print()
    print('Numero {}({}).'.format(*to_base(number, base, newbase)))