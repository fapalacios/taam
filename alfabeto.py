alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vogais = ['A', 'E', 'I', 'O', 'U']

for letra in alfabeto:
    if letra in vogais:
        print(letra, 'é vogal')
    else:
        print(letra, 'é consoante')
