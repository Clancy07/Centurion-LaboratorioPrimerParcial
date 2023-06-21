from funciones import *
import random

def agregar_clave_aleatoria(diccionario, key, rango):
    diccionario[key] = random.randint(rango[0], rango[1])
    return diccionario

def escribir_diccionarios_en_csv(diccionarios, nombre_archivo):

    encabezados = diccionarios[0].keys()

    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=encabezados)

        writer.writeheader()

        for diccionario in diccionarios:
            writer.writerow(diccionario)

def obtener_clave(lista_dicc, key):
    lista = []
    for elemento in lista_dicc:
        lista.append(elemento[key])

    return lista

def listar(lista):
    for elemento in lista:
        print(elemento, end=', ')

def pedir_string_y_validar_en_lista(mensaje, lista, mensaje_error):
    flag = True

    while flag:
        aux = input(mensaje).lower()

        for elemento in lista:
            if aux == elemento:
                flag = False
                string_validado = aux
                break
        
        if flag:
            print(mensaje_error)
    
    return string_validado

def contabilizar_segun_key_recibida(string_a_buscar, lista_dicc, key1, key2):
    string_a_buscar = string_a_buscar.capitalize()
    total = 0
    for elemento in lista_dicc:
        if string_a_buscar == elemento[key1]:
            total += int(elemento[key2])

    return total

def pedirle_al_usuario_una_marca_y_mostrar_el_stock_total_de_los_productos_de_esa_marca(insumos):
    marcas = obtener_clave(insumos, 'MARCA')
    print('Marcas disponibles: ')
    listar(marcas)
    marcas_lower = pasar_lista_a_minuscula(marcas)
    marca_ingresada = pedir_string_y_validar_en_lista('\nIngrese la marca: ', marcas_lower, 'Marca inválida. Vuelva a ingresarla.')
    total_stock = contabilizar_segun_key_recibida(marca_ingresada, insumos, 'MARCA', 'STOCK')
    print('Stock total de productos de marca ' + marca_ingresada + ': ', total_stock)

def crear_lista_insumos_bajo_stock(insumos):
    insumos_bajo_stock = []
    for insumo in insumos:
        if int(insumo['STOCK']) <= 2:
            insumos_bajo_stock.append(insumo)

    return insumos_bajo_stock

def encontrar_productos_bajo_stock(insumos):
    insumos_bajo_stock = crear_lista_insumos_bajo_stock(insumos)
        
    insumos_bajo_stock = reducir_lista_dicc(insumos_bajo_stock, ['NOMBRE', 'STOCK'])

    nombre_archivo = 'productos_bajo_stock.txt'

    escribir_diccionarios_en_csv(insumos_bajo_stock, nombre_archivo)