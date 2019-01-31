nome = input('Digite seu nome completo: ').strip()
print('{} {}'.format(nome.split(' ')[0], nome.split(' ')[len(nome.split(' '))-1]))
