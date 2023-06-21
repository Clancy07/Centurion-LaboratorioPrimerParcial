from funciones import *
from datetime import datetime

# ---------------------------------------------------------------------------- REALIZAR COMPRAS ----------------------------------------------------------------------------
def realizar_compras(insumos, marcas):
    seguir_comprando = True

    productos_comprados = []



    while seguir_comprando:

        flag_marca_coincidente = False

        flag_id = True

        flag_cantidad = True

        producto_comprado = {}
        productos_coincidentes = []
        ids_coincidentes = []

        print('\nMARCAS DISPONIBLES:')
        for marca in marcas:
            print(marca, end=', ')

        marca_solicitada = input('\n\nIngrese la marca: ').lower()

        for insumo in insumos:
            if marca_solicitada == insumo['MARCA'].lower():
                flag_marca_coincidente = True
                productos_coincidentes.append(insumo)
                ids_coincidentes.append(insumo['ID'])

        
        if flag_marca_coincidente:
            pass
        else:
            print('\nNo hubieron coincidencias. Debera reingresar la marca: ')
            continue

        crear_lista(productos_coincidentes, ['ID', 'NOMBRE', 'MARCA', 'PRECIO', 'CARACTERISTICAS'], 25)

        while flag_id:
            aux_id = input('Ingrese el ID del producto que desee comprar: ')

            if aux_id in ids_coincidentes:
                id_solicitado = aux_id
                flag_id = False
            else:
                print('El ID no coincide.')

        while flag_cantidad:
            aux_cantidad = input('Ingrese la cantidad que desea comprar: ')

            if aux_cantidad.isdigit():
                cantidad = aux_cantidad
                flag_cantidad = False
            else:
                print('Cantidad invalida')

        producto_comprado['ID'] = id_solicitado
        producto_comprado['CANTIDAD'] = cantidad
        
        for producto in productos_coincidentes:
            if producto['ID'] == producto_comprado['ID']:
                producto_comprado['PRECIO'] = producto['PRECIO'].strip('$')
                producto_comprado['NOMBRE'] = producto['NOMBRE']
                producto_comprado['SUBTOTAL'] = float(producto_comprado['PRECIO']) * float(producto_comprado['CANTIDAD'])

        productos_comprados.append(producto_comprado)

        seguir_comprando = input('Desea seguir comprando? (si/no): ')
        if seguir_comprando.lower() == 'no':
            seguir_comprando = False
    
    return productos_comprados



# ---------------------------------------------------------------------------- TOTAL COMPRA ----------------------------------------------------------------------------
def sumar_elementos_de_lista_dicc(lista_dicc, key):
    total = 0
    for elemento in lista_dicc:
        total += elemento[key]

    return(total)



# ---------------------------------------------------------------------------- CREAR FACTURA ----------------------------------------------------------------------------
def crear_factura(lista_dicc, total):
    fecha_hora_actual = datetime.now()
    nombre_factura = fecha_hora_actual.strftime("%Y-%m-%d_%H-%M-%S")

    file = open(f'facturas\\factura_{nombre_factura}.txt', 'w')

    file.write("Factura\n\n")
    file.write("Productos\t\t\t\tCantidad\tSubtotal\n")
    file.write("----------------------------------------------------\n")
    for elemento in lista_dicc:
        file.write(f"{elemento['NOMBRE']}\t\t{elemento['CANTIDAD']}\t\t{elemento['SUBTOTAL']:.2f}\n")
    file.write("----------------------------------------------------\n")

    file.write(f"Total: {total:.2f}\n")

    file.close()

