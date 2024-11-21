# transferencias
# campo para informar [
#     destinatário da transferencia
#     valor da transferencia
#     botão para confirmar
# ]
# telas precisam ter:
#     identificação do usuario
#     botão para sair
#     botão para voltar para o menu

import tkinter as tk
main = tk.Tk()
main.config(bg='white')
main.geometry('700x500')
main.title('caixa eletrônico - transferência')

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
titulo.grid(row=1, sticky='ew')
title = tk.Label(titulo, text='transferência', bg='white', font=('helvetca', 24, 'bold'))
title.pack(pady=25)

root = tk.Frame(main, bg='white')
root.grid(row=2, sticky='ew')

destinatario_label = tk.Label(root, text='destinatário:', bg='white', font=('helvetica', 18, 'bold'))
destinatario_label.grid(row=0, column=0, pady=20, padx=20)
destinatario = tk.Entry(root, width=30, font=('helvetica', 16), bg='lightgray')
destinatario.grid(row=0, column=1, pady=20)

valor_label = tk.Label(root, text='valor:', bg='white', font=('helvetica', 18, 'bold'))
valor_label.grid(row=1, column=0, pady=20, padx=20)
valor = tk.Entry(root, font=('helvetica', 16), bg='lightgray')
valor.grid(row=1, column=1, pady=20)

botao = tk.Frame(main, bg='white')
botao.grid(row=3, sticky='ew')

btn = tk.Button(botao, text='confirmar', bd=0, bg='blue', fg='white', font=('helvetica', 18, 'bold'))
btn.pack(pady=20)

main.mainloop()