nome = input('Digite seu nome: ').strip()
print(nome.lower().split(' ').__contains__('dos'))
print('dos' in nome.lower().split(' '))
