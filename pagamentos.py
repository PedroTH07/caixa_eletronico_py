# pagamentos
# campo para informar código de barras
# labels para mostrar valor e data de vencimento
# botão para confirmar
# telas precisam ter:
#     identificação do usuario
#     botão para sair
#     botão para voltar para o menu

import tkinter as tk

main = tk.Tk()
main.geometry('700x500')
main.title('caixa eletrônico - pagamentos')
main.config(bg='white')

# cabeçalho (header)
main.columnconfigure(0, weight=1)
header = tk.Frame(main, bg='blue', height=50)
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
titulo = tk.Frame(main, bg='white')
titulo.grid(sticky='ew', row=1)
title = tk.Label(titulo, text='pagamentos', bg='white', font=('helvetica', 24, 'bold'))
title.pack(pady=20)

# frame para posiocionar outros frames
frame = tk.Frame(main, bg='white')
frame.grid(sticky='ew', row=2, pady=20)

# código de barras
codigo_barras = tk.Frame(frame, bg='lightgray', height=200, width=300)
codigo_barras.grid_propagate(False)
codigo_barras.grid(row=0, column=0, padx=40)
alt = tk.Label(codigo_barras, text='código de barras', bg='lightgray', font=('helvetica', 14, 'bold'))
alt.grid(pady=10)

# labels
labels = tk.Frame(frame, bg='white')
labels.grid(row=0, column=1)

valor = tk.Label(labels, text=f'valor: R$500.00', bg='white', font=('helvetica', 17, 'bold'))
valor.pack(pady=20)

vencimento = tk.Label(labels, text=f'vencimento: 30/12/2024', bg='white', font=('helvetica', 17, 'bold'))
vencimento.pack(pady=20)

# botao
confirmar = tk.Button(main, text='confirmar', bd=0, bg='blue', fg='white', font=('helvetica', 16, 'bold'))
confirmar.grid(row=3, pady=10)

main.mainloop()