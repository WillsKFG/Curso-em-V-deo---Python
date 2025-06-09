from tkinter import*

janela = Tk()

#Funções
def analise():
    if one.get().isnumeric() and two.get().isnumeric and three.get().isnumeric():
        meses = int(three.get()) * 12
        prestacao = float(one.get()) / meses
        porcentagem = float(two.get()) * (30/100)

        if prestacao < porcentagem:
            lb4['text'] = 'APROVADO'
            lb4['bg'] = 'green'
            lb5 = Label(janela, text='Você pagará uma parcela de R${:.2f} durante {} meses.'.format(prestacao, meses),
                    font='40')
            lb5.pack()
        elif prestacao >= porcentagem:
            lb4['text'] = 'RECUSADO'
            lb4['bg'] = 'red'
            lb6 = Label(janela, text='Não atende aos requisitos para aprovação do empréstimo.', font='40')
            lb6.pack()
    else:
        lb4['bg'] = 'red'
        lb4['text'] = 'Valores inválidos! \nPor favor... \ndigite apenas números \n e tente novamente.'


#Labels and entrys

#Valor da casa
lb1 = Label(janela, text='Qual o valor do imóvel?', font=('Verdana', '20', 'italic', 'bold'))
lb1.pack(fill="x")
#Entry valor da casa
one = Entry(janela)
one.pack(fill='x')

#Salário do comprador
lb2 = Label(janela, text='Qual o seu salário mensal?',
            font=('Verdana', '20', 'italic', 'bold'))
lb2.pack(fill="x")
#Entry salário
two = Entry(janela)
two.pack(fill='x')

#Pagamento (tempo)
lb3 = Label(janela, text='Em quantos anos você gostaria de pagar o imóvel?', font=('Verdana', '20', 'italic', 'bold'))
lb3.pack(fill='x')
#Entry tempo
three = Entry(janela)
three.pack(fill='x')

#Botao 'ir'
bt1 = Button(janela, text='SIMULAR', fg='white', bg='orange', font=('Verdana', '40', 'italic', 'bold'), command=analise)
bt1.pack(fill='x')

#Resultado - LABEL
lb4 = Label(janela, text='Aguardando dados...', font=('Verdana', '40', 'italic', 'bold'))
lb4.pack(side='bottom')

#configurações gerais da janela
janela.geometry('800x550+50+50')
janela['bg'] = 'orange'
janela.title('Simulador de empréstimos')
janela.mainloop()