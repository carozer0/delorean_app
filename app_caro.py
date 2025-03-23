import os
import streamlit as st
import requests
from PIL import Image

st.set_page_config(layout="wide")
st.title("🎨 DeLorean Art Program ")

# Base API URL selon l’environnement
if 'API_URI' in os.environ:
    BASE_URI = st.secrets[os.environ.get('API_URI')]
else:
    BASE_URI = st.secrets['cloud_api_uri']

BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
url = BASE_URI + 'upload_image'

uploaded_file = st.file_uploader("Who’s ready to hop in the DeLorean?", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Ready for time travel", width=300)

    if st.button("🔍 Fire up the DeLorean! ⚡🕒🚗"):
        with st.spinner("The flux capacitor is fluxing..."):
            files = {"img": uploaded_file.getvalue()}
            response = requests.post(url, files={"img": files["img"]})

        if response.status_code == 200:
            data = response.json()
            st.success("Great Scott!")

            neighbors = data["neighbors"]
            st.markdown("🧑‍🎨 Here are your matches!")

            for i, match in enumerate(neighbors, start=1):
                st.markdown(f"---\n### 🖼️ Match #{i}")
                col1, col2 = st.columns([1, 2])

                with col1:
                    # 👤 Visage extrait local
                    face_path = match.get("painting_face_path")
                    if face_path and os.path.exists(face_path):
                        try:
                            with open(face_path, "rb") as img_file:
                                face_img = Image.open(img_file)
                                st.image(face_img, caption="👤 Extracted face", width=300)
                        except Exception as e:
                            st.warning(f"Erreur chargement visage : {e}")
                    else:
                        st.text("❌ Visage non disponible")

                    # 🎨 Tableau original local
                    painting_path = match.get("original_painting_path")
                    if painting_path and os.path.exists(painting_path):
                        try:
                            with open(painting_path, "rb") as img_file:
                                painting_img = Image.open(img_file)
                                st.image(painting_img, caption="🎨 Original painting", width=300)
                        except Exception as e:
                            st.warning(f"Erreur chargement peinture : {e}")
                    else:
                        st.text("❌ Tableau non disponible")

                    # 🌐 Image WikiArt directe
                    image_url = match.get("original_painting_image_url")
                    if image_url:
                        st.image(image_url, caption="🖼️ Depuis WikiArt", width=300)
                    else:
                        st.text("❌ Image WikiArt non trouvée")

                with col2:
                    st.markdown(f"**🎨 Titre :** *{match['original_painting_title']}*")
                    st.markdown(f"**👨‍🎨 Artiste :** {match['original_painting_artist']}")
                    st.markdown(f"[🔗 Voir sur WikiArt]({match['original_painting_wikiart_link']})")
                    st.write(f"📊 Similarité : {match['similarity']}")
