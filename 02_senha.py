#!/usr/bin/env python3

# Importa módulo para trabalhar com expressões regulares
import re

senha = input("Digite sua senha: ")

# Cria variável para diferença de tamanho entre o mínimo de caracteres da senha
# e a quantidade real digitada. Caso a senha digitada seja maior ou igual a 6,
# o mínimo exigido, é atribuído o valor 0.
dif_tam = 0 if len(senha) >= 6 else 6 - len(senha)

# Cria variável para contagem dos tipos de caracteres diferentes.
# Cada tipo é testado individualmente por meio de uma expressão regular.
tipos_diferentes = 0
if re.search('[0-9]', senha):
    tipos_diferentes += 1
if re.search('[a-z]', senha):
    tipos_diferentes += 1
if re.search('[A-Z]', senha):
    tipos_diferentes += 1
if re.search('[!@#$%^&*()-+]', senha):
    tipos_diferentes += 1

# A diferença entre os diferentes tipos exigidos e os que foram de fato inseridos
# é atribuída a uma variável. Aqui não usei uma expressão condicional, como para
# dif_tam, pois não há risco de ser atribuído um valor negativo.
dif_tipos = 4 - tipos_diferentes

# O resultado é apresentado após a expressão condicional averiguar qual diferença,
# se de tamanho ou de tipos diferentes, é a predominante.
print(dif_tam if dif_tam > dif_tipos else dif_tipos)
