import os
from funciones import *

flag_case_1 = False

while True:
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
                               '10- Salir del programa'])):

        case '1':
            flag_case_1 = True
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
                caracteristica_solicitada = input('Ingrese la caracteristica deseada: ')
                print() 
                articulos_por_caracteristica = buscar_por_caracteristica(insumos, caracteristica_solicitada, 'CARACTERISTICAS')
                crear_lista(articulos_por_caracteristica, ['ID', 'NOMBRE', 'MARCA', 'PRECIO','CARACTERISTICAS'], 25)
                print()

                os.system('pause')
            else:
                print()
                print(
                    'Antes de buscar insumos por caracteristicas, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '5':
            if flag_case_1:
                mostrar_productos(insumos)
                os.system('pause')
            else:
                print()
                print(
                    'Antes de listar los insumos ordenados, debe cargar los datos (opcion 1)')
                os.system('pause')

        case '6':
            realizar_compras()

        case '10':
            confirmar_salida = input('Esta seguro que desea salir? (si/no): ')
            if confirmar_salida. lower == 'si':
                break
