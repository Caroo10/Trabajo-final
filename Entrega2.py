import datetime
import json

class SistemaCitasPailaSalud:
    def _init_(self):
        self.usuarios = {}  
        self.citas = {}     
        self.atenciones = {}  
        self.admin_contraseña = "admin123"  

    def registrar_usuario(self, cedula, nombre, edad, telefono):
        """Registra un nuevo usuario en el sistema"""
        if cedula in self.usuarios:
            print("El usuario ya existe en el sistema.")
            return False
        
        self.usuarios[cedula] = {
            "nombre": nombre,
            "edad": edad,
            "telefono": telefono
        }
        print(f"Usuario {nombre} registrado exitosamente.")
        return True

    def agendar_cita(self, cedula, fecha, hora, tipo):
        """Agenda una nueva cita para un usuario"""
        if cedula not in self.usuarios:
            print("El usuario no está registrado en el sistema.")
            return False
        
        clave_cita = f"{cedula}{fecha}{hora}"
        self.citas[clave_cita] = {
            "cedula": cedula,
            "fecha": fecha,
            "hora": hora,
            "tipo de cita": tipo,
            "estado": "Confirmada"
        }
        print(f"Cita agendada para {self.usuarios[cedula]['nombre']} el {fecha} a las {hora}")
        return True

    def consultar_cita(self, cedula):
        """Consulta las citas de un usuario"""
        citas_usuario = [cita for clave, cita in self.citas.items() if cita['cedula'] == cedula]
        
        if not citas_usuario:
            print("No se encontraron citas para este usuario.")
            return None
        
        print("\n--- Citas Programadas ---")
        for cita in citas_usuario:
            print(f"Fecha: {cita['fecha']}, Hora: {cita['hora']}, "
                  f"tipo de cita: {cita['tipo de cita']}, "
                  f"Estado: {cita['estado']}")
        return citas_usuario

    def cancelar_cita(self, cedula, fecha, hora):
        """Cancela una cita específica"""
        clave_cita = f"{cedula}{fecha}{hora}"
        
        if clave_cita in self.citas:
            self.citas[clave_cita]['estado'] = "Cancelada"
            print("Cita cancelada exitosamente.")
            return True
        else:
            print("Cita no encontrada.")
            return False

    def registrar_atencion(self, cedula, fecha, hora, diagnostico):
        """Registra la atención de un paciente"""
        clave_atencion = f"{cedula}{fecha}{hora}"
        self.atenciones[clave_atencion] = {
            "cedula": cedula,
            "fecha": fecha,
            "hora": hora,
            "diagnostico": diagnostico
        }
        print("Atención registrada exitosamente.")

    def generar_reporte_administrador(self):
        """Genera un reporte completo para el administrador"""
        print("\n--- REPORTE COMPLETO DEL SISTEMA ---")
        
        print("\n==== USUARIOS ====")
        for cedula, datos in self.usuarios.items():
            print(f"Cédula: {cedula}, Nombre: {datos['nombre']}")
        
        print("\n==== CITAS ====")
        for clave, cita in self.citas.items():
            print(f"Cédula: {cita['cedula']}, Fecha: {cita['fecha']}, "
                  f"Hora: {cita['hora']}, Estado: {cita['estado']}")
        
        print("\n==== ATENCIONES ====")
        for clave, atencion in self.atenciones.items():
            print(f"Cédula: {atencion['cedula']}, Fecha: {atencion['fecha']}, "
                  f"Hora: {atencion['hora']}")

    def menu_principal(self):
        """Menú principal del sistema"""
        while True:
            print("\n--- EPS PailaSalud - Sistema de Gestión de Citas ---")
            print("1. Registrar Usuario")
            print("2. Agendar Cita")
            print("3. Consultar Cita")
            print("4. Cancelar Cita")
            print("5. Menú Administrador")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                cedula = input("Ingrese la cédula: ")
                nombre = input("Ingrese el nombre: ")
                edad = input("Ingrese la edad: ")
                telefono = input("Ingrese el teléfono: ")
                self.registrar_usuario(cedula, nombre, edad, telefono)
            
            elif opcion == "2":
                cedula = input("Ingrese la cédula: ")
                fecha = input("Ingrese la fecha (Día-Mes-Año): ")
                hora = input("Ingrese la hora: ")
                tipo = input("Ingrese el tipo de cita: ")
                self.agendar_cita(cedula, fecha, hora, tipo)
            
            elif opcion == "3":
                cedula = input("Ingrese la cédula para consultar citas: ")
                self.consultar_cita(cedula)
            
            elif opcion == "4":
                cedula = input("Ingrese la cédula: ")
                fecha = input("Ingrese la fecha de la cita (Día-Mes-Año): ")
                hora = input("Ingrese la hora de la cita: ")
                self.cancelar_cita(cedula, fecha, hora)
            
            elif opcion == "5":
                contraseña = input("Ingrese contraseña de administrador: ")
                if contraseña == self.admin_contraseña:
                    while True:
                        print("\n--- Menú Administrador ---")
                        print("1. Generar Reporte")
                        print("2. Salir a Menú Principal")
                        print("3. Salir del Sistema")
                        
                        opcion_admin = input("Seleccione una opción: ")
                        
                        if opcion_admin == "1":
                            self.generar_reporte_administrador()
                        elif opcion_admin == "2":
                            break
                        elif opcion_admin == "3":
                            return
                else:
                    print("Contraseña incorrecta, estafador.")
            
            elif opcion == "6":
                print("Gracias por usar el sistema de EPS PailaSalud. Esperamos no verte por aquí pronto")
                break

