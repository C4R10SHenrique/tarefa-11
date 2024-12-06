# main.py

import meu_pacote

# Definir valores para o cálculo das áreas
raio = 5
base = 4
altura = 3

# Utilizando o cronômetro para calcular a área do círculo e retângulo
@meu_pacote.cronometro
def calcular_areas():
    area_circulo = meu_pacote.area_circulo(raio)
    area_retangulo = meu_pacote.area_retangulo(base, altura)
    print(f"A área do círculo é: {area_circulo:.2f}")
    print(f"A área do retângulo é: {area_retangulo:.2f}")
    
# Chama a função para calcular as áreas e medir o tempo de execução
calcular_areas()
