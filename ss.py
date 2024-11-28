import psutil # análise de dados (CPU e memória RAM)
import customtkinter as ct  # customização
import customtkinter as ctk # customização
import random # número aleatórios 
import time # medir tempo
import sys # nesse algoritmo, a função sys.exit() retorna o fehcamento do mesmo.
import threading # em Python é utilizada para trabalhar com threads, que são uma forma de dividir a execução de um programa em múltiplas linhas de execução simultâneas.

ctk.set_appearance_mode("system")  # definir aparência da interface
ctk.set_default_color_theme("dark-blue")  # definir cor da interface
app = ctk.CTk()
app.geometry("1080x680") # definir a dimensão da interface
#app.attributes("-fullscreen", True)  # definir a dimensão da interface
app.title("System Monitorator")  # definir título da interface
app.resizable(False, False)  # impedir redimensionamento livre
app.configure(fg_color="black") # cor de fundo
# Variável de controle para alternar entre os algoritmos
algoritmo_atual = 0  # 0 - Bubble Sort, 1 - Selection Sort, 2 - Insertion Sort, 3 - Quick Sort
max_cpu = 0
max_ram = 0
# Função que será chamada pelo botão
def alternar_algoritmo():
    global algoritmo_atual
    algoritmo_atual = (algoritmo_atual + 1) % 4  # Alterna entre 0, 1, 2, 3 (Bubble Sort, Selection Sort, Insertion Sort, Quick Sort)
    print(f"Iniciando algoritmo: {algoritmo_atual}")
    limite = int(vetor_limite.get())  # Obtém o limite a partir da entrada do usuário
    medir_tempos(limite)
    threading.Thread(target=monitor_uso, daemon=True).start()
def fechar():
    global button
    button = 0
    if button == 0:
        sys.exit()
def resetar():
    global max_cpu, max_ram
    max_cpu = 0
    max_ram = 0
    bubble_lacpu.configure(text="--")
    bubble_laram.configure(text="--")
    bubble_label.configure(text="--")
    selection_lacpu.configure(text="--")
    selection_laram.configure(text="--")
    selection_label.configure(text="--")
    insertion_lacpu.configure(text="--")
    insertion_laram.configure(text="--")
    insertion_label.configure(text="--")
    quick_lacpu.configure(text="--")
    quick_laram.configure(text="--")
    quick_label.configure(text="--")
