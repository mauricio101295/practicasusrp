import numpy as np
import pyldpc

# Parámetros LDPC
n = 15  # Longitud del código (total de bits)
d_v = 3  # Grado de los nodos variables
d_c = 6  # Grado de los nodos de chequeo

# Crear matriz LDPC
H, G = pyldpc.make_ldpc(n, d_v, d_c, systematic=True, sparse=True)

# Mensaje de prueba
msg = np.random.randint(2, size=G.shape[1])

# Codificación LDPC
codeword = pyldpc.encode(msg, G)

# Simulación de un canal ruidoso (introducción de errores)
received_codeword = pyldpc.channel_noise(codeword, 0.1)

# Decodificación LDPC
decoded_msg, _ = pyldpc.decode(received_codeword, H, snr=0.1)

# Verificación de la decodificación
if np.array_equal(msg, decoded_msg):
    print("Decodificación exitosa.")
else:
    print("Error en la decodificación.")

# Resultados
print("Mensaje original:", msg)
print("Mensaje decodificado:", decoded_msg)
