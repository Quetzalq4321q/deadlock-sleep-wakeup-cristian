"""Servidor de tiempo UDP para el ejemplo del algoritmo de Cristian."""

import socket
import time


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
        servidor.bind(("127.0.0.1", 8080))
        print("Servidor de tiempo activo en 127.0.0.1:8080. Ctrl+C para salir.")
        while True:
            _, direccion = servidor.recvfrom(1024)
            hora_actual_ms = str(time.time_ns() // 1_000_000)
            servidor.sendto(hora_actual_ms.encode("ascii"), direccion)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
