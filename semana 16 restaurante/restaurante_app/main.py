import tkinter as tk

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio
from ui.estilos import configurar_estilos
from ui.login_view import LoginView
from ui.main_view import MainView


def main() -> None:
    raiz = tk.Tk()
    raiz.title("Sabores de Casa By Mabela | Gestión")
    raiz.geometry("1180x760")
    raiz.minsize(980, 640)
    raiz.configure(background="#F7F4FA")
    configurar_estilos(raiz)

    servicio = RestauranteServicio()
    servicio.cargar_datos()

    def mostrar_login() -> None:
        for widget in raiz.winfo_children():
            widget.destroy()
        LoginView(raiz, servicio, mostrar_panel).pack(fill="both", expand=True)

    def mostrar_panel(usuario: Usuario) -> None:
        for widget in raiz.winfo_children():
            widget.destroy()
        MainView(raiz, servicio, usuario, mostrar_login).pack(fill="both", expand=True)

    mostrar_login()
    raiz.mainloop()


if __name__ == "__main__":
    main()