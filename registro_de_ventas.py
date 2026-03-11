
venta = []

def registro():
    producto = input("\n introduce el nombre del producto: ")
    precio = int(input("\n introduce el precio c/u(sin puntos): "))
    cantidad = int(input("\n ingresa la cantidad: ")) 
    total = precio * cantidad
    

    number_venta = {
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad, 
        "total": total
    }
    venta.append(number_venta)
    print(f"producto vendido{producto} \n precio {precio} \n cantidad {cantidad} \n total venta {total}")

print("\n ---------MENU-----------\n 1. ingresar venta \n 2. salir y mostrar resumen")
op = input("\n ¿Que quieres hacer?: \n ")
    
while op == "1":
    registro()
    print("\n ---------MENU-----------\n 1. ingresar venta \n 2. salir y mostrar resumen")
    op = input("¿Que quieres hacer?: ")


print("\n resumen de compra\n ")
for i in venta:
    print(i)


#este es el ejemplo que hiciste
total_venta = sum(i['total'] for i in venta)
print(f"\n -------El total de la venta es: --------\n {total_venta} ")
