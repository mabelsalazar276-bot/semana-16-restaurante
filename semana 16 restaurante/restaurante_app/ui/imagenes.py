import tkinter as tk
from pathlib import Path

from PIL import Image, ImageOps, ImageTk


RUTA_LOGO = Path(__file__).resolve().parent.parent / "assets" / "logo.png.jpg"


def cargar_logo(master: tk.Misc, tamaño: tuple[int, int]) -> ImageTk.PhotoImage:
    with Image.open(RUTA_LOGO) as imagen:
        logo = ImageOps.contain(
            imagen.convert("RGBA"),
            tamaño,
            method=Image.Resampling.LANCZOS,
        )
    return ImageTk.PhotoImage(logo, master=master)
