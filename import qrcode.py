import qrcode

texto = "https://www.linkedin.com/in/felipe-m-kurjata/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = texto

qr.add_data(texto)
qr.make(fit=True)

img = qr.make_image(fill_color="preto", back_color="branco")
img.save("qrcode.png")