# deposito
# campo para informar [
#     destinário do depósito
#     valor do depósito
#     botão para confirmar
# ]
# telas precisam ter:
#     identificação do usuario
#     botão para sair
#     botão para voltar para o menu

import tkinter as tk
janela = tk.Tk()
janela.geometry('700x500')
janela.config(bg='white')
janela.title('caixa eletrônico - deposito')

# cabeçalho (header)
janela.columnconfigure(0, weight=1)
header = tk.Frame(janela, bg='blue', height=50)
# header.grid_propagate(False)
header.grid(sticky='ew', column=0, row=0)

id_user = tk.Label(header, text='usuario', font=('helvetica', 15, 'bold'), fg='white', bg='blue')
id_user.grid(column=0, row=0, pady=10, padx=30)

banco = tk.Label(header, text='MyBank', font=('helvetica', 20, 'bold'), bg='blue', fg='darkorange')
banco.grid(column=1, row=0, pady=10, padx=160)

imagem = tk.PhotoImage(file='img/voltar.png')
voltar_menu = tk.Button(header, image=imagem, bg='blue', bd=0)
voltar_menu.grid(column=2, row=0, pady=10, padx=15)

image = tk.PhotoImage(file='img/logout.png')
logout = tk.Button(header, image=image, bd=0, bg='blue')
logout.grid(column=3, row=0, pady=10, padx=10)

# campos
root = tk.Frame(janela, bg='white')
root.grid(row=2, column=0, sticky='ew')
titulo = tk.Frame(janela, bg='white')
titulo.grid(row=1, sticky='ew')

title = tk.Label(titulo, text='depósito', bg='white', font=('helvetica', 24, 'bold'))
title.pack(pady=20)

destinatario_label = tk.Label(root, text='destinátario:', bg='white', font=('helvetica', 18, 'bold'))
destinatario_label.grid(pady=20, row=0, column=0)
destinatario = tk.Entry(root, width=30, font=('helvetica', 16), bg='lightgray')
destinatario.grid(pady=20, row=0, column=1)

deposito_label = tk.Label(root, text='valor do deposito:', font=('helvetica', 18, 'bold'), bg='white')
deposito_label.grid(pady=20, row=1, column=0)
deposito = tk.Entry(root, font=('helvetica', 16), bg='lightgray')
deposito.grid(pady=20, row=1, column=1)

botao = tk.Frame(janela, bg='white')
botao.grid(row=3, sticky='ew')
confirmar = tk.Button(botao, text='confirmar', font=('helvetica', 18, 'bold'), bd=0, bg='blue', fg='white')
confirmar.pack(pady=20)

janela.mainloop()