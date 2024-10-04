import tkinter as tk
from tkinter import messagebox, simpledialog
from github import Github
from PIL import Image, ImageTk  # Importando para manipulação de imagens

# Substitua pelo seu token de acesso pessoal do GitHub
GITHUB_TOKEN = ''

# Autenticação
g = Github(GITHUB_TOKEN)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x500")
        self.root.configure(bg="#F0F8FF")  # Cor mais agradável: AliceBlue

        # Lista de tarefas
        self.tasks = []
        self.gist_id = None

        # Entrada de texto
        self.task_entry = tk.Entry(root, width=40, font=('Arial', 14), fg='black', bg='#D3D3D3')
        self.task_entry.pack(pady=10)

        # Botão de adicionar tarefa
        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task, 
                                    font=('Arial', 12, 'bold'), fg='black', bg='#B0C4DE', 
                                    relief='raised', bd=3)
        self.add_button.pack(pady=5)

        # Listbox para mostrar as tarefas
        self.task_listbox = tk.Listbox(root, height=10, width=40, font=('Arial', 14), 
                                       fg='black', bg='#F0F8FF', selectbackground="#B0C4DE", selectforeground="black")
        self.task_listbox.pack(pady=10)

        # Frame para os botões de edição e exclusão
        button_frame = tk.Frame(root, bg="#F0F8FF")
        button_frame.pack(pady=10)

        # Carregar ícones
        self.edit_icon = ImageTk.PhotoImage(Image.open("edit.png").resize((20, 20)))
        self.trash_icon = ImageTk.PhotoImage(Image.open("trash.png").resize((20, 20)))
        self.github_icon = ImageTk.PhotoImage(Image.open("github.png").resize((20, 20)))  # Ícone do GitHub

        # Botão de editar tarefa
        self.edit_button = tk.Button(button_frame, image=self.edit_icon, command=self.edit_task, 
                                     font=('Arial', 12, 'bold'), fg='black', bg='#B0C4DE', 
                                     relief='raised', bd=3)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        # Botão de apagar tarefa
        self.delete_button = tk.Button(button_frame, image=self.trash_icon, command=self.delete_task, 
                                       font=('Arial', 12, 'bold'), fg='black', bg='#B0C4DE', 
                                       relief='raised', bd=3)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Botão de salvar no GitHub com ícone
        self.save_button = tk.Button(root, text="Salvar no GitHub", 
                                     compound=tk.LEFT, command=self.save_to_gist, 
                                     font=('Arial', 12, 'bold'), fg='black', bg='#B0C4DE', 
                                     relief='raised', bd=3)
        self.save_button.pack(pady=5)

        # Botão de puxar lista do GitHub
        self.pull_button = tk.Button(root, text="Puxar do GitHub", command=self.load_tasks_from_gist, 
                                     font=('Arial', 12, 'bold'), fg='black', bg='#B0C4DE', 
                                     relief='raised', bd=3)
        self.pull_button.pack(pady=5)

        # Bind da tecla Enter para adicionar tarefa
        self.task_entry.bind('<Return>', lambda event: self.add_task())

    # Função para adicionar uma tarefa
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Digite uma tarefa.")

    # Atualiza a Listbox com numeração
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")

    # Função para salvar no GitHub Gist
    def save_to_gist(self):
        content = "\n".join(self.tasks)
        file_name = 'todo_list.txt'
        if self.gist_id:
            # Atualizar uma Gist existente
            gist = g.get_gist(self.gist_id)
            gist.edit(description="Atualização da To-Do List",
                      files={file_name: github.InputFileContent(content)})
            messagebox.showinfo("Gist Atualizada", f'Gist {self.gist_id} atualizada com sucesso!')
        else:
            # Criar uma nova Gist
            gist = g.get_user().create_gist(public=True,
                                            files={file_name: github.InputFileContent(content)},
                                            description="To-Do List")
            self.gist_id = gist.id
            messagebox.showinfo("Nova Gist", f'Nova Gist criada: {gist.html_url}')

    # Função para carregar tarefas da Gist (se já existir)
    def load_tasks_from_gist(self):
        gist_id = simpledialog.askstring("Gist ID", "Digite o ID da Gist para puxar a lista:")
        if gist_id:
            try:
                gist = g.get_gist(gist_id)
                content = gist.files['todo_list.txt'].content
                self.tasks = content.split("\n")
                self.update_task_listbox()
                self.gist_id = gist_id
                messagebox.showinfo("Lista carregada", "Lista de tarefas carregada do GitHub!")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível carregar a lista: {str(e)}")

    # Função para editar uma tarefa
    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Editar Tarefa", "Edite a tarefa:", initialvalue=self.tasks[selected_task_index])
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Erro", "Selecione uma tarefa para editar.")

    # Função para apagar uma tarefa
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Erro", "Selecione uma tarefa para apagar.")

# Inicializar a interface
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
