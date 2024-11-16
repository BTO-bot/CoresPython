#Main donde ejecutamos las funciones y traemos los modulos:


from Usuario import Usuario  
from TarjetaCredito import TarjetaCredito  

# Usuario de ejemplo:

usuario = Usuario("Camilo", "Solis", "camilo.solis95@gmail.cl")

# Creamos tarjetas de credito asociadas al usuario de ejemplo:

tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)

tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.015)

usuario.agregar_tarjeta(tarjeta1).agregar_tarjeta(tarjeta2)

# Operaciones en la primera tarjeta
usuario.hacer_compra(200, tarjeta_index=0).hacer_compra(300, tarjeta_index=0).pagar_tarjeta(100, tarjeta_index=0).mostrar_saldo_usuario(tarjeta_index=0)

# Operaciones en la segunda tarjeta
usuario.hacer_compra(500, tarjeta_index=1).pagar_tarjeta(150, tarjeta_index=1).mostrar_saldo_usuario(tarjeta_index=1)

