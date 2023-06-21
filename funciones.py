import csv, re, json

def crear_menu_opciones(lista_opciones):
    for opcion in lista_opciones:
        print(f'{opcion}')

    return input('ingrese una opcion: ')


def convertir_csv_a_lista_diccionarios(archivo_csv):
    lista_diccionarios = []

    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.DictReader(archivo)

        for linea in lector_csv:
            lista_diccionarios.append(linea)

    return lista_diccionarios


def filtrar_y_contabilizar_lista_de_dicc(lista_diccionarios, clave):
    lista_con_repetidos = []

    for elemento in lista_diccionarios:
        lista_con_repetidos.append(elemento[clave])

    lista_sin_repetidos = list(set(lista_con_repetidos))
    coleccion_retorno = []

    for elemento in lista_sin_repetidos:
        cantidad = lista_con_repetidos.count(elemento)
        dicc = {'elemento': elemento, 'cantidad': cantidad}
        coleccion_retorno.append(dicc)

    return coleccion_retorno


def crear_lista(lista_diccionarios, lista_claves, ancho_columna: int = 12):
    contador_columnas = 0

    # Encabezado
    for clave in lista_claves:
        contador_columnas += 1
        print(f'{clave.capitalize():<{ancho_columna}}', end='')
    print()
    print('-' * (ancho_columna * contador_columnas))

    # Elementos
    for diccionario in lista_diccionarios:
        for clave in lista_claves:
            elemento = diccionario.get(clave, '-')
            print(f'{elemento:<{ancho_columna}}', end='')
        print()


def reducir_lista_dicc(lista_diccionarios, lista_keys):
    coleccion_retorno = []
    for diccionario in lista_diccionarios:
        nuevo_diccionario = {}
        for key in lista_keys:
            if key in diccionario:
                nuevo_diccionario[key] = diccionario[key]
        coleccion_retorno.append(nuevo_diccionario)
    return coleccion_retorno


def filtrar_lista_dicc(lista_diccionarios, clave):
    lista_con_repetidos = []

    for diccionario in lista_diccionarios:
        lista_con_repetidos.append(diccionario[clave])

    lista_sin_repetidos = list(set(lista_con_repetidos))

    return lista_sin_repetidos


def imprimir_insumos_por_marca(lista_marcas, lista_dicc, key_titulo, key1, key2):
    for marca in lista_marcas:
        for insumo in lista_dicc:
            if insumo[key_titulo] == marca:
                print('-' * 30)
                print(marca, end='\n')
                print("{:<15s}{:<15s}".format(key1, key2))
                print("{:<15s}{:<15s}".format(insumo[key1], insumo[key2]))
                print('-' * 30, end='\n\n')


def imprimir_lista_dicc(lista_dicc):
    for elemento in lista_dicc:
        print(elemento)


def buscar_por_caracteristica(lista_diccionarios, caracteristica, key):
    resultados = []
    # Convertir la característica de búsqueda a minúsculas
    caracteristica_busqueda = caracteristica.lower()
    for diccionario in lista_diccionarios:
        # Obtener las características del diccionario
        caracteristicas = diccionario.get(key, '')
        # Dividir las características por el separador '~'
        caracteristicas_lista = caracteristicas.split('~')
        for carac in caracteristicas_lista:
            if caracteristica_busqueda == carac.lower():  # Comparar sin distinguir mayúsculas y minúsculas
                resultados.append(diccionario)
                break  # Romper el bucle si se encuentra una coincidencia
    return resultados

def mostrar_productos(lista_diccionarios):
    headers = ["ID", "Descripción", "Precio", "Marca", "Primera característica"]

    # Imprimir encabezados de tabla
    print("{:<10s}{:<35s}{:<10s}{:<25s}{:<20s}".format(*headers))
    print("-" * 100)

    for producto in lista_diccionarios:
        caracteristicas = producto['CARACTERISTICAS'].split('~')
        primer_caracteristica = caracteristicas[0] if caracteristicas else ''

        # Obtener valores de cada columna
        id_producto = str(producto['ID'])
        descripcion = producto['NOMBRE']
        precio = str(producto['PRECIO'])
        marca = producto['MARCA']

        # Imprimir fila de la tabla
        print("{:<10s}{:<35s}{:<10s}{:<25s}{:<20s}".format(id_producto, descripcion, precio, marca, primer_caracteristica))
    
    print("-" * 100)

def pasar_lista_a_minuscula(lista):
    lista_retorno = []
    for elemento in lista:
        lista_retorno.append(elemento.lower())

    return lista_retorno

def realizar_compras():
    insumos = convertir_csv_a_lista_diccionarios('insumos.csv')

    insumos_marca_solicitada = []
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

