import qrcode
from tkinter import *


def Gerar_QR_Code():
    codigo = qrcode.make("MEL100001A")
    codigo.save("MEL100001A.jpg")

    texto["text"] = "MEL100001A"



janela = Tk()
janela.title("Gerenciador de codigos QR Code")
janela.geometry("300x200")
#informacao = Label(janela, text="Clique no botão para gerar um novo QR Code")
#informacao.grid(column=0,row=0)

botao = Button(janela, text="Gerar um novo QR Code",command=Gerar_QR_Code)
botao.grid(column=0,row=1,padx=80,pady=20)


texto = Label(janela, text="",padx=20,pady=20)
texto.grid(column=0,row=2)
janela.mainloop()