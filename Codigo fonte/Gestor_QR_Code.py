import qrcode

codigo = qrcode.make("MEL100001A")
codigo.save("MEL100001A.jpg")