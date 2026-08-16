from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n===== REGISTRAR PRODUCTO =====")
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    try:
        precio = float(input("Precio: "))
        if precio < 0:
            print("\n❌ El precio no puede ser negativo.")
            return
    except ValueError:
        print("\n❌ Ingrese un valor numérico válido para el precio.")
        return

    producto = Producto(codigo, nombre, categoria, precio)

    if restaurante.registrar_producto(producto):
        print("\n✅ Producto registrado correctamente.")
    else:
        print("\n❌ Ya existe un producto con ese código.")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n===== BUSCAR PRODUCTO =====")
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    if producto:
        print(f"\n✅ Producto encontrado:\n{producto.mostrar_informacion()}")
    else:
        print("\n❌ No se encontró ningún producto con ese código.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n===== ACTUALIZAR PRODUCTO =====")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    producto_existente = restaurante.buscar_producto(codigo)
    if not producto_existente:
        print("\n❌ No se encontró ningún producto con ese código.")
        return

    print(f"Actual: {producto_existente.mostrar_informacion()}")
    nuevo_nombre = input("Nuevo nombre: ").strip()
    nueva_categoria = input("Nueva categoría: ").strip()
    try:
        nuevo_precio = float(input("Nuevo precio: "))
        if nuevo_precio < 0:
            print("\n❌ El precio no puede ser negativo.")
            return
    except ValueError:
        print("\n❌ Ingrese un valor numérico válido para el precio.")
        return

    if restaurante.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio):
        print("\n✅ Producto actualizado correctamente.")
    else:
        print("\n❌ No se pudo actualizar el producto.")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n===== ELIMINAR PRODUCTO =====")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("\n✅ Producto eliminado correctamente.")
    else:
        print("\n❌ No se encontró un producto con ese código.")


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("\nNo existen productos registrados.")
        return

    print("\n========== PRODUCTOS ==========\n")
    for producto in productos:
        print(producto.mostrar_informacion())


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n===== REGISTRAR USUARIO =====")
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo electrónico: ").strip()

    usuario = Usuario(identificacion, nombre, correo)

    if restaurante.registrar_usuario(usuario):
        print("\n✅ Usuario registrado correctamente.")
    else:
        print("\n❌ Ya existe un usuario con esa identificación.")


def listar_usuarios(restaurante: Restaurante) -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("\nNo existen usuarios registrados.")
        return

    print("\n========== USUARIOS ==========\n")
    for usuario in usuarios:
        print(usuario.mostrar_informacion())


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n===== CATEGORÍAS ÚNICAS (CONJUNTO) =====")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
    else:
        for categoria in categorias:
            print(f"- {categoria}")


def main() -> None:
    restaurante = Restaurante()

    # Tupla: Opciones estables del menú principal
    opciones_menu: tuple = (
        "1. Registrar producto",
        "2. Buscar producto",
        "3. Actualizar producto",
        "4. Eliminar producto",
        "5. Listar productos",
        "6. Registrar usuario",
        "7. Listar usuarios",
        "8. Mostrar categorías",
        "9. Salir"
    )

    # Diccionario: Relaciona cada opción del menú con su respectiva función
    acciones_menu = {
        "1": lambda: registrar_producto(restaurante),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante),
        "4": lambda: eliminar_producto(restaurante),
        "5": lambda: listar_productos(restaurante),
        "6": lambda: registrar_usuario(restaurante),
        "7": lambda: listar_usuarios(restaurante),
        "8": lambda: mostrar_categorias(restaurante)
    }

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        for opcion in opciones_menu:
            print(opcion)
        print("----------------------------------------")

        eleccion = input("\nSeleccione una opción: ").strip()

        if eleccion == "9":
            print("\n¡Gracias por utilizar el sistema!")
            break
        elif eleccion in acciones_menu:
            acciones_menu[eleccion]()
        else:
            print("\n❌ Opción no válida.")


if __name__ == "__main__":
    main()