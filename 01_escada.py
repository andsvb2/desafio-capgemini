#!/usr/bin/env python3

# Inicializa as variáveis com o tamanho da escada desejada pelo usuário e
# a quantidade de espaços necessária para começar a exibição.

tamanho = int(input('Qual o tamanho do objeto? '))
espacos = tamanho - 1

# Cria um laço do tamanho desejado para a escada com cada linha sendo calculada
# e exibida a partir das variaveis inicializadas tamanho e espacos.
# A variável espacos é atualizada logo após a exibição da linha.

for i in range(tamanho):
    print((" " * espacos) + ("*" * (tamanho - espacos)))
    espacos -= 1
