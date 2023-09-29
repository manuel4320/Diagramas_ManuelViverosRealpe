class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sueldo Bruto: {self.sueldo_bruto}"

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

    def mostrar_informacion(self):
        info_empleado = super().mostrar_informacion()
        subordinados = [sub.mostrar_informacion() for sub in self.subordinados]
        return f"{info_empleado}, Categoría: {self.categoria}\nSubordinados:\n{', '.join(subordinados)}"

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono_contacto):
        super().__init__(nombre, edad)
        self.telefono_contacto = telefono_contacto

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono de Contacto: {self.telefono_contacto}"


empleados = []
clientes = []


def agregar_empleado():
    nombre = input("Nombre del empleado: ")
    edad = int(input("Edad del empleado: "))
    sueldo_bruto = float(input("Sueldo bruto del empleado: "))
    empleado = Empleado(nombre, edad, sueldo_bruto)
    empleados.append(empleado)
    print("Empleado agregado con éxito.")


def agregar_directivo():
    nombre = input("Nombre del directivo: ")
    edad = int(input("Edad del directivo: "))
    sueldo_bruto = float(input("Sueldo bruto del directivo: "))
    categoria = input("Categoría del directivo: ")
    directivo = Directivo(nombre, edad, sueldo_bruto, categoria)
    empleados.append(directivo)
    print("Directivo agregado con éxito.")


def agregar_cliente():
    nombre = input("Nombre del cliente: ")
    edad = int(input("Edad del cliente: "))
    telefono_contacto = input("Teléfono de contacto del cliente: ")
    cliente = Cliente(nombre, edad, telefono_contacto)
    clientes.append(cliente)
    print("Cliente agregado con éxito.")


def mostrar_empleados():
    print("\nInformación de Empleados:")
    for empleado in empleados:
        print(empleado.mostrar_informacion())


def mostrar_clientes():
    print("\nInformación de Clientes:")
    for cliente in clientes:
        print(cliente.mostrar_informacion())


while True:
    print("\nMenú Principal:")
    print("1. Añadir Empleado")
    print("2. Añadir Directivo")
    print("3. Añadir Cliente")
    print("4. Ver Empleados")
    print("5. Ver Clientes")
    print("6. Salir")

    opcion = input("ingrese una opción: ")

    if opcion == "1":
        agregar_empleado()
    elif opcion == "2":
        agregar_directivo()
    elif opcion == "3":
        agregar_cliente()
    elif opcion == "4":
        mostrar_empleados()
    elif opcion == "5":
        mostrar_clientes()
    elif opcion == "6":
        print("¡ADIOS!")
        break
    else:
        print("Opción no válida.")
