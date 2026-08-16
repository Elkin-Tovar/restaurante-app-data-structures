from typing import List, Set, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """
    Clase encargada de administrar las colecciones y operaciones
    del restaurante (productos y usuarios).
    """

    def __init__(self) -> None:
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un producto validando que no exista un código duplicado.
        """
        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """
        Busca y retorna un producto según su código.
        """
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> bool:
        """
        Actualiza los datos de un producto existente.
        """
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nombre
            producto.categoria = categoria
            producto.precio = precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        """
        Elimina un producto de la lista según su código.
        """
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        """
        Retorna la lista de productos registrados.
        """
        return self.productos

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra un usuario validando que no exista una identificación duplicada.
        """
        for usuario_existente in self.usuarios:
            if usuario_existente.identificacion == usuario.identificacion:
                return False

        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[Usuario]:
        """
        Retorna la lista de usuarios registrados.
        """
        return self.usuarios

    def obtener_categorias_unicas(self) -> Set[str]:
        """
        Utiliza un conjunto (set) para obtener las categorías de los productos sin duplicados.
        """
        return {producto.categoria for producto in self.productos}