# TÍTULO
label_titulo = ct.CTkLabel(app, text="Monitor de Sistemas", font=("Arial", 45), text_color="#F8F8FF")
label_titulo.place(x=300, y=25)
# CPU
cpu_title_label = ct.CTkLabel(app, text="Uso de CPU", font=("Arial", 30), text_color="#FF4500")
cpu_title_label.place(x=35, y=150)
cpu_label = ct.CTkLabel(app, text="0%", font=("Arial", 30), text_color="#F8F8FF")
cpu_label.place(x=243, y=150)
# RAM
ram_title_label = ct.CTkLabel(app, text="Uso da RAM", font=("Arial", 30), text_color="#3CB371")
ram_title_label.place(x=400, y=150)
ram_label = ct.CTkLabel(app, text="0%", font=("Arial", 30), text_color="#F8F8FF")
ram_label.place(x=610, y=150)
# BUBBLE_SORT
bubble_tittle = ct.CTkLabel(app, text="Bubble Sort", font=("Arial", 30), text_color="#FFD700")
bubble_tittle.place(x=35, y=200)
bubble_label = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
bubble_label.place(x=250, y=200)
bubble_cpu = ct.CTkLabel(app, text="CPU:", font=("Arial", 30), text_color="#FFD700")
bubble_cpu.place(x=400, y=200)
bubble_lacpu = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
bubble_lacpu.place(x=490, y=200)
bubble_ram = ct.CTkLabel(app, text="RAM:", font=("Arial", 30), text_color="#FFD700")
bubble_ram.place(x=615, y=200)
bubble_laram = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
bubble_laram.place(x=705, y=200)
# SELECTION_SORT
selection_tittle = ct.CTkLabel(app, text="Selection Sort", font=("Arial", 30), text_color="#836FFF")
selection_tittle.place(x=35, y=250)
selection_label = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
selection_label.place(x=250, y=250)
selection_cpu = ct.CTkLabel(app, text="CPU:", font=("Arial", 30), text_color="#836FFF")
selection_cpu.place(x=400, y=250)
selection_lacpu = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
selection_lacpu.place(x=490, y=250)
selection_ram = ct.CTkLabel(app, text="RAM:", font=("Arial", 30), text_color="#836FFF")
selection_ram.place(x=615, y=250)
selection_laram = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
selection_laram.place(x=705, y=250)
# INSERTION_SORT
insertion_tittle = ct.CTkLabel(app, text="Insertion Sort", font=("Arial", 30), text_color="#FF69B4")
insertion_tittle.place(x=35, y=300)
insertion_label = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
insertion_label.place(x=250, y=300)
insertion_cpu = ct.CTkLabel(app, text="CPU:", font=("Arial", 30), text_color="#FF69B4")
insertion_cpu.place(x=400, y=300)
insertion_lacpu = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
insertion_lacpu.place(x=490, y=300)
insertion_ram = ct.CTkLabel(app, text="RAM:", font=("Arial", 30), text_color="#FF69B4")
insertion_ram.place(x=615, y=300)
insertion_laram = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
insertion_laram.place(x=705, y=300)
# QUICK_SORT
quick_tittle = ct.CTkLabel(app, text="Quick Sort", font=("Arial", 30), text_color="#1E90FF")
quick_tittle.place(x=35, y=350)
quick_label = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
quick_label.place(x=250, y=350)
quick_cpu = ct.CTkLabel(app, text="CPU:", font=("Arial", 30), text_color="#1E90FF")
quick_cpu.place(x=400, y=350)
quick_lacpu = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
quick_lacpu.place(x=490, y=350)
quick_ram = ct.CTkLabel(app, text="RAM:", font=("Arial", 30), text_color="#1E90FF")
quick_ram.place(x=615, y=350)
quick_laram = ct.CTkLabel(app, text="--", font=("Arial", 30), text_color="#F8F8FF")
quick_laram.place(x=705, y=350)
# VETOR
vetor_tittle = ct.CTkLabel(app, text="Vetor:", font=("Arial", 30), text_color="#F8F8FF")
vetor_tittle.place(x=35, y=100)
vetor_limite = ct.CTkEntry(app, placeholder_text="--", font=("Arial", 20)) # Campo de entrada para o limite do vetor
vetor_limite.place(x=120, y=103)
# BOTÃO_ORDENAR
botao_ordenacao = ct.CTkButton(app, text="Ordenar", font=("Arial", 20), command=alternar_algoritmo) # Botão para alternar os algoritmos
botao_ordenacao.place(x=280, y=103)
# BOTÃO_RESETAR
botao_reset = ct.CTkButton(app, text="Resetar", font=("Arial", 20), command=resetar) # Botão para alternar os algoritmos
botao_reset.place(x=440, y=103)
# BOTÃO_MINIMIZAR
minimizar_button = ctk.CTkButton(app, text="Minimizar", font=("Arial", 20), command=lambda: app.iconify())
minimizar_button.pack(pady=20)
minimizar_button.place(x=600, y=103)
# BOTÃO_FECHAR
fechar_button = ctk.CTkButton(app, text="Fechar", font=("Arial", 20), command=fechar)
fechar_button.place(x=760, y=103)
# CPU_INSTRUÇÕES

# Funções de ordenação
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(array):
    numero = len(array)
    for cont in range(numero):
        index = cont
        for j in range(cont + 1, numero):
            if array[j] < array[index]:
                index = j
        array[cont], array[index] = array[index], array[cont]

