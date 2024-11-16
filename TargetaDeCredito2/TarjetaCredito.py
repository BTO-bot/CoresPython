#Modulo de Tarjeta de credito:

class TarjetaCredito:

    def __init__(self, saldo_pagar=0, limite_credito=20000, intereses=0.015):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses


    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self  

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self  


    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self  


    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self 
