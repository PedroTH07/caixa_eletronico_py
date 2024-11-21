# login com:
#     identificação
#     senha
#     botão entrar
#     cancelar (limpa campos)

import tkinter as tk
janela = tk.Tk()
janela.title('caixa eletrônico - login')
janela.config(bg='blue')
janela.geometry('700x500')
title = tk.Label(janela, text='login', font=('helvetica', 26, 'bold'), bg='blue', fg='orange')
title.pack(pady=15)

# funções
def mostrar():
    global situ_senha
    if not situ_senha:
        senha.config(show='')
        situ_senha = 1
    else:
        senha.config(show='*')
        situ_senha = 0

# campos
id_label = tk.Label(janela, text='nome de usuário:', font=('helvetica', 18, 'bold'), bg='blue', fg='white')
id_label.pack(pady=10)
id_entry = tk.Entry(janela, width=30, font=('helvetica', 18))
id_entry.pack(pady=10)

senha_label = tk.Label(janela, text='insira sua senha:', font=('helvetica', 18, 'bold'), bg='blue', fg='white')
senha_label.pack(pady=10)

frame = tk.Frame(janela, bg='blue')
frame.pack()

senha = tk.Entry(frame, width=30, show='*', font=('helvetica', 18))
senha.grid(pady=10, row=0, column=0)
imagem = tk.PhotoImage(file='img/olho_senha.png')
mostrar_senha = tk.Button(frame, image=imagem, bg='blue', bd=0, command=mostrar)
mostrar_senha.grid(row=0, column=1, pady=10)
situ_senha = 0

# botões
entrar = tk.Button(janela, text='entrar', bd=0, bg='white', font=('helvetica', 18, 'bold'), fg='blue', width=10)
entrar.pack(pady=20)

cancelar = tk.Button(janela, text='cancelar', bd=0, bg='orange', font=('helvetica', 18, 'bold'), fg='white', width=10)
cancelar.pack(pady=10)

janela.mainloop()