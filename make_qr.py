"""Uso: python make_qr.py https://TU_USUARIO.github.io/tomato-ai/ [salida.png]"""
import sys, qrcode
from qrcode.constants import ERROR_CORRECT_H
url = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else "qr_tomato_ai.png"
qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=40, border=4)
qr.add_data(url); qr.make(fit=True)
qr.make_image(fill_color="#0f3321", back_color="white").save(out)
print("QR guardado en", out)
