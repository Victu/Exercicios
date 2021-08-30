print('=' * 66)
print(' >>{:-^60}<<'.format("> SEQUÊNCIA DE FIBONACCI <"))
print('=' * 66)

Tt = int(input('Informe quantos termos quer mostrar: ')) #Tt -> Total de termos
pt = pt_st = x = 0  #pt -> Primeiro termo
st = 1  #st -> Segundo termo
repetir = ""
sair = False

print('----' * Tt)
while x <= Tt and not sair:
    pt = st
    st = pt_st
    pt_st = pt + st  #pt_st -> Soma do primeiro termo com o segundo termo
    print(st, end=", " if x < Tt else '...')
    x += 1

    if x == Tt:
        print('')
        print('----' * Tt)
        repetir = input('\nDeseja repetir? ')[0]
        if repetir in 'Nn':
            sair = True
        else:
            Tt = int(input('Informe quantos termos quer mostrar: '))
            print('----' * Tt)
            pt = pt_st = x = 0
            st = 1

print('-' * 66)
print('{:^60}'.format(' SEQUÊNCIA FINALIZADA.'))
