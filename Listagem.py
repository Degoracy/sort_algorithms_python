listagem = ('Lápis', 1.99,
            'Borracha', 2,
            'Mochila', 200.00,
            'Caderno', 15.00,
            'Caneta', 3.00,
            'Livro', 50.00,)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('_' * 40)
