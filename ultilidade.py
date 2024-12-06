# utilidades.py

import time

def cronometro(func):
    """Decora uma função para medir o tempo de execução."""
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Marca o início do tempo
        resultado = func(*args, **kwargs)
        fim = time.time()  # Marca o fim do tempo
        tempo_execucao = fim - inicio
        print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
        return resultado
    return wrapper
