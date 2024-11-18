import psutil
import customtkinter as ct
import random
import time

ct.set_appearance_mode("black")  # definir aparência da interface
ct.set_default_color_theme("dark-blue")  # definir cor da interface
app = ct.CTk()
app.geometry("720x480")  # definir a dimensão da interface
app.title("System Monitorator")  # definir título da interface
app.resizable(False, False)  # impedir redimensionamento
#TÍTULO
label_titulo = ct.CTkLabel(app, text="Monitor de Sistemas", font=("Arial", 45), text_color="#FF4500")
label_titulo.place(x=100, y=25)
#CPU
cpu_title_label = ct.CTkLabel(app, text="Uso de CPU", font=("Arial", 30), text_color="#FF4500")
cpu_title_label.place(x=35, y=100)
cpu_label = ct.CTkLabel(app, text="0%", font=("Arial", 30))
cpu_label.place(x=450, y=100)
#RAM
ram_title_label = ct.CTkLabel(app, text="Uso da RAM", font=("Arial", 30), text_color="#00FF00")
ram_title_label.place(x=35, y=150)
ram_label = ct.CTkLabel(app, text="0%", font=("Arial", 30))
ram_label.place(x=450, y=150)
#BUBBLE_SORT
bubble_tittle = ct.CTkLabel(app, text="Bubble Sort", font=("Arial", 30), text_color="#00BFFF" )
bubble_tittle.place(x=35, y=200)
bubble_label = ct.CTkLabel(app, text="--", font=("Arial", 30))
bubble_label.place(x=450, y=200)
#SELECTION_SORT
selection_tittle = ct.CTkLabel(app, text="Selection Sort", font=("Arial", 30), text_color="#FF00FF" )
selection_tittle.place(x=35, y=250)
selection_label = ct.CTkLabel(app, text="--", font=("Arial", 30))
selection_label.place(x=450, y=250)
#INSERTION_SORT
insertion_tittle = ct.CTkLabel(app, text="Insertion Sort", font=("Arial", 30), text_color="#FFFF00" )
insertion_tittle.place(x=35, y=300)
insertion_label = ct.CTkLabel(app, text="--", font=("Arial", 30))
insertion_label.place(x=450, y=300)
#QUICK_SORT
quick_tittle = ct.CTkLabel(app, text="Quick Sort", font=("Arial", 30), text_color="#FF0000" )
quick_tittle.place(x=35, y=350)
quick_label = ct.CTkLabel(app, text="--", font=("Arial", 30))
quick_label.place(x=450, y=350)

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
def quick_sort(array):   # Recebe uma lista como argumento e aplica a ordenação
  # Função auxiliar "helper" realiza a ordenação recursiva que recebe a lista, índice inicial e final
  def quick_sort_helper(array, low, higt):
    if low < higt:        # Verifica se há ainda elementos para ordenar até o fim
      pivot = partition(array, low, higt)  # Função para encontre o índice do pivô e separar números menores a esquerda e maiores a direita
      # Ordenar as duas metades
      quick_sort_helper(array, low, pivot - 1)    # Recursão para a parte esquerda
      quick_sort_helper(array, pivot + 1, higt)  # Recursão para a parte direita
  def partition(array, low, higt): # Função respons. p/ organizar os elementos em torno de um pivô
    pivot = array[higt]  # O pivô é o último elemento
    i = low - 1     # Usado para rastrear a posição até onde os elementos menores ou iguais ao pivô devem ir
    for j in range(low, higt):  # Começa o loop FOR que percorre a sub-lista "low" e "high - 1"
      if array[j] <= pivot:    # Para cada elementos "array[j] verifica se ele é menor ou igual ao pivô, coloca na parte esquerda da lista
        i += 1                 # Incremenda o índice "i"
        array[i], array[j] = array[j], array[i]    # Troca os elementos array[i] e array[j]
    array[i + 1], array[higt] = array[higt], array[i+1]     # Coloca o pivô na posição "i + 1" que é o local correto
    return i + 1         # Retorna o índice final do pivô
# Chama a função recursiva para ordenar o array
  quick_sort_helper(array, 0, len(array)- 1) # A função chama os índices 0 e len(array) - 1, para ordenar a lista inteira usando a abordagem recursiva.
  return array   # Retorna o array ordenado

def atualizar_dados():
    uso_cpu = psutil.cpu_percent()   # Obter uso da CPU
    uso_ram = psutil.virtual_memory().percent    # Obter uso da RAM
    cpu_label.configure(text = f"{uso_cpu}%")   # Atualizar labels
    ram_label.configure(text = f"{uso_ram}%")   # Atualizar labels
    app.after(100, atualizar_dados)
def medir_tempos():
    vetor = random.sample(range(1000), 1000)
    vetor2 = vetor
    vetor3 = vetor
    vetor4 = vetor
    #bubble_sort
    inicio1 = time.time()
    arr = vetor[:]
    bubble_sort(arr)
    fim1 = time.time()
    tempo1 = fim1 - inicio1
    print(f"Tempo de bubble_sort em execução: {tempo1} segundos")
    bubble_label.configure(text=f"{tempo1:.4f}s")
    # print(arr)

    #selection_sort
    inicio = time.time()
    array = vetor2[:]
    selection_sort(array)
    fim = time.time()
    tempo = fim - inicio
    print(f"Tempo de selection_sort em execução: {tempo} segundos")
    selection_label.configure(text=f"{tempo:.4f}s")
    # print(array)

    #insertion_sort
    inicio2 = time.time()
    array = vetor3[:]
    insertion_sort(array)
    fim2 = time.time()
    tempo2 = fim2 - inicio2
    print(f"Tempo de insertion_sort em execução: {tempo2} segundos")
    insertion_label.configure(text=f"{tempo2:.4f}s")
    # print(array)

    #Quick_sort
    inicio3 = time.time()
    array = vetor4[:]
    array = quick_sort(array)
    fim3 = time.time()
    tempo3 = fim3 - inicio3
    print(f"Tempo de Quick_sort em execução: {tempo3} segundos")
    quick_label.configure(text=f"{tempo3:.4f}s")
    # print(array)
atualizar_dados()
medir_tempos()
if __name__ == "__main__":
    app.mainloop()