# saque:
#     saldo na conta (label)
#     campo para informar valor de saque (entry)
#     botão para confirmar saque (button)
# telas precisam ter:
#     identificação do usuario
#     botão para sair
#     botão para voltar para o menu

import tkinter as tk
janela = tk.Tk()
janela.geometry('700x500')
janela.title('caixa eletrônico - saque')
janela.config(bg='white')

def olho():
    global verificacao
    if not verificacao:
        saldo.config(bg='white', fg='black')
        verificacao = 1
    else:
        saldo.config(bg='gray', fg='gray')
        verificacao = 0

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
root.grid(sticky='ew', row=3)

# saldo
titulo = tk.Frame(janela, bg='white')
titulo.grid(sticky='ew', row=1)
title = tk.Label(titulo, text='saque', font=('helvetica', 24, 'bold'), bg='white')
title.pack(pady=20)

frame = tk.Frame(janela, bg='white')
frame.grid(row=2, sticky='ew')

saldo_label = tk.Label(frame, text='saldo:', bg='white', font=('helvetica', 20, 'bold'))
saldo_label.grid(pady=15, row=0, column=0,padx=10)

saldo = tk.Label(frame, text=f'R$100.00', bg='gray', font=('helvetica', 20, 'bold'), fg='gray')
saldo.grid(row=0, column=1, pady=15, padx=10)
verificacao = 0

olho_senha = tk.PhotoImage(file='img/olho_senha.png')
ocultar = tk.Button(frame, bd=0, bg='white', image=olho_senha, command=olho)
ocultar.grid(row=0, column=2, pady=15, padx=10)

# valor de saque
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
saque_label = tk.Label(root, text='valor do saque:', bg='white', font=('helvetica', 18, 'bold'))
saque_label.grid(row=0, column=0, pady=15)
saque = tk.Entry(root, font=('helvetica', 16, 'bold'), bg='lightgray')
saque.grid(row=0, column=1, pady=15)

# confirmar saque
botao = tk.Frame(janela, bg='white')
botao.grid(sticky='ew', row=4)
comfirm = tk.Button(botao, text='confirmar saque', bd=0, bg='blue', fg='white', font=('helvetica', 18, 'bold'))
comfirm.pack(pady=20)

janela.mainloop()