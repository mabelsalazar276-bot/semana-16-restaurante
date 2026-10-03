from typing import List, Optional

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Fachada de datos y reglas necesarias para la primera interfaz gráfica."""

    def __init__(self, archivo_servicio: type[ArchivoServicio] = ArchivoServicio) -> None:
        self._archivo_servicio = archivo_servicio
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []

    def cargar_datos(self) -> None:
        self._productos = self._archivo_servicio.cargar_productos()
        self._usuarios = self._archivo_servicio.cargar_usuarios()
        self._ventas = self._archivo_servicio.cargar_ventas()

    def validar_acceso(self, nombre_usuario: str, contrasena: str) -> Optional[Usuario]:
        """Valida el acceso comparando el nombre de usuario y su contraseña."""
        nombre_usuario_normalizado = nombre_usuario.strip().lower()
        for usuario in self._usuarios:
            if (
                usuario.nombre_usuario.lower() == nombre_usuario_normalizado
                and usuario.contrasena == contrasena.strip()
            ):
                return usuario
        return None

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    def recargar_productos(self) -> List[Producto]:
        self._productos = self._archivo_servicio.cargar_productos()
        return self.listar_productos()

    def registrar_producto(
        self,
        id_producto: int,
        nombre: str,
        precio: float,
        categoria: str,
        stock: int,
    ) -> Producto:
        if any(producto.id_producto == int(id_producto) for producto in self._productos):
            raise ValueError("Ya existe un producto con ese identificador.")

        producto = Producto(id_producto, nombre, precio, categoria, stock)
        self._productos.append(producto)
        self._guardar_productos()
        return producto

    def buscar_producto(self, id_producto: int) -> Optional[Producto]:
        id_buscado = int(id_producto)
        return next(
            (producto for producto in self._productos if producto.id_producto == id_buscado),
            None,
        )

    def actualizar_producto(
        self,
        id_producto: int,
        nombre: str,
        precio: float,
        categoria: str,
        stock: int,
    ) -> Producto:
        producto = self.buscar_producto(id_producto)
        if producto is None:
            raise ValueError("No existe un producto con ese identificador.")

        producto_actualizado = Producto(id_producto, nombre, precio, categoria, stock)
        posicion = self._productos.index(producto)
        self._productos[posicion] = producto_actualizado
        self._guardar_productos()
        return producto_actualizado

    def eliminar_producto(self, id_producto: int) -> None:
        producto = self.buscar_producto(id_producto)
        if producto is None:
            raise ValueError("No existe un producto con ese identificador.")

        self._productos.remove(producto)
        self._guardar_productos()

    def _guardar_productos(self) -> None:
        if not self._archivo_servicio.guardar_productos(self._productos):
            raise OSError("No se pudo guardar el catálogo de productos.")

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    def buscar_usuario(self, id_usuario: int) -> Optional[Usuario]:
        id_buscado = int(id_usuario)
        return next(
            (usuario for usuario in self._usuarios if usuario.id_usuario == id_buscado),
            None,
        )

    def registrar_usuario(
        self,
        nombre: str,
        apellido: str,
        nombre_usuario: str,
        contrasena: str,
        correo_electronico: str,
        fecha_nacimiento: str,
        rol: str,
        usuario_actual: Usuario,
    ) -> Usuario:
        self._exigir_administrador(usuario_actual)
        self._validar_rol_gestionable(rol)
        nombre_usuario_normalizado = nombre_usuario.strip().casefold()
        correo_normalizado = correo_electronico.strip().casefold()
        if any(usuario.nombre_usuario.casefold() == nombre_usuario_normalizado for usuario in self._usuarios):
            raise ValueError("Ese nombre de usuario ya está registrado.")
        if any(usuario.correo_electronico.casefold() == correo_normalizado for usuario in self._usuarios):
            raise ValueError("Ese correo electrónico ya está registrado.")

        siguiente_id = max((usuario.id_usuario for usuario in self._usuarios), default=0) + 1
        usuario = Usuario(
            siguiente_id,
            nombre,
            apellido,
            nombre_usuario,
            contrasena,
            correo_electronico,
            fecha_nacimiento,
            rol,
        )
        usuarios_actualizados = [*self._usuarios, usuario]
        if not self._archivo_servicio.guardar_usuarios(usuarios_actualizados):
            raise OSError("No se pudo guardar el usuario en usuarios.json.")
        self._usuarios = usuarios_actualizados
        return usuario

    def actualizar_usuario(
        self,
        id_usuario: int,
        nombre: str,
        apellido: str,
        nombre_usuario: str,
        contrasena: str,
        correo_electronico: str,
        fecha_nacimiento: str,
        rol: str,
        usuario_actual: Usuario,
    ) -> Usuario:
        self._exigir_administrador(usuario_actual)
        usuario = self.buscar_usuario(id_usuario)
        if usuario is None:
            raise ValueError("No existe un usuario con ese identificador.")
        if usuario.id_usuario == usuario_actual.id_usuario:
            raise ValueError("No puede modificar la cuenta administradora activa.")
        self._validar_rol_gestionable(rol)

        nombre_usuario_normalizado = nombre_usuario.strip().casefold()
        correo_normalizado = correo_electronico.strip().casefold()
        if any(
            item.id_usuario != usuario.id_usuario
            and item.nombre_usuario.casefold() == nombre_usuario_normalizado
            for item in self._usuarios
        ):
            raise ValueError("Ese nombre de usuario ya está registrado.")
        if any(
            item.id_usuario != usuario.id_usuario
            and item.correo_electronico.casefold() == correo_normalizado
            for item in self._usuarios
        ):
            raise ValueError("Ese correo electrónico ya está registrado.")

        usuario_actualizado = Usuario(
            usuario.id_usuario,
            nombre,
            apellido,
            nombre_usuario,
            contrasena or usuario.contrasena,
            correo_electronico,
            fecha_nacimiento,
            rol,
        )
        usuarios_actualizados = [
            usuario_actualizado if item.id_usuario == usuario.id_usuario else item
            for item in self._usuarios
        ]
        if not self._archivo_servicio.guardar_usuarios(usuarios_actualizados):
            raise OSError("No se pudo actualizar el usuario en usuarios.json.")
        self._usuarios = usuarios_actualizados
        return usuario_actualizado

    def eliminar_usuario(self, id_usuario: int, usuario_actual: Usuario) -> None:
        self._exigir_administrador(usuario_actual)
        usuario = self.buscar_usuario(id_usuario)
        if usuario is None:
            raise ValueError("No existe un usuario con ese identificador.")
        if usuario.id_usuario == usuario_actual.id_usuario:
            raise ValueError("No puede eliminar la cuenta administradora activa.")

        usuarios_actualizados = [
            item for item in self._usuarios if item.id_usuario != usuario.id_usuario
        ]
        if not self._archivo_servicio.guardar_usuarios(usuarios_actualizados):
            raise OSError("No se pudo eliminar el usuario de usuarios.json.")
        self._usuarios = usuarios_actualizados

    def _validar_rol_gestionable(self, rol: str) -> None:
        rol_normalizado = rol.strip().casefold()
        if rol_normalizado not in {"empleado", "mesero", "cliente"}:
            raise ValueError("Solo se pueden registrar empleados o clientes.")

    def _exigir_administrador(self, usuario_actual: Usuario) -> None:
        if (
            not any(usuario is usuario_actual for usuario in self._usuarios)
            or usuario_actual.rol.casefold() != "administrador"
        ):
            raise PermissionError(
                "Solo un administrador puede registrar, actualizar o eliminar usuarios."
            )

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)

    def listar_ventas(self) -> List[Venta]:
        return list(self._ventas)

    def registrar_venta(self, usuario_id: int, producto_id: int) -> Venta:
        usuario = next(
            (item for item in self._usuarios if item.id_usuario == int(usuario_id)),
            None,
        )
        if usuario is None:
            raise ValueError("Seleccione un usuario registrado.")

        producto = self.buscar_producto(producto_id)
        if producto is None:
            raise ValueError("Seleccione un producto registrado.")

        venta = Venta(usuario.id_usuario, producto.id_producto)
        ventas_actualizadas = [*self._ventas, venta]
        if not self._archivo_servicio.guardar_ventas(ventas_actualizadas):
            raise OSError("No se pudo guardar la venta en ventas.json.")
        self._ventas = ventas_actualizadas
        return venta
