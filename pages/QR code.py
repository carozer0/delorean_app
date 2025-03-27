import streamlit as st
import qrcode
from PIL import Image
import io

# Lien vers ton app Streamlit (exemple)
url = "https://delorean.streamlit.app/"

# Génération du QR code
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Affichage dans Streamlit
st.title("Scan to time travel !")

# Convertir l’image en bytes
buf = io.BytesIO()
img.save(buf)
buf.seek(0)

# Affichage
st.image(buf, caption="app QR Code", width=400)
