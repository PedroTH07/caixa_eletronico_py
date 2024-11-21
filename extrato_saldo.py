# extrato/saldo
# mostrar últimas movimentações da conta
# botão para imprimir
# telas precisam ter:
#     identificação do usuario
#     botão para sair
#     botão para voltar para o menu

import tkinter as tk
main = tk.Tk()
main.geometry('700x500')
main.title('caixa eletrônico - extrato')
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
janela = tk.Frame(main, bg='white')
janela.grid(sticky='ew')

title = tk.Label(janela, text='extrato', bg='white', font=('helvetica', 24, 'bold'))
title.pack(pady=10)

extrato = {
    200.00: 'pedro',
    -100.00: 'joão',
    400.00: 'ricardo',
    -700.00: 'tigrinho'
}

root = tk.Frame(janela, bg='white')
root.pack()

for n in extrato:
    if n > 0:
        label2 = tk.Label(root, bg='white', text=extrato[n], font=('helvetica', 18, 'bold'))
        label2.grid()
        label = tk.Label(root, text=f'R${n}', bg='white', fg='green', font=('helvetica', 16, 'bold'))
        label.grid()
    else:
        label2 = tk.Label(root, bg='white', text=extrato[n], font=('helvetica', 18, 'bold'))
        label2.grid()
        label = tk.Label(root, text=f'R${n}', bg='white', fg='red', font=('helvetica', 16, 'bold'))
        label.grid()

btn = tk.Button(janela, text='imprimir', bd=0, bg='blue', fg='white', font=('helvetica', 16, 'bold'))
btn.pack(pady=20)

main.mainloop()