from random import randint
while 1:
    numero = randint(0, 5)
    print('-=-' * 20)
    jog = int(input('Digite um numero: '))
    if numero == jog:
        print('{} ACERTOU {}'.format('*-*' * 5, '*-*' * 5))
    else:
        print('{} PERDEU {}'.format('*-*'*5, '*-*'*5))
    print('-=-' * 20)
