import os
from funciones import *
from funciones_compras import *
from funciones_recuperatorio import *

flag_case_1 = False
flag_case_7 = False

running = True

while running:
    os.system('cls')

    match(crear_menu_opciones(['   *** Menu principal ***   ',
                               '1- Cargar datos desde archivo',
                               '2- Listar cantidad por marca',
                               '3- Listar insumos por marca',
                               '4- Buscar insumo por característica',
                               '5- Listar insumos ordenados',
                               '6- Realizar compras',
                               '7- Guardar en formato JSON',
                               '8- Leer desde formato JSON',
                               '9- Actualizar precios',
                               '10- Salir del programa',
                               '11- Agregar insumo',
                               '12 - exportar archivo',
                               '13 - stock por marca',
                               '14 - productos con bajo stock'])):

        case '1':
            flag_case_1 = True

            insumos = convertir_csv_a_lista_diccionarios('insumos.csv')

            lista_con_key_stock = list(map(lambda diccionario: agregar_clave_aleatoria(diccionario, 'STOCK', (0, 10)), insumos))

            escribir_diccionarios_en_csv(insumos, 'insumos.csv')

            insumos = convertir_csv_a_lista_diccionarios('insumos.csv')
            print('\n', 'Carga realizada con exito')
            os.system('pause')

        case '2':
            if flag_case_1:
                print()
                cantidad_por_marca = filtrar_y_contabilizar_lista_de_dicc(
                    insumos, 'MARCA')
                crear_lista(cantidad_por_marca, ['elemento', 'cantidad'], 25)

                os.system('pause')
            else:
                print()
                print(
                    'Antes de listar la cantidad de insumos por marca, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '3':
            if flag_case_1:
                print()
                marcas = filtrar_lista_dicc(insumos, 'MARCA')
                imprimir_insumos_por_marca(
                    marcas, insumos, 'MARCA', 'NOMBRE', 'PRECIO')

                os.system('pause')
            else:
                print()
                print(
                    'Antes de listar los insumos por marca, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '4':
            if flag_case_1:
                print()
                caracteristica_solicitada = input(
                    'Ingrese la caracteristica deseada: ')
                print()
                articulos_por_caracteristica = buscar_por_caracteristica(
                    insumos, caracteristica_solicitada, 'CARACTERISTICAS')
                crear_lista(articulos_por_caracteristica, [
                            'ID', 'NOMBRE', 'MARCA', 'PRECIO', 'CARACTERISTICAS'], 25)
                print()

                os.system('pause')
            else:
                print()
                print(
                    'Antes de buscar insumos por caracteristicas, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '5':
            if flag_case_1:
                lista_con_formato = dar_formato_a_lista_insumos(insumos)
                lista_ordenada = sorted(lista_con_formato, key=crear_orden)
                mostrar_productos(lista_ordenada)
                os.system('pause')
            else:
                print()
                print(
                    'Antes de listar los insumos ordenados, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '6':
            if flag_case_1:
                marcas = filtrar_lista_dicc(insumos, 'MARCA')
                productos_comprados = realizar_compras(insumos, marcas)
                total_de_compra = sumar_elementos_de_lista_dicc(
                    productos_comprados, 'SUBTOTAL')
                print(f'TOTAL: {total_de_compra:.2f}',
                      'Se ha generado una factura')
                os.system('pause')
                crear_factura(productos_comprados, total_de_compra)
            else:
                print()
                print(
                    'Antes de realizar compras, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '7':
            if flag_case_1:
                flag_case_7 = True

                alimentos = buscar_palabra_en_lista_dicc(
                    insumos, 'Alimento', 'NOMBRE')
                crear_json('alimentos.json', alimentos)
                print('Archivo JSON generado con exito')
                os.system('pause')
            else:
                print()
                print(
                    'Antes de guardar en formato JSON, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '8':
            if flag_case_7:
                alimentos = cargar_json_a_lista_dicc('alimentos.json')
                crear_lista(
                    alimentos, ['ID', 'NOMBRE', 'MARCA', 'PRECIO', 'CARACTERISTICAS'], 25)
                os.system('pause')
            else:
                print()
                print(
                    'Antes de leer el archivo JSON, debe cargarlo (opcion 7)')
                os.system('pause')

        case '9':
            if flag_case_1:
                insumos = strip_lista_dicc(insumos, 'PRECIO', '$')
                actualizar_precios(insumos)
                print('Se han actualizado los precios en el archivo CSV')
                os.system('pause')
            else:
                print()
                print(
                    'Antes de actualizar los precios, debe carfar los datos (opcion 1)')
                os.system('pause')

        case '10':
            confirmar_salida = input('Esta seguro que desea salir? (si/no): ')
            if confirmar_salida.lower() == 'si':
                os.system('cls')
                running = False

        case '11':
            insumo_nuevo = agregar_insumo()
            escribir_csv('insumos.csv', insumo_nuevo)

        case '12':
            if flag_case_1:
                    opcion = elegir_json_o_csv()
                    if opcion == 'json':
                        crear_json('datos_actualizados.json', insumos)
                    elif opcion == 'csv':
                        exportar_csv()
                    os.system('pause')
            else:
                print()
                print(
                    'Antes de exportar los datos, debe cargarlos (opcion 1)')
                os.system('pause')

        case '13':
            if flag_case_1:
                    pedirle_al_usuario_una_marca_y_mostrar_el_stock_total_de_los_productos_de_esa_marca(insumos)
                    os.system('pause')
            else:
                print()
                print(
                    'Antes de ver el stock por marca, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '14':
            if flag_case_1:
                    encontrar_productos_bajo_stock(insumos)
                    print('Se genero un archivo con una lista de los productos con bajo stock')
                    os.system('pause')
            else:
                print()
                print(
                    'Antes de ver que productos tienen bajo stock, debe cargar los datos (opcion 1)')
                os.system('pause')
