# Deadlock, SLEEP/WAKEUP y algoritmo de Cristian

Ejemplos independientes basados en el PDF del curso de Sistemas Operativos. Cada archivo tiene su propio punto de entrada. El algoritmo de Cristian usa dos programas que se comunican entre sí: primero se inicia el servidor y luego el cliente.

## Contenido

| Tema | Archivo | Qué muestra |
| --- | --- | --- |
| Deadlock | `deadlock.cpp` | Prevención de interbloqueo mediante un orden fijo al tomar dos mutex. |
| SLEEP/WAKEUP | `sleep_wakeup.cpp` | Espera y notificación con `condition_variable` y una condición persistente. |
| Algoritmo de Cristian | `algoritmo_cristian_servidor.py` | Servidor UDP que responde con su hora en milisegundos. |
| Algoritmo de Cristian | `algoritmo_cristian_cliente.py` | Cliente UDP que mide el RTT y estima la hora del servidor. |
| Material original | `docs/dead lock wake up y algoritmo de Christian.pdf` | Documento usado como referencia. |

## Requisitos

- Compilador de C++11 con soporte para hilos, por ejemplo `g++`.
- Python 3 para los programas del algoritmo de Cristian.

## Ejecutar cada ejemplo

Desde la raíz de este repositorio:

```sh
g++ deadlock.cpp -std=c++11 -pthread -o deadlock
./deadlock

g++ sleep_wakeup.cpp -std=c++11 -pthread -o sleep_wakeup
./sleep_wakeup
```

En Windows, los ejecutables normalmente terminan en `.exe`; ejecútalos como `./deadlock.exe` y `./sleep_wakeup.exe` en PowerShell.

Para Cristian, abre dos terminales. En la primera:

```sh
python algoritmo_cristian_servidor.py
```

En la segunda:

```sh
python algoritmo_cristian_cliente.py
```

En algunos sistemas, el comando de Python es `python3` o `py`. El servidor queda activo hasta interrumpirlo con `Ctrl+C`. Ambos programas usan `127.0.0.1:8080` y solo la biblioteca estándar de Python.

La estimación de Cristian supone un tiempo de ida y vuelta aproximadamente simétrico y un tiempo de procesamiento del servidor pequeño. El cliente calcula `hora_servidor + RTT / 2`; no modifica el reloj del sistema.
