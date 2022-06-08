"""
Desafio 004
Problema: Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela.
Resolução do problema:
"""
n=input('Digite algo: ')
print(f'O valor primitivo desta variável é {type(n)}')
print(f'É número? {n.isnumeric()}')
print(f'é um dígito? {n.isdigit()}')
print(f'É um valor alphanúmerico? \033[32m{n.isalnum()}\033[m')
print(f'É um texto? \033[34m{n.isalpha()}\033[m')
print(f'É um valor decimal? \033[32m{n.isdecimal()}\033[m')
print(f'É um identificador? \033[35m{n.isidentifier()}\033[m')
print(f'Está em letra minúscula? \033[37m{n.islower()}\033[m')
print(f'Está em lestra maiúscula? \033[36m{n.isupper()}\033[m')
print(f'É uma tabela de impressão? \033[34m{n.isprintable()}\033[m')
print(f'É um espaço? \033[31m{n.isspace()}\033[m')
print(f'Está capitalizada ? \033[30m{n.istitle()}\033[m')