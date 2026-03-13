import tkinter as tk
from tkinter import ttk, messagebox
from modelos.vehiculos import Vehiculo

class AppGaraje(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Sistema de Gestión de Garaje")
        self.geometry("650x600")
        
        # Color de fondo suave para la ventana principal
        self.configure(bg="#f0f0f0")

        self._crear_componentes()

    def _crear_componentes(self):
        # --- ENCABEZADO CON CARRITO (TEXTO UNICODE) ---
        self.lbl_icono = tk.Label(self, text="🚗", font=("Arial", 60), bg="#f0f0f0")
        self.lbl_icono.pack(pady=(20, 0))
        
        self.lbl_titulo = tk.Label(self, text="REGISTRO DE GARAJE", 
                                   font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
        self.lbl_titulo.pack(pady=(0, 20))

        # --- CONTENEDOR DEL FORMULARIO ---
        frame_form = tk.LabelFrame(self, text=" Ingresar Datos ", font=("Arial", 10, "bold"),
                                   padx=20, pady=20, bg="white", relief="flat", highlightbackground="#ccc", highlightthickness=1)
        frame_form.pack(fill="x", padx=50, pady=10)

        # Campos de texto
        tk.Label(frame_form, text="Placa:", bg="white").grid(row=0, column=0, sticky="e", pady=8)
        self.txt_placa = tk.Entry(frame_form, font=("Arial", 11))
        self.txt_placa.grid(row=0, column=1, columnspan=2, sticky="we", padx=10)

        tk.Label(frame_form, text="Marca:", bg="white").grid(row=1, column=0, sticky="e", pady=8)
        self.txt_marca = tk.Entry(frame_form, font=("Arial", 11))
        self.txt_marca.grid(row=1, column=1, columnspan=2, sticky="we", padx=10)

        tk.Label(frame_form, text="Propietario:", bg="white").grid(row=2, column=0, sticky="e", pady=8)
        self.txt_propietario = tk.Entry(frame_form, font=("Arial", 11))
        self.txt_propietario.grid(row=2, column=1, columnspan=2, sticky="we", padx=10)

        # --- BOTONES SEPARADOS ---
        # Botón Registrar (Verde)
        self.btn_registrar = tk.Button(frame_form, text="✅ Registrar", 
                                       command=self._evento_registrar,
                                       bg="#28a745", fg="white", font=("Arial", 10, "bold"),
                                       width=15, cursor="hand2")
        self.btn_registrar.grid(row=3, column=1, pady=20, padx=10)

        # Botón Limpiar (Gris)
        self.btn_limpiar = tk.Button(frame_form, text="🧹 Limpiar", 
                                     command=self._limpiar_campos,
                                     bg="#6c757d", fg="white", font=("Arial", 10, "bold"),
                                     width=15, cursor="hand2")
        self.btn_limpiar.grid(row=3, column=2, pady=20, padx=10)

        # --- TABLA DE REGISTROS ---
        columnas = ("placa", "marca", "propietario")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=8)
        
        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")
        
        # Ajustar ancho de columnas
        self.tabla.column("placa", width=100, anchor="center")
        self.tabla.column("marca", width=150, anchor="center")
        self.tabla.column("propietario", width=200, anchor="center")
        
        self.tabla.pack(fill="both", expand=True, padx=50, pady=20)

    def _evento_registrar(self):
        p = self.txt_placa.get()
        m = self.txt_marca.get()
        pr = self.txt_propietario.get()

        if p and m and pr:
            nuevo_vehiculo = Vehiculo(p, m, pr)
            self.servicio.registrar_vehiculo(nuevo_vehiculo)
            self._actualizar_tabla()
            self._limpiar_campos()
            messagebox.showinfo("Éxito", "Vehículo registrado en el sistema")
        else:
            messagebox.showwarning("Atención", "Por favor completa todos los campos")

    def _actualizar_tabla(self):
        # Limpiar la tabla antes de volver a llenar
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Llenar con los datos del servicio
        for v in self.servicio.obtener_vehiculos():
            self.tabla.insert("", "end", values=(v.placa, v.marca, v.propietario))

    def _limpiar_campos(self):
        self.txt_placa.delete(0, tk.END)
        self.txt_marca.delete(0, tk.END)
        self.txt_propietario.delete(0, tk.END)
        self.txt_placa.focus()
        