def dar_formato_a_lista_insumos(insumos):
    for insumo in insumos:
        caracteristicas = insumo['CARACTERISTICAS'].split('~')
        insumo['CARACTERISTICAS'] = caracteristicas[0]
        insumo['PRECIO'] = insumo['PRECIO'].strip('$')
    
    return insumos

def crear_orden(diccionario):
    return (diccionario["MARCA"], -float(diccionario["PRECIO"]))

def buscar_palabra_en_lista_dicc(lista_dicc, palabra, key):
    patron = re.compile(palabra)
    coicidencias = []

    for elemento in lista_dicc:
        match = patron.search(elemento[key])
        if match:
            coicidencias.append(elemento)

    return coicidencias

def crear_json(nombre_archivo, lista_dicc):
    archivo = open(nombre_archivo, 'w')
    archivo.write(json.dumps(lista_dicc, indent=4))
    archivo.close

def cargar_json_a_lista_dicc(nombre_json):
    file = open(nombre_json, 'r')
    contenido = file.read()
    lista_dicc = json.loads(contenido)
    file.close()

    return lista_dicc

def strip_lista_dicc(lista_dicc, key, str):
    for elemento in lista_dicc:
        elemento[key] = elemento[key].strip(str)

    return lista_dicc

def actualizar_precios(insumos):
    archivo_csv = 'insumos.csv'

    insumos_original = list(insumos)

    insumos_actualizados = list(map(lambda p: {**p, 'PRECIO': float(p['PRECIO']) * 1.084}, insumos))

    insumos_actualizados = insumos_original + insumos_actualizados

    with open(archivo_csv, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=insumos_actualizados[0].keys())
        writer.writeheader()
        writer.writerows(insumos_actualizados)

def escribir_csv(archivo, datos):
    with open(archivo, 'a', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv, delimiter=',')
        escritor.writerow([])
        escritor.writerow(datos)

def agregar_insumo():
    arcivo_insumos = 'insumos.csv'
    contador_lineas = 0

    with open(arcivo_insumos, 'r') as archivo:
        for linea in archivo:
            contador_lineas += 1

    archivo = 'marcas.txt'

    with open(archivo, 'r') as file:
        marcas = [line for line in file]

    print('Marcas disponibles: ')
    for marca in marcas:
        print(marca)

    marcas_lower = []
    nuevo_insumo = []
    nuevo_insumo.append(contador_lineas)

    for marca in marcas:
        marca = marca.strip('\n')
        marcas_lower.append(marca.lower())

    patron_precio = re.compile(r'\d+(\.\d+)?')


    flag_nombre = True
    flag_marca = True
    flag_precio = True

    caracteristicas = []

    while flag_nombre: 
        aux_nombre = input('Ingrese el nombre del producto: ')

        if aux_nombre.isalpha():
            flag_nombre = False
            nombre_ingresado = aux_nombre
        else:
            print('Nombre invalido. Vuelva a ingresarlo.')
    nuevo_insumo.append(nombre_ingresado)

    while flag_marca:
        aux_marca = input('Ingrese la marca: ').lower()

        for marca in marcas_lower:
            if aux_marca == marca:
                flag_marca = False
                marca_ingresada = aux_marca
                break

        if flag_marca:
            print('Marca inválida. Vuelva a ingresarla.')
    nuevo_insumo.append(marca_ingresada)

    while flag_precio:
        aux_precio = input('Ingrese el precio: ')
        match = patron_precio.search(aux_precio)
        if match:
            flag_precio = False
            precio_ingresado = aux_precio
        else:
            print('Precio invalido. Reingrese un precio valido.')
    nuevo_insumo.append(precio_ingresado)

    while len(caracteristicas) <= 2:
        caracteristica = input('Ingrese una caracteristica: ')
        if caracteristica == '':
            print('debe ingresar al menos una caracteristica')
        else:
            caracteristicas.append(caracteristica)
            if len(caracteristicas) <= 2:
                continuar = input('Desea ingresar una caracteristica mas? (si/no): ')
                if continuar.lower() == 'si':
                    pass
                else:
                    break
    caracteristicas_separadas = '~'.join(caracteristicas)
    nuevo_insumo.append(caracteristicas_separadas)
    
    return nuevo_insumo

def elegir_json_o_csv():
    opcion = 'error'

    while opcion == 'error':
        opcion = input('A que formato desea importar? (json/csv): ').lower()
        if opcion == 'json':
            pass
        elif opcion == 'csv':
            pass
        else:
            opcion = 'error'
            print('Opcion invalida')

    return opcion

def exportar_csv():
    with open('insumos.csv', 'r') as file:
        lector_csv = csv.reader(file)
        lineas = list(lector_csv)

    with open('datos_actualizados.csv', 'w', newline='') as archivo_nuevo:
        escritor_csv = csv.writer(archivo_nuevo)
        for fila in lineas:
            escritor_csv.writerow(fila)

