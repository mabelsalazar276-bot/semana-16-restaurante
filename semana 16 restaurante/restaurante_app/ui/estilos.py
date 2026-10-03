from tkinter import ttk


LILA = "#624A75"
LILA_CLARO = "#EEE7F3"
ACENTO = "#9272A7"
FONDO = "#F7F4FA"
PANEL = "#FFFFFF"
TEXTO = "#302B36"
TEXTO_SUAVE = "#766F7D"
BORDE = "#E5DFEA"


def configurar_estilos(master: ttk.Widget) -> None:
    estilos = ttk.Style(master)
    if "clam" in estilos.theme_names():
        estilos.theme_use("clam")

    estilos.configure(".", font=("Segoe UI", 10))
    estilos.configure("TFrame", background=FONDO)
    estilos.configure("TLabel", background=FONDO, foreground=TEXTO)
    estilos.configure(
        "TButton",
        background=LILA_CLARO,
        foreground=LILA,
        padding=(12, 8),
        borderwidth=0,
        focusthickness=0,
    )
    estilos.map(
        "TButton",
        background=[("pressed", "#E3D9EC"), ("active", "#EAE2F0")],
    )
    estilos.configure("TEntry", padding=(9, 8), fieldbackground=PANEL, foreground=TEXTO)
    estilos.configure("TSeparator", background=BORDE)

    estilos.configure("App.TFrame", background=FONDO)
    estilos.configure("Header.TFrame", background=PANEL)
    estilos.configure("HeaderTitle.TLabel", background=PANEL, foreground=LILA, font=("Trebuchet MS", 18, "bold"))
    estilos.configure("HeaderMeta.TLabel", background=PANEL, foreground=TEXTO_SUAVE)
    estilos.configure("Header.TButton", background=PANEL, foreground=LILA, padding=(10, 7))
    estilos.map("Header.TButton", background=[("active", LILA_CLARO)])

    estilos.configure("Sidebar.TFrame", background=LILA)
    estilos.configure("SidebarHeading.TLabel", background=LILA, foreground="#DED5E8", font=("Segoe UI", 9, "bold"))
    estilos.configure("Nav.TButton", background=LILA, foreground="#FFFFFF", anchor="w", padding=(14, 11))
    estilos.map("Nav.TButton", background=[("active", "#765D8C")], foreground=[("active", "#FFFFFF")])
    estilos.configure("NavActive.TButton", background=ACENTO, foreground="#FFFFFF", anchor="w", padding=(14, 11))
    estilos.map("NavActive.TButton", background=[("active", "#7C5E91")])

    estilos.configure("PageTitle.TLabel", background=FONDO, foreground=LILA, font=("Trebuchet MS", 19, "bold"))
    estilos.configure("StatValue.TLabel", background=PANEL, foreground=LILA, font=("Segoe UI", 24, "bold"))
    estilos.configure("Muted.TLabel", background=FONDO, foreground=TEXTO_SUAVE)
    estilos.configure("Panel.TLabelframe", background=PANEL, bordercolor=BORDE, borderwidth=1, relief="solid")
    estilos.configure("Panel.TLabelframe.Label", background=PANEL, foreground=LILA, font=("Segoe UI", 10, "bold"))
    estilos.configure("Panel.TFrame", background=PANEL)
    estilos.configure("Primary.TButton", background=ACENTO, foreground="#FFFFFF", font=("Segoe UI", 10, "bold"))
    estilos.map("Primary.TButton", background=[("pressed", "#7C5E91"), ("active", "#806291")], foreground=[("active", "#FFFFFF")])
    estilos.configure("Danger.TButton", background="#F5E7E3", foreground="#983F32")
    estilos.map("Danger.TButton", background=[("active", "#EED4CD")])
    estilos.configure("Table.Treeview", background=PANEL, fieldbackground=PANEL, foreground=TEXTO, rowheight=31)
    estilos.map("Table.Treeview", background=[("selected", LILA)], foreground=[("selected", "#FFFFFF")])
    estilos.configure("Table.Treeview.Heading", background=LILA_CLARO, foreground=LILA, font=("Segoe UI", 9, "bold"), padding=(8, 8))
    estilos.map("Table.Treeview.Heading", background=[("active", "#E3D9EC")])

    estilos.configure("LoginCard.TFrame", background=PANEL, bordercolor=BORDE, borderwidth=1, relief="solid")
    estilos.configure("LoginBrand.TLabel", background=PANEL, foreground=LILA, font=("Trebuchet MS", 22, "bold"))
    estilos.configure("LoginTitle.TLabel", background=PANEL, foreground=LILA, font=("Segoe UI", 22, "bold"))
    estilos.configure("LoginSubtitle.TLabel", background=PANEL, foreground=TEXTO_SUAVE)
    estilos.configure("LoginFormKicker.TLabel", background=PANEL, foreground=ACENTO, font=("Segoe UI", 9, "bold"))
    estilos.configure("LoginField.TLabel", background=PANEL, foreground=TEXTO, font=("Segoe UI", 10, "bold"))
    estilos.configure("LoginHint.TLabel", background=PANEL, foreground=TEXTO_SUAVE, font=("Segoe UI", 9))
    estilos.configure("Panel.TLabel", background=PANEL, foreground=TEXTO)