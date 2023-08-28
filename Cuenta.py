
def input_s(msg):

    res = input(msg)
    if res in [" ",".",",",":",";"]:
        res = input("No se aceptan valores no alfanumericos, intente denuevo\n" + msg)
    return res

class cuenta:
    usuarios = []   # Almacenamiento de los datos de usuarios

    def __init__(self, ci, nombre, saldo) -> None:
        # Se crea el objeto con los atributos nombre, cedula y su saldo inicial
        self.ci = ci
        self.nombre = nombre
        self.saldo = saldo
        cuenta.usuarios.append(self)


        print("Se creo la cuenta satisfactoriamente\n")

    def restar_saldo(self, num):
    # Metodo que recibe un objeto cuenta y resta su saldo - numero enviado
        if self.saldo - num < 0:
            print("Saldo insuficiente")
            return False

        self.saldo -= num
        return True
    @classmethod
    # Metodo que verifica si la cedula enviada corresponde a una cuenta existente
    def existe_cuenta(cls, cedula):
        for i in cls.usuarios:
            if cedula == i.ci: return True
        print("La cedula no coincide con la base de datos, intente de nuevo\n")
        return False
    @classmethod
    # Ciclo que recorre la lista de usuarios con un contador, cuando coincida
    # una cedula con la lista devuelve es objeto usuario
    def conseguir_cuenta(cls, cedula):
        for usuario, i in zip(cls.usuarios, range(len(cls.usuarios))):
            if cedula == usuario.ci: return cls.usuarios[i]
    @classmethod
    def verificar_usuarios(cls, num):
    # Recibe un numero y lo compara con la lista de usuarios, si el numero es mayor retorna False
    # de lo contrario retorna True
        if len(cls.usuarios) < num:
            print("No existen suficientes usarios para realizar esta operacion, regresando\n")
            return True
        return False

def crear_cuenta():
    #Se crea objeto clase cuenta
    cedula = int(input("Ingrese la cedula: "))
    nombre = input_s("Ingrese nombre de usuario: ")
    saldo = int(input("Ingrese monto inicial: "))

    cuenta(cedula, nombre, saldo)

def consulta():
    #Te devuelve el saldo actual del objeto
    if cuenta.verificar_usuarios(1): return

    cedula = int(input("Ingrese la cedula: "))

    if cuenta.existe_cuenta(cedula):
        co = cuenta.conseguir_cuenta(cedula)
        print("\nNombre de Usuario: {}\nReferencia: {}\nSaldo: {}\n".format(co.nombre, co.ci, co.saldo))

    else:
        consulta()


def retiro():
    if cuenta.verificar_usuarios(1): return

    cedula = int(input("Ingrese la cedula: "))
    if cuenta.existe_cuenta(cedula):
        re = int(input("Ingrese el monto a retirar: "))
        co = cuenta.conseguir_cuenta(cedula)

        if co.restar_saldo(re): print("Operacion exitosa, regresando...\n")
    else:
        retiro()

def deposito():
    if cuenta.verificar_usuarios(1): return

    cedula = int(input("Ingrese la cedula: "))
    if cuenta.existe_cuenta(cedula):
        re = int(input("Ingrese el monto a depositar: "))
        co = cuenta.conseguir_cuenta(cedula)

        co.saldo += re
        print("Operacion exitosa, regresando...\n")
    else:
        retiro()


def transferencia():
    if cuenta.verificar_usuarios(2): return

    cedula1 = int(input("Ingrese la cedula de la cuenta a retirar: "))
    if cuenta.existe_cuenta(cedula1) == False: transferencia()
    cedula2 = int(input("Ingrese la cedula de la cuenta a recibir: "))

    if cuenta.existe_cuenta(cedula2):
        re = int(input("Ingrese el monto a transferir: "))
        co1 = cuenta.conseguir_cuenta(cedula1)
        co2 = cuenta.conseguir_cuenta(cedula2)

        if co1.restar_saldo(re):
            co2.saldo += re
            print("Operacion exitosa, regresando...\n\n")

    else:
        transferencia()


def main():
    while True:
        print("Banesco Online\n\n(1) Crear usuario\n(2) Consulta\n(3) Deposito\n(4) Retiro\n(5) Transferencia\n(6) Finalizar\n")

        op = input("Marque una opcion: ")
        while op not in ["1", "2", "3", "4", "5", "6"]:
            print("Respuesta invalida, intente de nuevo")
            op = input("Marque una opcion: ")

        if op == "1": crear_cuenta()
        if op == "2": consulta()
        if op == "3": deposito()
        if op == "4": retiro()
        if op == "5": transferencia()
        if op == "6": break

main()
