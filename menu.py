# menu:
#     botões:
#         saque: (feito)
#         depósito: (feito)
#         extrato/saldo: (feito)
#         transferência: (feito)
#         pagamentos: (feito)
#         empréstimos: (feito)

import tkinter as tk
janela = tk.Tk()
janela.geometry('700x500')
janela.title('caixa eletrônico - menu')
janela.config(bg='white')

# cabeçalho (header)
janela.columnconfigure(0, weight=1)
header = tk.Frame(janela, bg='blue', height=50)
# header.grid_propagate(False)
header.grid(sticky='ew', column=0, row=0)

id_user = tk.Label(header, text='usuario', font=('helvetica', 15, 'bold'), fg='white', bg='blue')
id_user.grid(column=0, row=0, pady=10, padx=30)

banco = tk.Label(header, text='MyBank', font=('helvetica', 20, 'bold'), bg='blue', fg='darkorange')
banco.grid(column=1, row=0, pady=10, padx=160)

image = tk.PhotoImage(file='img/logout.png')
logout = tk.Button(header, image=image, bd=0, bg='blue')
logout.grid(column=3, row=0, pady=10, padx=25)

title = tk.Label(janela, text='menu', bg='white', font=('helvetica', 24, 'bold'))
title.grid(pady=15)

# botões
menu = tk.Frame(janela, bg='white')
menu.grid(sticky='ew')
menu.columnconfigure(0, weight=1)
menu.columnconfigure(1, weight=1)

saque = tk.Button(menu, text='Saque', font=('helvetica', 18, 'bold'), bd=0, bg='blue', fg='white', width=15)
saque.grid(pady=20, row=0, column=0)

deposito = tk.Button(menu, text='Deposito', font=('helvetica', 18, 'bold'), bd=0, bg='blue', fg='white', width=15)
deposito.grid(pady=20, row=1, column=0)

extrato = tk.Button(menu, text='Extrato/Saldo', font=('helvetica', 18, 'bold'), bd=0, bg='blue', fg='white', width=15)
extrato.grid(pady=20, row=2, column=0)

tranferencia = tk.Button(menu, text='Transferência', font=('helvetica', 18, 'bold'), bd=0, bg='blue', fg='white', width=15)
tranferencia.grid(pady=20, row=0, column=1)

pagamentos = tk.Button(menu, text='Pagamentos', font=('helvetica', 18, 'bold'), bd=0, bg='blue', fg='white', width=15)
pagamentos.grid(pady=20, row=1, column=1)

emprestimos = tk.Button(menu, text='Empréstimos', font=('helvetica', 18, 'bold'), bd=0, bg='blue', fg='white', width=15)
emprestimos.grid(pady=20, row=2, column=1)

janela.mainloop()