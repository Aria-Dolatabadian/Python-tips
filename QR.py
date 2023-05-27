import pyqrcode
text = "www.google.com"

qr_code = pyqrcode.create(text)
qr_code.svg ("qr.svg",scale = 10)
