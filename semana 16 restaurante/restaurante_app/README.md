# Sabores de Casa By Mabela

**Autora:** Mabela del Cisne Salazar Ren
**Entrega:** Semana 16

## Descripción

Sabores de Casa By Mabela es una aplicación de escritorio hecha en Python con Tkinter/ttk. Esta versión continúa el trabajo de semanas anteriores: conserva el inicio de sesión, la navegación, la gestión de productos y las ventas, y amplía la gestión administrativa de usuarios mediante eventos.

El código mantiene responsabilidades separadas entre archivos JSON, modelos, servicios, interfaz y punto de entrada. La interfaz recibe las acciones; `RestauranteServicio` aplica las reglas y `ArchivoServicio` lee o guarda los datos.

## Estructura

```text
restaurante_app/
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── assets/
│   ├── icono_inicio.xbm
│   ├── icono_productos.xbm
│   ├── icono_usuarios.xbm
│   ├── icono_ventas.xbm
│   └── logo.png.jpg
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   ├── restaurante.py
│   └── restaurante_servicio.py
└── ui/
    ├── __init__.py
    ├── estilos.py
    ├── imagenes.py
    ├── login_view.py
    ├── main_view.py
```

## Funcionamiento por componentes

- **Modelos:** describen productos, usuarios y ventas con sus referencias y fecha.
- **Servicios:** comprueban las operaciones permitidas y guardan la información en los JSON correspondientes.
- **Interfaz:** reúne la navegación, formularios, selectores y tablas, con una paleta lila y blanca. El logotipo `logo.png.jpg` aparece en la pantalla de inicio de sesión y en el encabezado del panel; los recursos gráficos están en `assets/`.
- **Inicio:** resume cuántos usuarios, platos y ventas hay registrados.
- **Ejecución:** `main.py` crea la ventana, carga los datos y presenta el login.

## Archivos de datos

La información utilizada por el programa se encuentra en la carpeta `datos/`:

- `productos.json`: catálogo disponible.
- `usuarios.json`: usuarios habilitados para ingresar.
- `ventas.json`: ventas registradas con identificadores de usuario y producto, y fecha/hora ISO.

Las rutas de estos archivos y de los recursos gráficos se forman con `pathlib` tomando como referencia la ubicación del código; la aplicación no depende de una ruta absoluta ni de la carpeta desde la que se ejecute.

## Ventas y flujo de eventos

En **Ventas** se elige un usuario y un plato en los selectores y se pulsa **Registrar venta**. El botón usa `command=` para llamar al callback de la vista; este recoge las opciones y solicita la operación a `RestauranteServicio`. El servicio valida ambas referencias y usa `ArchivoServicio` para guardar en `ventas.json`. Si se registra correctamente, la tabla se actualiza y la interfaz confirma el resultado. Al abrir el programa, se recupera el historial guardado.

Secuencia del evento: acción del usuario → botón `command=` → callback → servicio → persistencia JSON → tabla y mensaje de respuesta.

## Operaciones de productos

La sección **Productos** contiene el menú de platos de muestra: encebollado, ceviche de camarón, llapingachos, seco de pollo, jugo de naranjilla y tres leches. El formulario permite registrar, consultar, actualizar o eliminar sus datos, incluidos precio y existencias.

- **Registrar:** crea un producto nuevo.
- **Cargar / Consultar:** busca un producto mediante su ID y muestra sus datos en el formulario.
- **Actualizar:** reemplaza la información del producto seleccionado por su ID.
- **Eliminar:** retira el producto del catálogo.

Las acciones del menú se procesan mediante `RestauranteServicio`; la vista no modifica directamente `productos.json`. Después de cada operación, vuelve a consultar los datos y refresca la tabla. Para eliminar un plato solicita confirmación.

## Gestión de usuarios y eventos

Solo una sesión de **Administrador** puede acceder a **Usuarios**. Desde el formulario puede registrar, actualizar y eliminar cuentas de **Empleado** y **Cliente**; el Treeview muestra ID, nombre, cuenta y rol, sin contraseñas. Al seleccionar una fila, `<<TreeviewSelect>>` busca el objeto por su ID a través de `RestauranteServicio` y carga sus datos en el formulario. La contraseña se deja vacía al editar para conservar la actual, salvo que se ingrese una nueva.

Los botones usan `command=` para registrar, actualizar, eliminar y limpiar. Los eventos `bind()` implementan `<Return>` como atajo para registrar, `<Escape>` para limpiar el formulario y cancelar la selección, y `<<ComboboxSelected>>` para responder al cambio de rol. Los callbacks coordinan la interfaz; las reglas de validación y la persistencia permanecen en `RestauranteServicio`. El servicio también impide modificar o eliminar la cuenta del administrador que inició sesión.

El modelo `Usuario` persiste el atributo `rol` (`Administrador`, `Empleado` o `Cliente`) en `usuarios.json`. Al cargar datos anteriores, también reconoce el campo `rango` y convierte el rol histórico `Mesero` a `Empleado`.

## Cómo iniciar la aplicación

Requiere Python 3.9 o posterior y Tkinter/Tcl-Tk. Desde la carpeta `restaurante_app`, instala Pillow en el entorno de Python que utilizarás y ejecuta la aplicación:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

Si clonas el repositorio desde GitHub, primero entra en `restaurante_app` (`cd restaurante.semana15/restaurante_app` desde la carpeta en la que clonaste el repositorio). Se recomienda crear un entorno virtual antes de instalar las dependencias; los pasos para Windows, macOS y Linux están en el README de la raíz.

## Credenciales de demostración

```text
Usuario: admin
Contraseña: admin123

Usuario: mesero
Contraseña: mesero2026
```

Las contraseñas se almacenan como texto simple en el JSON; esta es una aplicación docente, no un sistema de autenticación para producción.

## Verificación de sintaxis

Para revisar que los archivos Python sean válidos, utiliza:

```bash
python -m compileall -q main.py modelos servicios ui
```

## Comprobación de la Semana 16

1. Iniciar `main.py` e ingresar como administrador para abrir la gestión de usuarios.
2. Registrar un Empleado o Cliente, seleccionar una fila para cargar sus datos, actualizarla y probar la eliminación confirmada.
3. Probar `Enter`, `Escape` y el cambio de rol en el Combobox; verificar que no se elimine ni modifique la cuenta administrativa activa.
4. Confirmar que los cambios quedan en `datos/usuarios.json`, cerrar y volver a iniciar sesión para comprobar que se conservan.
5. Comprobar que Productos y Ventas continúan disponibles y funcionando.