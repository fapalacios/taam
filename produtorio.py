#calcular produtorio de uma lista

lista = [1,2,3,4]

it = iter(lista)
product = next(it)

while(True):
    try: 
       product *= next(it)
    except StopIteration as err:
        break
print(product)