# Iniciar el sistema
if _name_ == "_main_":
    sistema = SistemaCitasPailaSalud()
    sistema.menu_principal()
import datetime
import json
class SistemaCitasPailaSalud:
    def init(self):
        self.usuarios = {}  
        self.citas = {}     
        self.atenciones = {}  
        self.admin_contraseña = "admin123"  

    def registrar_usuario(self, cedula, nombre, edad, telefono):
        """Registra un nuevo usuario en el sistema"""
        if cedula in self.usuarios:
            print("El usuario ya existe en el sistema.")
            return False
        
        self.usuarios[cedula] = {
            "nombre": nombre,
            "edad": edad,
            "telefono": telefono
        }
        print(f"Usuario {nombre} registrado exitosamente.")
        return True

    def agendar_cita(self, cedula, fecha, hora, especialidad):
        """Agenda una nueva cita para un usuario"""
        if cedula not in self.usuarios:
            print("El usuario no está registrado en el sistema.")
            return False
        
        clave_cita = f"{cedula}{fecha}{hora}"
        self.citas[clave_cita] = {
            "cedula": cedula,
            "fecha": fecha,
            "hora": hora,
            "especialidad": especialidad,
            "estado": "Confirmada"
        }
        print(f"Cita agendada para {self.usuarios[cedula]['nombre']} el {fecha} a las {hora}")
        return True

    def consultar_cita(self, cedula):
        """Consulta las citas de un usuario"""
        citas_usuario = [cita for clave, cita in self.citas.items() if cita['cedula'] == cedula]
        
        if not citas_usuario:
            print("No se encontraron citas para este usuario.")
            return None
        
        print("\n--- Citas Programadas ---")
        for cita in citas_usuario:
            print(f"Fecha: {cita['fecha']}, Hora: {cita['hora']}, "
                  f"Especialidad: {cita['especialidad']}, "
                  f"Estado: {cita['estado']}")
        return citas_usuario

    def cancelar_cita(self, cedula, fecha, hora):
        """Cancela una cita específica"""
        clave_cita = f"{cedula}{fecha}{hora}"
        
        if clave_cita in self.citas:
            self.citas[clave_cita]['estado'] = "Cancelada"
            print("Cita cancelada exitosamente.")
            return True
        else:
            print("Cita no encontrada.")
            return False

    def registrar_atencion(self, cedula, fecha, hora, diagnostico):
        """Registra la atención de un paciente"""
        clave_atencion = f"{cedula}{fecha}{hora}"
        self.atenciones[clave_atencion] = {
            "cedula": cedula,
            "fecha": fecha,
            "hora": hora,
            "diagnostico": diagnostico
        }
        print("Atención registrada exitosamente.")

    def generar_reporte_administrador(self):
        """Genera un reporte completo para el administrador"""
        print("\n--- REPORTE COMPLETO DEL SISTEMA ---")
        
        print("\n==== USUARIOS ====")
        for cedula, datos in self.usuarios.items():
            print(f"Cédula: {cedula}, Nombre: {datos['nombre']}")
        
        print("\n==== CITAS ====")
        for clave, cita in self.citas.items():
            print(f"Cédula: {cita['cedula']}, Fecha: {cita['fecha']}, "
                  f"Hora: {cita['hora']}, Estado: {cita['estado']}")
        
        print("\n==== ATENCIONES ====")
        for clave, atencion in self.atenciones.items():
            print(f"Cédula: {atencion['cedula']}, Fecha: {atencion['fecha']}, "
                  f"Hora: {atencion['hora']}")

    def menu_principal(self):
        """Menú principal del sistema"""
        while True:
            print("\n--- EPS PailaSalud - Sistema de Gestión de Citas ---")
            print("1. Registrar Usuario")
            print("2. Agendar Cita")
            print("3. Consultar Cita")
            print("4. Cancelar Cita")
            print("5. Menú Administrador")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                cedula = input("Ingrese la cédula: ")
                nombre = input("Ingrese el nombre: ")
                edad = input("Ingrese la edad: ")
                telefono = input("Ingrese el teléfono: ")
                self.registrar_usuario(cedula, nombre, edad, telefono)
            
            elif opcion == "2":
                cedula = input("Ingrese la cédula: ")
                fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
                hora = input("Ingrese la hora (HH:MM): ")
                tipo = input("Ingrese la especialidad: ")
                self.agendar_cita(cedula, fecha, hora, tipo)
            
            elif opcion == "3":
                cedula = input("Ingrese la cédula para consultar citas: ")
                self.consultar_cita(cedula)
            
            elif opcion == "4":
                cedula = input("Ingrese la cédula: ")
                fecha = input("Ingrese la fecha de la cita (Día-Mes-Año): ")
                hora = input("Ingrese la hora de la cita: ")
                self.cancelar_cita(cedula, fecha, hora)
            
            elif opcion == "5":
                contraseña = input("Ingrese contraseña de administrador: ")
                if contraseña == self.admin_contraseña:
                    while True:
                        print("\n--- Menú Administrador ---")
                        print("1. Generar Reporte")
                        print("2. Salir a Menú Principal")
                        print("3. Salir del Sistema")
                        
                        opcion_admin = input("Seleccione una opción: ")
                        
                        if opcion_admin == "1":
                            self.generar_reporte_administrador()
                        elif opcion_admin == "2":
                            break
                        elif opcion_admin == "3":
                            return
                else:
                    print("Contraseña incorrecta.")
            
            elif opcion == "6":
                print("Gracias por usar el sistema de EPS PailaSalud. ¡Hasta pronto!")
                break

if _name_ == "main":
    sistema = SistemaCitasPailaSalud()
    sistema.menu_principal()
