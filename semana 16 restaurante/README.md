# Sabores de Casa By Mabela

Aplicación de escritorio para gestionar productos, usuarios y ventas de un restaurante con Python y Tkinter.

## Requisitos

- Python 3.9 o posterior.
- Tkinter/Tcl-Tk instalado (se incluye normalmente con Python en Windows).
- Git para clonar el repositorio.

## Clonar e iniciar en Windows

En PowerShell, ejecuta:

```powershell
git clone https://github.com/mabelsalazar276-bot/restaurante.semana15.git
cd restaurante.semana15\restaurante_app
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

Si PowerShell bloquea la activación del entorno virtual, se puede invocar Python directamente sin activarlo:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

En macOS o Linux, después de clonar:

```bash
cd restaurante.semana15/restaurante_app
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

En algunas distribuciones de Linux, Tkinter se instala aparte del paquete de Python; instala el paquete `python3-tk` si aparece `No module named '_tkinter'`.

Las rutas de imágenes y JSON se construyen con `pathlib` desde la ubicación de los módulos del proyecto, así que no dependen del nombre de usuario ni de la carpeta donde se clone. Los datos iniciales están en `datos/` y los cambios se guardan allí.

Consulta [restaurante_app/README.md](./restaurante_app/README.md) para ver las funciones, roles y eventos implementados.
