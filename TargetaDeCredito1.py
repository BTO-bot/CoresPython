class TarjetaCredito:
    tarjetas = []  # Esta sera la lista que guardara las instancias creadas

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas.append(self)


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


    @classmethod
    def mostrar_todas_tarjetas(cls):
        for tarjeta in cls.tarjetas:
            tarjeta.mostrar_info_tarjeta()



# tarjetas de créditos
tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.015)
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.03)

# Operaciones de la tarjeta 1
tarjeta1.compra(200).compra(300).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Operaciones de la tarjeta 2
tarjeta2.compra(500).compra(600).compra(200).pago(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Operaciones de la tarjeta 3
tarjeta3.compra(200).compra(100).compra(150).compra(75).compra(50).mostrar_info_tarjeta()

# Nos permite ver todas las tarjetas
TarjetaCredito.mostrar_todas_tarjetas()
