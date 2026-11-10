"""Cliente UDP que estima la hora del servidor con el algoritmo de Cristian."""

import socket
import time


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
        cliente.settimeout(5)
        t0 = time.time_ns() // 1_000_000
        cliente.sendto(b"Dame la hora", ("127.0.0.1", 8080))
        datos, _ = cliente.recvfrom(1024)
        t1 = time.time_ns() // 1_000_000

    hora_servidor_ms = int(datos.decode("ascii"))
    rtt_ms = t1 - t0
    hora_estimada_ms = hora_servidor_ms + rtt_ms / 2

    print(f"Tiempo de ida y vuelta (RTT): {rtt_ms} ms")
    print(f"Hora enviada por el servidor: {hora_servidor_ms} ms")
    print(f"Hora estimada del servidor: {hora_estimada_ms:.1f} ms")


if __name__ == "__main__":
    try:
        main()
    except socket.timeout:
        print("No hubo respuesta. Inicia primero algoritmo_cristian_servidor.py.")
