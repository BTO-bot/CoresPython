#Modulo de Usuarios:

from TarjetaCredito import TarjetaCredito  

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = []  # Lista guardar múltiples tarjetas de crédito

#Metodos actualizados para agregar nuevas tarjetas al usuario:

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)
        return self

    def hacer_compra(self, monto, tarjeta_index=0): # Realiza una compra con la tarjeta escogida por el índice
        
        if 0 <= tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].compra(monto)
        else:
            print("Índice de tarjeta no válido.")
        return self

    def pagar_tarjeta(self, monto, tarjeta_index=0): # Realiza un pago con la tarjeta escogida 
        
        if 0 <= tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].pago(monto)
        else:
            print("Índice de tarjeta no válido.")
        return self

# Muestra el saldo de la tarjeta escogida:

    def mostrar_saldo_usuario(self, tarjeta_index=0): 
        
        if 0 <= tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].mostrar_info_tarjeta()
        else:
            print("Índice de tarjeta no válido.")
        return self

# Un Ejemplo para llamar a los métodos de la tarjeta y acceder a sus atributos:

    def metodo_ejemplo(self): 
        
        self.tarjetas[0].compra(100)
        print(self.tarjetas[0].saldo_pagar)
