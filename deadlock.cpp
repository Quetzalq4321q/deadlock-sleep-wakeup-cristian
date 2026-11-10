#include <iostream>
#include <mutex>
#include <thread>

std::mutex recurso_a;
std::mutex recurso_b;

void tarea() {
    // Todos los hilos toman los recursos en el mismo orden: A y luego B.
    std::lock_guard<std::mutex> primero(recurso_a);
    std::lock_guard<std::mutex> segundo(recurso_b);
    std::cout << "Tarea finalizada\n";
}

int main() {
    std::thread hilo_1(tarea);
    std::thread hilo_2(tarea);
    hilo_1.join();
    hilo_2.join();
    return 0;
}
