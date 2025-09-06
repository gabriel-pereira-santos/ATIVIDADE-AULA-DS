import statistics

# 1  **************************************************

def amplitude(lista):
    menor = min(lista)
    maior =  max(lista)
    amplitude  =  maior - menor
    return amplitude 


def verificar(lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    moda = statistics.mode(lista)
    amplitudee = amplitude(lista)
    variancia = statistics.variance(lista)
    print(f'''
    media = {media}
    mediana = {mediana}
    moda = {moda}
    amplitude = {amplitudee}
    variancia = {variancia}
    ''')

# 2  **************************************************

def dados(n):
    media = statistics.mean(n)
    mediana = statistics.median(n)
    try:
        moda = statistics.mode(n)
    except statistics.StatisticsError:
        moda = "Sem moda (valores com mesma frequência)"

    variancia = statistics.variance(n)
    desvio_padrao = statistics.stdev(n)
    amplitude = max(n) - min(n)

    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda}")
    print(f"Variância: {variancia:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
    print(f"Amplitude: {amplitude:.2f}")



