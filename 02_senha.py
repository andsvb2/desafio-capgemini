#!/usr/bin/env python3

# Importa módulo para trabalhar com expressões regulares
import re

# Cria variável para receber a senha digitada e, logo em seguida, calcula a
# diferença de tamanho entre o mínimo necessário de caracteres da senha e a
# quantidade real digitada. Caso a senha digitada seja maior ou igual a 6, o
# mínimo exigido, é atribuído o valor 0.
senha = input("Digite sua senha: ")
dif_tam = 0 if len(senha) >= 6 else 6 - len(senha)

# Cria variável para contagem dos tipos diferentes necessários de caracteres.
# Cada tipo é testado individualmente por meio de uma expressão regular. Ao
# final sobrará a quantidade faltante de tipos diferentes.
tipos_necessarios = 4
if re.search('[0-9]', senha):
    tipos_necessarios -= 1
if re.search('[a-z]', senha):
    tipos_necessarios -= 1
if re.search('[A-Z]', senha):
    tipos_necessarios -= 1
if re.search('[!@#$%^&*()-+]', senha):
    tipos_necessarios -= 1

# A expressão condicional avalia qual dos dois cenários é o correto: 1) se
# faltam mais caracteres de tipos diferentes, mesmo que o tamanho mínimo de
# senha tenha sido alcançado; 2) se é necessário completar o mínimo de
# caracteres, pois os diferentes tipos já estão presentes na senha. No primeiro
# caso o valor atribuído a tipos_necessarios será exibido, na segunda situação
# exibido o valor de dif_tam.
print(tipos_necessarios if tipos_necessarios > dif_tam else dif_tam)
