# Lista de la compra
# lista de las cantidades
# lista de precios

lista_de_la_compra = ['patatas', 'arroz', 'naranjas', 'mermelada', 'vino blanco']
lista_de_cantidades = ['2 kilos', '1 kilo', '4 kilos','1 bote','1 litro']
lista_de_precios = []

print("Mi lista de la compra")
for i in range(1, 5):
    print(lista_de_la_compra[i-1], lista_de_cantidades [i-1])

for item in lista_de_la_compra:
    print ("dame precio para", item)
    precio = float(input())
    lista_de_precios.append(precio)

suma=0
for num in lista_de_precios:
    suma=suma+float(num)

print(suma)



