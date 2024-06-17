# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo (Optimal Filtering - OF 2).
# Autor: Guilherme Barroso Morett.
# Data: 12 de junho de 2024.

# Objetivo do código: análise do erro absoluto do parâmetro da amplitude, fase ou pedestal pelo método do Filtro Ótimo (Optimal Filtering - OF 2).

"""
Organização do Código:

Importação de arquivos.
Leitura dos dados de ocupação: leitura_dados_ocupacao_OF2.py
Leitura dos dados de ruídos: leitura_dados_ruidos_OF2.py
Método: metodo_OF2.py

Funções presentes:

1) Função para o cálculo da estatística do erro de estimação da amplitude, fase ou pedestal.
Entrada: lista com os erros de estimação da amplitude, fase ou pedestal.
Saída: a média, a variância e o desvio padrão do erro de estimação da amplitude, fase ou pedestal.

2) Função para o plote do histograma do erro de estimação da amplitude, fase ou pedestal.
Entrada: lista com os erros de estimação da amplitude, fase ou pedestal e seus dados estatísticos.
Saída: nada.

3) Função principal.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from termcolor import colored

# Importação dos arquivos.
from leitura_dados_ocupacao_OF2 import *
from leitura_dados_ruidos_OF2 import *
from metodo_OF2 import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Análise do erro de estimação da amplitude, fase ou pedestal pelo método do Filtro Ótimo (Optimal Filtering - OF 2).:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------------ 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE, FASE OU PEDESTAL --------------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude, fase ou pedestal.
def dados_estatisticos_erro_parametro(lista_erro_parametro):
    
    # A lista do erro de estimação da amplitude, fase ou pedestal é convertida para o tipo numpy array.
    vetor_erro_parametro = np.array(lista_erro_parametro)

    # Cálculo da média do erro de estimação da amplitude, fase ou pedestal.
    media_erro_parametro = np.mean(vetor_erro_parametro)

    # Cálculo da variância do erro de estimação da amplitude, fase ou pedestal.
    var_erro_parametro = np.var(vetor_erro_parametro)

    # Cálculo do desvio padrão do erro de estimação da amplitude, fase ou pedestal.
    desvio_padrao_erro_parametro = np.std(vetor_erro_parametro)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação da amplitude, fase ou pedestal.
    return media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### --------------------- 2) FUNÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO ERRO DE ESTIMAÇÃO DA AMPLITUDE, FASE OU PEDESTAL ------------------------ ###

# Definição de função para o plot do histograma do erro de estimação da amplitude, fase ou pedestal.
def histograma_erro_parametro(parametro, lista_erro_parametro, media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro):
    
    # A lista do erro de estimação do parâmetro é convertida para o tipo numpy array.
    vetor_erro_parametro = np.array(lista_erro_parametro)

    # Se a variável parametro for igual a string "amplitude".
    if parametro == "amplitude":
        
        # Nomeação do eixo x de acordo com o parâmetro da amplitude.
        plt.xlabel(f'Erro de estimação da {parametro} (ADC Count)', fontsize = 18)

    # Se a variável parametro for igual a string "fase".
    elif parametro == "fase":
        
        # Nomeação do eixo x de acordo com o parâmetro da fase.
        plt.xlabel(f'Erro de estimação da {parametro} (ns)', fontsize = 18)
     
    # Se a variável parametro for igual a string "pedestal".   
    elif parametro == "pedestal":
        
        # Nomeação do eixo x de acordo com o parâmetro do pedestal.
        plt.xlabel(f'Erro de estimação do {parametro} (ADC Count)', fontsize = 18)
        
    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)

    # A variável texto recebe uma string com as informações de interesse.
    texto = f"Média: {round(media_erro_parametro, 6)} \n Variância: {round(var_erro_parametro, 6)} \n Desvio padrão: {round(desvio_padrao_erro_parametro, 6)}"

    # Definição do histograma a partir do vetor vetor_erro_parametro.
    plt.hist(vetor_erro_parametro, bins = 100, range = [-800, 800], edgecolor = 'black', linewidth = 1.2)
    
    # Posicionamento do texto no gráfico.
    plt.text(0.99, 0.98, texto, horizontalalignment = 'right',
    verticalalignment = 'top',
    transform = plt.gca().transAxes,
    bbox = dict(facecolor = 'white', alpha = 0.5),
    fontsize = 14)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ------------------------------------------------------------- ###

# Definição da função principal (main) do código.
def principal_histograma_erro_parametro():
    
    # Impressão de mensagem no terminal.
    print("Opções de parâmetros:\nAmplitude: 1\nFase: 2\nPedestal: 3\n")
    
    # A variável parametro armazena o número do tipo inteiro digitado pelo usuário via terminal.
    parametro = int(input("Digite o número do parâmetro desejado: "))
    
    # A variável valores_parametro é uma lista com os valores aceitáveis para o parametro.
    valores_parametro = list(range(1,4,1))

    # Caso o valor digitado armazenado na variável paraemtro não estiver presente na lista valores_parametro.
    if parametro not in valores_parametro:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # A variável numero_ocupacao armazena o valor digitado da ocupação desejada no terminal pelo usuário.
    n_ocupacao = float(input("Digite o valor da ocupação desejada: "))

    # A variável valores_ocupacao é uma lista com os valores aceitáveis de ocupação de 0 até 100.
    valores_ocupacao = list(range(0,101,10))

    # Caso o valor digitado armazenado na variável n_ocupacao não estiver presente na lista valores_ocupacao.
    if n_ocupacao not in valores_ocupacao:
    
        # Exibição de uma mensagem de alerta de que a ocupação solicitada é inválida.
        print("\nNúmero de ocupação inválida!\n")
        # A execução do programa é interrompida.
        exit(1) 

    # O tipo da variável n_ocupacao é convertida para inteiro.
    # Obs.: essa conversão possibilita que a leitura do arquivo possa ser feita corretamente.
    n_ocupacao = int(n_ocupacao)
    
    # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
    n_janelamento = int(input("Digite a quantidade de janelamento: "))

    # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de dois.
    valores_janelamento = list(range(7,20,2))

    # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
    if n_janelamento not in valores_janelamento:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)

    # Chamada ordenada das funções.
    
    Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao) 
    
    Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
    vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
    
    Matriz_Dados_Pulsos, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
    
    Matriz_Dados_Pulsos, vetor_fase_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento)
    
    # Caso a variável parametro seja igual a 1.
    if parametro == 1:
        
        # A variável parametro recebe a string "amplitude".
        parametro = "amplitude"
        
    # Caso a variável parametro seja igual a 2.
    elif parametro == 2:
    
        # A variável parametro recebe a string "fase".
        parametro = "fase"
        
    # Caso a variável parametro seja igual a 3.
    elif parametro == 3:
        
        # A variável parametro recebe a string "pedestal".
        parametro = "pedestal"   
    
    Matriz_Dados_Pulsos_Treino, Matriz_Dados_Pulsos_Teste, vetor_amplitude_referencia_treino, vetor_amplitude_referencia_teste = dados_treino_teste_histograma(Matriz_Dados_Pulsos, vetor_amplitude_referencia_janelado)
    
    Matriz_Dados_Pulsos_Treino, Matriz_Dados_Pulsos_Teste, vetor_fase_referencia_treino, vetor_fase_referencia_teste = dados_treino_teste_histograma(Matriz_Dados_Pulsos, vetor_fase_referencia_janelado)
    
    vetor_dados_ruidos = leitura_dados_ruidos(n_ocupacao)
    
    Matriz_Dados_Ruidos = amostras_ruidos_janelamento(vetor_dados_ruidos, n_janelamento)
    
    Matriz_Dados_Ruidos_Treino, Matriz_Dados_Ruidos_Teste = dados_ruidos_treino_teste_histograma(Matriz_Dados_Ruidos)
    
    Matriz_Covariancia = matriz_covariancia(Matriz_Dados_Ruidos_Treino)
       
    lista_erro_parametro = metodo_OF2(parametro, n_janelamento, Matriz_Dados_Pulsos_Teste, vetor_amplitude_referencia_teste, vetor_fase_referencia_teste, Matriz_Covariancia)

    media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro = dados_estatisticos_erro_parametro(lista_erro_parametro)
    
    histograma_erro_parametro(parametro, lista_erro_parametro, media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro)
    
# Chamada da função principal (main) do código.
principal_histograma_erro_parametro()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")