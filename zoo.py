#Tkinter
import tkinter as tk
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from tkinter import ttk, messagebox

# Dados dos animais: quantidades de comida consumida (em kg)
animais = {
    'Elefante': {'veg': 4.5, 'er': 6.5, 'pei': 0},
    'Girafa': {'veg': 1.5, 'er': 1.5, 'pei': 0},
    'Hipopotamo': {'veg': 2.5, 'er': 2.5, 'pei': 0},
    'Gorila': {'veg': 2.5, 'er': 1.0, 'pei': 0},
    'Alce': {'veg': 1.0, 'er': 2.0, 'pei': 0},
    'Canguru': {'veg': 1.0, 'er': 1.0, 'pei': 0},
    'Zebra': {'veg': 1.5, 'er': 1.0, 'pei': 0},
    'Pinguim': {'veg': 0, 'er': 0, 'pei': 2.0}
}

# Função para calcular a quantidade de briquetes
def calcular_briquetes(animais_selecionados, seguir_ordem):
    # Inicializa os dois rounds
    round_1_animais = []
    round_2_animais = []
    
    # Verifica se precisa seguir a ordem
    if seguir_ordem:
        round_1_animais = animais_selecionados[:2]
        round_2_animais = animais_selecionados[2:]
    else:
        round_1_animais = [animais_selecionados[0], animais_selecionados[2]]
        round_2_animais = [animais_selecionados[1], animais_selecionados[3]]

    # Função auxiliar para somar comida
    def somar_comida(animais_lista):
        comida_total = {'veg': 0, 'er': 0, 'pei': 0}
        for animal in animais_lista:
            comida_total['veg'] += animais[animal]['veg']
            comida_total['er'] += animais[animal]['er']
            comida_total['pei'] += animais[animal]['pei']
        return comida_total

    # Calcular comida total para cada round
    round_1_comida = somar_comida(round_1_animais)
    round_2_comida = somar_comida(round_2_animais)

    # Função para converter kg em briquetes (1 briquete = 3 kg)
    def converter_briquetes(comida):
        return {tipo: (quantidade // 3) + (1 if quantidade % 3 > 0 else 0) for tipo, quantidade in comida.items()}

    # Converte a quantidade de comida total em briquetes
    round_1_briquetes = converter_briquetes(round_1_comida)
    round_2_briquetes = converter_briquetes(round_2_comida)

    # Função para calcular briquetes sobrando
    def calcular_sobrando(briquetes):
        total_briquetes = briquetes['veg'] + briquetes['er'] + briquetes['pei'] + 1  # +1 para o briquete de carne fixo
        return 8 - total_briquetes

    # Calcula os espaços sobrando no carrinho
    round_1_sobrando = calcular_sobrando(round_1_briquetes)
    round_2_sobrando = calcular_sobrando(round_2_briquetes)

    # Função para exibir o resultado em uma caixa de diálogo
    def exibir_resultado(round_num, animais_round, briquetes, sobrando):
        resultado = f"Round {round_num}:\n"
        resultado += f"Animais: {', '.join(animais_round)}\n"
        resultado += f"{briquetes['veg']} briquetes de vegetais\n"
        resultado += f"{briquetes['er']} briquetes de erva\n"
        resultado += f"{briquetes['pei']} briquetes de peixe\n"
        resultado += f"1 carne (fixo)\n"
        if sobrando > 0:
            resultado += f"Sobrando {sobrando} espaços no carrinho\n"
        else:
            resultado += "Carrinho completo\n"
        return resultado

    # Exibe os resultados
    resultado_final = exibir_resultado(1, round_1_animais, round_1_briquetes, round_1_sobrando)
    resultado_final += exibir_resultado(2, round_2_animais, round_2_briquetes, round_2_sobrando)
    messagebox.showinfo("Resultado", resultado_final)

# Função chamada ao clicar no botão de calcular
def ao_clicar():
    selecionados = [combo_animal1.get(), combo_animal2.get(), combo_animal3.get(), combo_animal4.get()]
    if len(set(selecionados)) != 4:
        messagebox.showerror("Erro", "Selecione 4 animais diferentes!")
        return
    seguir_ordem = var_seguir_ordem.get()
    calcular_briquetes(selecionados, seguir_ordem)

# Configurando a interface gráfica
janela = tk.Tk()
janela.title("Calculadora de Briquetes")

# Criação dos rótulos e campos de seleção
tk.Label(janela, text="Selecione os 4 animais:").grid(row=0, column=0, columnspan=2)

animais_lista = list(animais.keys())

combo_animal1 = ttk.Combobox(janela, values=animais_lista)
combo_animal2 = ttk.Combobox(janela, values=animais_lista)
combo_animal3 = ttk.Combobox(janela, values=animais_lista)
combo_animal4 = ttk.Combobox(janela, values=animais_lista)

combo_animal1.grid(row=1, column=0)
combo_animal2.grid(row=1, column=1)
combo_animal3.grid(row=2, column=0)
combo_animal4.grid(row=2, column=1)

# Checkbox para seguir a ordem dos animais
var_seguir_ordem = tk.BooleanVar()
checkbox_ordem = tk.Checkbutton(janela, text="Seguir ordem dos animais", variable=var_seguir_ordem)
checkbox_ordem.grid(row=3, column=0, columnspan=2)

# Botão de calcular
botao_calcular = tk.Button(janela, text="Calcular Briquetes", command=ao_clicar)
botao_calcular.grid(row=4, column=0, columnspan=2)

# Inicia a janela
janela.mainloop()
