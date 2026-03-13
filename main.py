from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppGaraje

def main():
    # Instanciamos el servicio (la lógica)
    servicio = GarajeServicio()
    
    # Pasamos el servicio a la interfaz (Inyección de dependencias básica)
    app = AppGaraje(servicio)
    
    # Iniciamos el bucle principal
    app.mainloop()

if __name__ == "__main__":
    main()
    