def insertion_sort(array):
    numero = len(array)
    for cont in range(1, numero):
        key = array[cont]
        indice = cont - 1
        while indice >= 0 and key < array[indice]:
            array[indice + 1] = array[indice]
            indice -= 1
        array[indice + 1] = key

def quick_sort(array):
    def quick_sort_helper(array, low, high):
        if low < high:
            pivot = partition(array, low, high)
            quick_sort_helper(array, low, pivot - 1)
            quick_sort_helper(array, pivot + 1, high)
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def monitor_uso():
    global max_cpu, max_ram
    max_cpu = 0
    max_ram = 0
    while True:
        uso_cpu = psutil.cpu_percent(interval=1) # Obter uso da CPU
        uso_ram = psutil.virtual_memory().percent # Obter uso da RAM
        max_cpu = max(max_cpu, uso_cpu)
        max_ram = max(max_ram, uso_ram)
        #app.after(0.1, monitor_uso)
        time.sleep(0.1)

# Função para atualizar o uso de CPU e RAM
def atualizar_dados():
    uso_cpu = psutil.cpu_percent(interval=0.1)  # Obter uso da CPU
    uso_ram = psutil.virtual_memory().percent  # Obter uso da RAM
    cpu_label.configure(text=f"{uso_cpu: .2f}%")  # Atualizar labels
    ram_label.configure(text=f"{uso_ram: .2f}%")  # Atualizar labels
    app.after(100, atualizar_dados)

atualizar_dados() # Inicia a atualização de dados e a interface gráfica
#monitor_uso() # Inicia o monitoramento de CPU e RAM
# Função para medir e atualizar os tempos

def medir_tempos(limite):
    vetor = random.sample(range(limite), limite)  # Agora o vetor é gerado com o limite informado pelo usuário
    vetor2 = vetor
    vetor3 = vetor
    vetor4 = vetor
    global max_cpu, max_ram
    if algoritmo_atual == 0:  # Bubble Sort

        inicio1 = time.time()
        arr = vetor[:]
        bubble_sort(arr)
        fim1 = time.time()
        tempo1 = fim1 - inicio1
        print(f"Tempo de bubble_sort em execução: {tempo1} segundos")
        bubble_label.configure(text=f"{tempo1:.3f}s")
        bubble_lacpu.configure(text=f"{max_cpu}%")
        bubble_laram.configure(text=f"{max_ram}%")
        vetor = 0
    elif algoritmo_atual == 1:  # Selection Sort
        inicio = time.time()
        array = vetor2[:]
        selection_sort(array)
        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo de selection_sort em execução: {tempo} segundos")
        selection_label.configure(text=f"{tempo:.3f}s")
        selection_lacpu.configure(text=f"{max_cpu}%")
        selection_laram.configure(text=f"{max_ram}%")
        vetor2 = 0
    elif algoritmo_atual == 2:  # Insertion Sort
        inicio2 = time.time()
        array = vetor3[:]
        insertion_sort(array)
        fim2 = time.time()
        tempo2 = fim2 - inicio2
        print(f"Tempo de insertion_sort em execução: {tempo2} segundos")
        insertion_label.configure(text=f"{tempo2:.3f}s")
        insertion_lacpu.configure(text=f"{max_cpu}%")
        insertion_laram.configure(text=f"{max_ram}%")
        vetor3 = 0
    elif algoritmo_atual == 3:  # Quick Sort
        inicio3 = time.time()
        array = vetor4[:]
        array = quick_sort(array)
        fim3 = time.time()
        tempo3 = fim3 - inicio3
        print(f"Tempo de Quick_sort em execução: {tempo3} segundos")
        quick_label.configure(text=f"{tempo3:.3f}s")
        quick_lacpu.configure(text=f"{max_cpu}%")
        quick_laram.configure(text=f"{max_ram}%")
        vetor4 = 0
if __name__ == "__main__":
    app.mainloop()
