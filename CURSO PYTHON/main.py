n1 = int(input ('''Digite o primeiro número: '''))

for n1_checked in range(10):
    if n1 > 10:
        n1 = int(input('''Seu número é muio grande, digite um numero menor que 10: '''))
    else:
        break

n2 = int(input('''Agora digite o número final: '''))
for n2_checked in range(10):
    if n2 > 1000:
        n2 = int(input('''Esse número é muito grande, digite um número menor que 1000:  '''))
    else:
        break

n3 = int(input(f'''Agora escreva de quantos em quantos números vai ser mostrado de {n1} a {n2}:  '''))
for n3_checked in range(10):
    if n3 > 100:
        n3 = int(input(f'''Esse número é grande demais!, Digite um número menor que 100:  '''))
    else:
        break

for final in range(n1, n2, n3):
    print(final)