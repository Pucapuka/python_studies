import tkinter as tk
from tkinter import simpledialog, Toplevel, Entry, Button, messagebox, Text
import numpy as np

class AplicacaoMatrizes:
    def __init__(self, root):
        self.root = root
        self.root.title("Operações com Matrizes")

        # Dicionário para armazenar as matrizes
        self.matrizes = {}

        # Botão para adicionar uma matriz
        self.botao_adicionar_matriz = tk.Button(root, text="Adicionar Matriz", command=self.adicionar_matriz)
        self.botao_adicionar_matriz.pack(pady=10)

        # Botão para executar eliminação de Gauss
        self.botao_eliminacao_gauss = tk.Button(root, text="Eliminação de Gauss", command=self.executar_eliminacao_gauss)
        self.botao_eliminacao_gauss.pack(pady=10)

        # Botão para executar fatoração LU
        self.botao_fatoracao_lu = tk.Button(root, text="Fatoração LU", command=self.executar_fatoracao_lu)
        self.botao_fatoracao_lu.pack(pady=10)

        # Caixa de texto para exibir os resultados
        self.text_resultado = Text(root, height=20, width=80)
        self.text_resultado.pack(pady=10)

    def adicionar_matriz(self):
        # Solicitar as dimensões da matriz
        try:
            num_linhas = int(simpledialog.askstring("Número de Linhas", "Digite o número de linhas da matriz:"))
            num_cols = int(simpledialog.askstring("Número de Colunas", "Digite o número de colunas da matriz:"))
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido para o número de linhas e colunas.")
            return

        # Criar uma nova janela para inserir os valores na matriz
        nova_janela = Toplevel(self.root)
        nova_janela.title("Inserir Valores na Matriz")

        # Criar uma grade de Entry para os valores da matriz
        entries = []
        for i in range(num_linhas):
            linha_entries = []
            for j in range(num_cols):
                entry = Entry(nova_janela, width=10)
                entry.grid(row=i, column=j, padx=5, pady=5)
                linha_entries.append(entry)
            entries.append(linha_entries)

        # Função para salvar a matriz
        def salvar_matriz():
            matriz = []
            for i in range(num_linhas):
                linha = []
                for j in range(num_cols):
                    valor = entries[i][j].get()
                    try:
                        valor = float(valor)
                    except ValueError:
                        messagebox.showerror("Erro", "Digite valores numéricos válidos.")
                        return
                    linha.append(valor)
                matriz.append(linha)

            nome_matriz = simpledialog.askstring("Nome da Matriz", "Digite um nome para a matriz:")
            if nome_matriz:
                self.matrizes[nome_matriz] = {
                    'matriz': np.array(matriz)
                }
                self.text_resultado.insert(tk.END, f"Matriz '{nome_matriz}' adicionada:\n")
                self.text_resultado.insert(tk.END, f"{np.array(matriz)}\n")
                nova_janela.destroy()  # Fechar a janela de adicionar matriz

        # Botão para salvar a matriz
        btn_salvar = Button(nova_janela, text="Salvar Matriz", command=salvar_matriz)
        btn_salvar.grid(row=num_linhas, columnspan=num_cols, pady=10)

        # Garantir que a janela de adicionar matriz fique sempre na frente
        nova_janela.attributes('-topmost', 'true')

    def executar_eliminacao_gauss(self):
        matriz_key = simpledialog.askstring("Eliminação de Gauss", "Digite o nome da matriz:")
        if matriz_key in self.matrizes:
            try:
                resultado = self.eliminacao_gauss(matriz_key)
                self.text_resultado.insert(tk.END, f"Resultado da Eliminação de Gauss para a matriz '{matriz_key}':\n")
                self.text_resultado.insert(tk.END, f"{resultado}\n")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Matriz não encontrada", "A matriz especificada não foi encontrada.")

    def executar_fatoracao_lu(self):
        matriz_key = simpledialog.askstring("Fatoração LU", "Digite o nome da matriz:")
        if matriz_key in self.matrizes:
            try:
                L, U, x, y = self.fatoracao_lu(matriz_key)
                self.text_resultado.insert(tk.END, f"Resultado da Fatoração LU para a matriz '{matriz_key}':\n")
                self.text_resultado.insert(tk.END, "L:\n")
                self.text_resultado.insert(tk.END, f"{L}\n")
                self.text_resultado.insert(tk.END, "U:\n")
                self.text_resultado.insert(tk.END, f"{U}\n")
                self.text_resultado.insert(tk.END, "y:\n")
                self.text_resultado.insert(tk.END, f"{y}\n")
                self.text_resultado.insert(tk.END, "x:\n")
                self.text_resultado.insert(tk.END, f"{x}\n")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Matriz não encontrada", "A matriz especificada não foi encontrada.")

    def eliminacao_gauss(self, matriz_key):
        """Eliminação de Gauss para resolver sistemas lineares."""
        A = self.matrizes[matriz_key]['matriz'].astype(float)
        n, m = A.shape

        if m != n + 1:
            raise ValueError("A matriz deve ser aumentada com a coluna dos termos constantes para a eliminação de Gauss.")

        # Etapa de eliminação
        for i in range(n):
            # Pivoteamento parcial
            max_index = i
            for k in range(i + 1, n):
                if abs(A[k, i]) > abs(A[max_index, i]):
                    max_index = k
            if max_index != i:
                A[[i, max_index]] = A[[max_index, i]]

            # Verificar se o pivô é zero
            if A[i, i] == 0:
                raise ValueError("A matriz não pode ser fatorada pela eliminação de Gauss (pivô zero encontrado).")

            # Zerar abaixo do pivô
            for j in range(i + 1, n):
                ratio = A[j, i] / A[i, i]
                A[j, i:] -= ratio * A[i, i:]

        # Resolução do sistema triangular superior
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (A[i, n] - np.dot(A[i, i+1:n], x[i+1:n])) / A[i, i]

        return x

    def fatoracao_lu(self, matriz_key):
        """Fatoração LU de uma matriz."""
        matriz = self.matrizes[matriz_key]['matriz']
        n = len(matriz)
        L = np.eye(n)
        U = matriz[:, :-1].copy()

        for i in range(n):
            for j in range(i + 1, n):
                if U[i, i] == 0:
                    raise ValueError("A matriz não pode ser fatorada pela eliminação de Gauss (pivô zero encontrado).")
                ratio = U[j, i] / U[i, i]
                L[j, i] = ratio
                U[j, i:] -= ratio * U[i, i:]

        # Vetor b (última coluna da matriz original)
        b = matriz[:, -1]

        # Remove a última coluna da matriz U, pois ela é o vetor b
        #U = U[:, :-1]

        # Resolve Ly = b usando substituição direta
        y = np.zeros(n)
        for i in range(n):
            y[i] = b[i] - np.dot(L[i, :i], y[:i])

        # Resolve Ux = y usando substituição reversa
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

        return L, U, x, y

# Criando a janela principal da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoMatrizes(root)
    root.mainloop()
