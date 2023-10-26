from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from aluno import Aluno

class App:
    def __init__(self):
        self.alunos = []
        self.janela = Tk()
        self.janela.title('SysAlunos')
        self.labelMatricula = Label(self.janela, text="Matrícula: ", font="Tahoma 14 bold", fg="red")
        self.labelMatricula.grid(row=0, column=0)
        self.txtMatricula = Entry(self.janela, font="Tahoma 14", width=27, state=DISABLED)
        self.txtMatricula.grid(row=0, column=1)
        self.labelNome = Label(self.janela, text="Nome: ", font="Tahoma 14 bold", fg="red")
        self.labelNome.grid(row=1, column=0)
        self.txtNome = Entry(self.janela, font="Tahoma 14", width=27)
        self.txtNome.grid(row=1, column=1)
        self.labelIdade = Label(self.janela, text="Idade: ", font="Tahoma 14 bold", fg="red")
        self.labelIdade.grid(row=2, column=0)
        self.txtIdade = Entry(self.janela, font="Tahoma 14", width=27)
        self.txtIdade.grid(row=2, column=1)
        self.labelCurso = Label(self.janela, text="Curso: ", font="Tahoma 14 bold", fg="red")
        self.labelCurso.grid(row=3, column=0)
        self.cursos = ['Python', 'Javascript', 'Django', 'Reactjs']
        self.cbCursos = ttk.Combobox(self.janela, values=self.cursos, width=28, font="Tahoma 12")
        self.cbCursos.grid(row=3, column=1)
        self.labelNota = Label(self.janela, text="Nota: ", font="Tahoma 14 bold", fg="red")
        self.labelNota.grid(row=4, column=0)
        self.txtNota = Entry(self.janela, font="Tahoma 14", width=27)
        self.txtNota.grid(row=4, column=1)
        self.buttonAdicionar = Button(self.janela, font="Tahoma 12 bold", width=7, text="Adicionar", fg="red", command=self.adicionarAluno)
        self.buttonAdicionar.grid(row=5, column=0)
        self.buttonEditar = Button(self.janela, font="Tahoma 12 bold", width=7, text="Editar", fg="red", command=self.editarAluno)
        self.buttonEditar.grid(row=5, column=1)
        self.buttonDeletar = Button(self.janela, font="Tahoma 12 bold", width=7, text="Deletar", fg="red", command=self.deletarAluno)
        self.buttonDeletar.grid(row=5, column=2)
        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)
        self.colunas = ['Matricula', 'Nome', 'Idade', 'Curso', 'Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show='headings')
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
        self.tabela.pack()
        self.tabela.bind('<ButtonRelease-1>', self.selecionarAluno)
        self.janela.mainloop()

    def adicionarAluno(self) -> None:
        nome = self.txtNome.get()
        idade = int(self.txtIdade.get())
        curso = self.cbCursos.get()
        nota = float(self.txtNota.get())
        aluno = Aluno(nome, idade, curso, nota)
        self.alunos.append(aluno)
        messagebox.showinfo("Sucesso!", "Aluno adicionado com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.txtNome.delete(0, END)
        self.txtIdade.delete(0, END)
        self.txtNota.delete(0, END)
        self.cbCursos.set("")
        self.txtMatricula.config(state=NORMAL)
        self.txtMatricula.delete(0, END)
        self.txtMatricula.config(state=DISABLED)

    def atualizarTabela(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        for aluno in self.alunos:
            self.tabela.insert("", END, values=(aluno.matricula, aluno.nome, aluno.idade, aluno.curso, aluno.nota))

    def selecionarAluno(self, event):
        linhaSelecionada = self.tabela.selection()[0]
        item = self.tabela.item(linhaSelecionada)['values']
        self.limparCampos()
        self.txtMatricula.config(state=NORMAL)
        self.txtMatricula.insert(0, item[0])
        self.txtMatricula.config(state=DISABLED)
        self.txtNome.insert(0, item[1])
        self.txtIdade.insert(0, str(item[2]))
        self.cbCursos.set(item[3])
        self.txtNota.insert(0, str(item[4]))

    def editarAluno(self):
        matricula = self.txtMatricula.get()
        for aluno in self.alunos:
            if str(aluno.matricula) == matricula:
                aluno.nome = self.txtNome.get()
                aluno.idade = int(self.txtIdade.get())
                aluno.curso = self.cbCursos.get()
                aluno.nota = float(self.txtNota.get())
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo("Atualizado!", "Dados atualizados com sucesso!")

    def deletarAluno(self):
        matricula = self.txtMatricula.get()
        for aluno in self.alunos:
            if str(aluno.matricula) == matricula:
                self.alunos.remove(aluno)
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo("Removido!", "Dados removidos com sucesso!")

if __name__ == "__main__":
    app = App()