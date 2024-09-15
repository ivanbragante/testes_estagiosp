# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

# Código:

# INDICE = 13
# SOMA = 0
# K = 0

# while K < INDICE:
#     K = K + 1
#     SOMA = K + SOMA
    
# print(SOMA)

# SOMA irá imprimir 91

############################################################################# 

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# Código:

# def pertence_fibonacci(numero):
    
#     a, b = 0, 1
#     while b <= numero:
#         if b == numero:
#             return True
#         a, b = b, a + b
#     return False

# num = int(input("Digite um número: "))

# # Chama a função e imprime o resultado
# if pertence_fibonacci(num):
#     print(f"O número {num} pertence à sequência de Fibonacci.")
# else:
#     print(f"O número {num} não pertence à sequência de Fibonacci.")

#############################################################################

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

# Código:

# import json

# # Coloque o caminho do arquivo json
# with open('C:/Users/Ivan/Desktop/Python Excercicio vaga/dados.json', 'r') as file:
#     dados = json.load(file)

# # Filtrando os dias com faturamento maior que 0
# faturamentos_validos = [dia['valor'] for dia in dados if dia['valor'] > 0]

# # Calculando o menor e o maior valor de faturamento
# menor_faturamento = min(faturamentos_validos)
# maior_faturamento = max(faturamentos_validos)

# media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)

# dias_acima_da_media = sum(1 for dia in faturamentos_validos if dia > media_faturamento)

# # Exibindo os resultados

# print("Menor faturamento em um dia: ", menor_faturamento,"\nMaior faturamento em um dia: ", maior_faturamento,"\nDias com faturamento acima da média: ", dias_acima_da_media)

# Resultado exibido: 
# Menor faturamento em um dia:  373.7838 
# Maior faturamento em um dia:  48924.2448
# Dias com faturamento acima da média:  10

#############################################################################

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP - R$67.836,43
# • RJ - R$36.678,66
# • MG - R$29.229,88
# • ES - R$27.165,48
# • Outros - R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

# Código:

# Valores de faturamento por estado (em reais)

# faturamento_estados = {
#     'SP': 67836.43,
#     'RJ': 36678.66,
#     'MG': 29229.88,
#     'ES': 27165.48,
#     'Outros': 19849.53
# }

# # Calculando o faturamento total
# faturamento_total = sum(faturamento_estados.values())

# # Calculando o percentual de cada estado
# percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

# # Exibindo os percentuais
# print(percentuais) 

# Valor impresso no terminal:
# {'SP': 37.52845624346717, 'RJ': 20.291360952794975, 'MG': 16.170548370275327, 'ES': 15.02848141496807, 'Outros': 10.98115301849447}

#############################################################################

# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# Código:

# def inverter_string(string):

#   string_invertida = ""
#   for i in range(len(string) - 1, -1, -1):
#     string_invertida += string[i]
#   return string_invertida

# # Exemplo de uso:
# string = input("Digite uma string: ")
# resultado = inverter_string(string)
# print("A string invertida é:", resultado)