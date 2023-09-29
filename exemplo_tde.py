def imprime_numeros_crescentes(N, atual=0):
    if atual <= N:
        print(atual)
        imprime_numeros_crescentes(N, atual + 1)

# Exemplo de uso:
numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("O número deve ser positivo.")
else:
    imprime_numeros_crescentes(numero)