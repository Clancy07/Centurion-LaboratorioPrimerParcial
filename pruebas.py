from funciones import *


def imprimir_lista_dicc(lista_dicc):
    for elemento in lista_dicc:
        print(elemento)


def pasar_lista_a_minuscula(lista):
    lista_retorno = []
    for elemento in lista:
        lista_retorno.append(elemento.lower())

    return lista_retorno


insumos = convertir_csv_a_lista_diccionarios('insumos.csv')


# marcas = filtrar_lista_dicc(insumos, 'MARCA')
# marcas_minusculas = pasar_lista_a_minuscula(marcas)
# marca_buscada = input('Ingrese el nombre de la marca deseada: ').lower()

# if marca_buscada in marcas_minusculas:
#     for insumo in insumos:
#         if marca_buscada == insumo['MARCA'].lower():
#             insumos_marca_solicitada.append(insumo)

# crear_lista(insumos_marca_solicitada, [
#             'ID', 'NOMBRE', 'MARCA', 'PRECIO', 'CARACTERISTICAS'], 30)
# id_solicitado = input('Ingrese el ID del producto que desea comprar: ')

# insumos_comprados = []
# for insumo in insumos_marca_solicitada:
#     if id_solicitado == insumo['ID']:
#         aux = insumo
#         aux['CANTIDAD'] = input('Ingrese la cantidad que desea comprar: ')
#         insumos_comprados.append(aux)


insumos_marca_solicitada = []
lista_compras = []
carrito_de_compras = []

while True:
    marcas = filtrar_lista_dicc(insumos, 'MARCA')
    marcas_minusculas = pasar_lista_a_minuscula(marcas)
    marca_buscada = input('Ingrese el nombre de la marca deseada: ').lower()
    if marca_buscada in marcas_minusculas:
        for insumo in insumos:
            if marca_buscada == insumo['MARCA'].lower():
                insumos_marca_solicitada.append(insumo)

    crear_lista(insumos_marca_solicitada, [
                'ID', 'NOMBRE', 'MARCA', 'PRECIO', 'CARACTERISTICAS'], 30)
    
    id_solicitado = input('Ingrese el ID del producto que desea comprar: ')

    insumos_comprados = []
    for insumo in insumos_marca_solicitada:
        if id_solicitado == insumo['ID']:
            aux = insumo
            aux['CANTIDAD'] = input('Ingrese la cantidad que desea comprar: ')
            insumos_comprados.append(aux)
    
    confirmacion_salir = input('Desea realizar otra compra? (si/no): ')
    if confirmacion_salir.lower() == 'no':
        carrito_de_compras.extend(insumos_comprados)
        break
    else:
        carrito_de_compras.extend(insumos_comprados)
        insumos_marca_solicitada = []

carrito_con_precio_final = []
for producto in carrito_de_compras:
    producto['PRECIO_TOTAL'] = str(float(producto['PRECIO'].strip('$')) * float(producto['CANTIDAD']))
    carrito_con_precio_final.append(producto)

precio_final = 0
for producto in carrito_con_precio_final:
    precio_final += float(producto['PRECIO_TOTAL'])

print(f'El total de compra es de: ${precio_final}')


