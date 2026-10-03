import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio
from ui.imagenes import cargar_logo


class LoginView(ttk.Frame):
    """Pantalla de acceso simulado."""

    def __init__(
        self,
        master: tk.Misc,
        servicio: RestauranteServicio,
        al_ingresar: Callable[[Usuario], None],
    ) -> None:
        super().__init__(master, padding=0, style="App.TFrame")
        self.servicio = servicio
        self.al_ingresar = al_ingresar
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        campos = ttk.Frame(self, padding=(38, 34), style="LoginCard.TFrame")
        campos.grid(row=0, column=0, sticky="", padx=24, pady=30)
        campos.columnconfigure(0, weight=1)
        self.logo_restaurante = cargar_logo(self, (280, 153))
        ttk.Label(
            campos,
            image=self.logo_restaurante,
            anchor="center",
            style="LoginBrand.TLabel",
        ).grid(row=0, column=0, sticky="ew", pady=(0, 22))
        ttk.Label(campos, text="ACCESO DEL PERSONAL", style="LoginFormKicker.TLabel").grid(
            row=1, column=0, sticky="w", pady=(0, 8)
        )
        ttk.Label(campos, text="Inicio de sesión", style="LoginTitle.TLabel").grid(
            row=2, column=0, sticky="w"
        )
        ttk.Label(
            campos,
            text="Ingresa tus credenciales para continuar.",
            style="LoginSubtitle.TLabel",
        ).grid(row=3, column=0, sticky="w", pady=(7, 24))

        ttk.Label(campos, text="Usuario", style="LoginField.TLabel").grid(
            row=4, column=0, sticky="w", pady=(0, 6)
        )
        self.usuario_var = tk.StringVar()
        self.usuario_entry = ttk.Entry(campos, textvariable=self.usuario_var, width=34)
        self.usuario_entry.grid(row=5, column=0, sticky="ew", pady=(0, 18))

        ttk.Label(campos, text="Contraseña", style="LoginField.TLabel").grid(
            row=6, column=0, sticky="w", pady=(0, 6)
        )
        self.contrasena_var = tk.StringVar()
        self.contrasena_entry = ttk.Entry(
            campos, textvariable=self.contrasena_var, show="*", width=34
        )
        self.contrasena_entry.grid(
            row=7, column=0, sticky="ew", pady=(0, 24)
        )
        self.usuario_entry.bind("<Return>", self._manejar_enter)
        self.contrasena_entry.bind("<Return>", self._manejar_enter)

        ttk.Button(
            campos,
            text="Iniciar sesión",
            command=self._intentar_ingreso,
            style="Primary.TButton",
        ).grid(row=8, column=0, sticky="ew", ipady=4)
        ttk.Label(
            campos,
            text="Cuenta de demostración: admin",
            style="LoginHint.TLabel",
        ).grid(row=9, column=0, sticky="w", pady=(15, 0))
        self.usuario_entry.focus_set()

    def _manejar_enter(self, evento: tk.Event) -> str:
        self._intentar_ingreso()
        return "break"

    def _intentar_ingreso(self) -> None:
        if not self.usuario_var.get().strip() or not self.contrasena_var.get().strip():
            messagebox.showwarning("Datos incompletos", "Ingrese usuario y contraseña.")
            return

        usuario = self.servicio.validar_acceso(
            self.usuario_var.get(), self.contrasena_var.get()
        )
        if usuario is None:
            messagebox.showerror("Acceso denegado", "Las credenciales no son válidas.")
            return
        self.al_ingresar(usuario)
