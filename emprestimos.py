# emprestimos
# valor disponivel
# taxas de juros
# parcelas(escolhe)
# valor da parcela (atualiza conforme parcela)
# check de concordo com os termos
# botão para confirmar
# telas precisam ter:
#     identificação do usuario
#     botão para sair
#     botão para voltar para o menu

import tkinter as tk
main = tk.Tk()
main.geometry('700x500')
main.title('caixa eletrônico - empréstimos')
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

# função
estado = 0
def mostrar():
    global estado
    if not estado:
        saldo.config(bg='white', fg='black')
        estado = 1
    else:
        saldo.config(bg='gray', fg='gray')
        estado = 0

# campos
titulo = tk.Frame(main, bg='white')
titulo.grid(row=1, sticky='ew')
title = tk.Label(titulo, text='empréstimos', bg='white', font=('hevlvetica', 20, 'bold'))
title.pack(pady=10)

labels = tk.Frame(main, bg='white')
labels.grid(row=2, sticky='ew')
labels.columnconfigure(0, weight=1)
labels.columnconfigure(1, weight=1)
limite_saque = tk.Label(labels, text=f'limite de saque: R$20000.00', bg='white', font=('helvetica', 14, 'bold'))
limite_saque.grid(column=0, padx=30, row=0)

saldo_label = tk.Label(labels, text='saldo:', bg='white', font=('helvetica', 14, 'bold'))
saldo_label.grid(row=0, column=1)

saldo = tk.Label(labels, text=f'R$200.00', bg='gray', fg='gray', font=('helvetica', 14, 'bold'))
saldo.grid(column=2, row=0, padx=30)

imagem = tk.PhotoImage(file='img/olho_senha.png')
olho = tk.Button(labels, image=imagem, bd=0, bg='white', command=mostrar)
olho.grid(column=3, row=0)

parcelas = tk.Frame(main, bg='white')
parcelas.grid(row=3, sticky='ew')
parcelas.columnconfigure(0, weight=1)
parcelas.columnconfigure(1, weight=1)

taxa_juro = tk.Label(parcelas, text=f'taxa de juros: 10%', bg='white', font=('helvetica', 14, 'bold'))
taxa_juro.grid(pady=10, row=0, column=1)

parcelas_label = tk.Label(parcelas, text='parcelas:', bg='white', font=('helvetica', 14, 'bold'))
parcelas_label.grid(row=0, column=0, pady=10)

qnt_parcelas = tk.IntVar()
parcelas3 = tk.Radiobutton(parcelas, text='3 parcelas', bg='white', font=('helvetica', 14), variable=qnt_parcelas, value=1)
parcelas3.grid()
parcelas6 = tk.Radiobutton(parcelas, text='6 parcelas', bg='white', font=('helvetica', 14), variable=qnt_parcelas, value=2)
parcelas6.grid()
parcelas9 = tk.Radiobutton(parcelas,  text='9 parcelas', bg='white', font=('helvetica', 14), variable=qnt_parcelas, value=3)
parcelas9.grid()
parcelas12 = tk.Radiobutton(parcelas,  text='12 parcelas', bg='white', font=('helvetica', 14), variable=qnt_parcelas, value=4)
parcelas12.grid()

valor_parecela_label = tk.Label(parcelas, text='valor das parcelas:', bg='white', font=('helvetica', 14, 'bold'))
valor_parecela_label.grid(row=1, column=1)
valor_parcela = tk.Label(parcelas, text=f'R$200.00', bg='white', font=('helvetica', 14, 'bold'))
valor_parcela.grid(row=2, column=1)

# botões
botoes = tk.Frame(main, bg='white')
botoes.grid(row=4, sticky='ew')

termos = tk.BooleanVar()
btn_termos = tk.Checkbutton(botoes, bg='white', font=('helvetica', 14), text='concordo com os termos', variable=termos)
btn_termos.pack(pady=10)

confirmar = tk.Button(botoes, bg='blue', fg='white', bd=0, text='confirmar', font=('helvetica', 16, 'bold'))
confirmar.pack(pady=5)

main.mainloop()