#include <condition_variable>
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mutex_estado;
std::condition_variable aviso;
bool listo = false;

void consumidor() {
    std::unique_lock<std::mutex> bloqueo(mutex_estado);
    // wait libera el mutex mientras espera y vuelve a comprobar la condición.
    aviso.wait(bloqueo, [] { return listo; });
    std::cout << "Dato recibido\n";
}

int main() {
    std::thread hilo(consumidor);
    {
        std::lock_guard<std::mutex> bloqueo(mutex_estado);
        listo = true;
    }
    aviso.notify_one();
    hilo.join();
    return 0;
}
