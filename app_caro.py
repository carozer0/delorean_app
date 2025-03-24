import os
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(layout="wide")
st.title("🎨 DeLorean Art Program ")

# Détection de l’URL d'API
if 'API_URI' in os.environ:
    BASE_URI = st.secrets[os.environ.get('API_URI')]
else:
    BASE_URI = st.secrets['cloud_api_uri']

BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
url = BASE_URI + 'upload_image'

uploaded_file = st.file_uploader("Who’s ready to hop in the DeLorean?", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Ready for time travel", width=300)

    if st.button("🔍 Fire up the DeLorean! ⚡🕒🚗"):
        with st.spinner("The flux capacitor is fluxing..."):
            files = {"img": uploaded_file.getvalue()}
            response = requests.post(url, files={"img": files["img"]})

        if response.status_code == 200:
            data = response.json()
            st.success("Great Scott!")

            neighbors = data["neighbors"]
            input_coords = data.get("input_photo_coordinates", [])
            cropped_input_face = None

            # 🧠 Extraire le visage croppé de la photo utilisateur
            if input_coords and len(input_coords) == 4:
                x1, y1, x2, y2 = input_coords
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(image.width, x2), min(image.height, y2)

                if x2 > x1 and y2 > y1:
                    cropped_input_face = image.crop((x1, y1, x2, y2))

            st.markdown("🧑‍🎨 Here are your matches!")

            for i, match in enumerate(neighbors, start=1):
                st.markdown(f"---\n### 🖼️ Match #{i}")
                col1, col2 = st.columns([1, 2])

                with col1:
                    image_url = match.get("original_painting_image_url")
                    face_data = match.get("face_coordinates", [])

                    if image_url and face_data:
                        try:
                            x1, y1, x2, y2, w_img, h_img = face_data[0]

                            response_img = requests.get(image_url)
                            full_img = Image.open(BytesIO(response_img.content)).convert("RGB")

                            resized_img = full_img.resize((w_img, h_img))

                            x1 = max(0, min(x1, w_img))
                            x2 = max(0, min(x2, w_img))
                            y1 = max(0, min(y1, h_img))
                            y2 = max(0, min(y2, h_img))

                            if x2 > x1 and y2 > y1:
                                cropped_face = resized_img.crop((x1, y1, x2, y2))
                                st.image(cropped_face, caption="🎨 Face from painting", width=300)
                            else:
                                st.warning("⚠️ Coordonnées invalides après clamp")

                            st.image(resized_img, caption="🖼️ Original painting (resized)", width=300)

                        except Exception as e:
                            st.warning(f"Erreur image WikiArt : {e}")

                    else:
                        # 🗂️ Cas local
                        face_path = match.get("painting_face_path")
                        painting_path = match.get("original_painting_path")

                        if face_path and os.path.exists(face_path):
                            try:
                                with open(face_path, "rb") as f:
                                    face_img = Image.open(f)
                                    st.image(face_img, caption="🎨 Face from painting (local)", width=300)
                            except Exception as e:
                                st.warning(f"Erreur chargement visage local : {e}")

                        if painting_path and os.path.exists(painting_path):
                            try:
                                with open(painting_path, "rb") as f:
                                    painting_img = Image.open(f)
                                    st.image(painting_img, caption="🖼️ Original painting (local)", width=300)
                            except Exception as e:
                                st.warning(f"Erreur chargement peinture locale : {e}")

                    # 🧍‍♂️ Visage de la photo de départ
                    if cropped_input_face:
                        st.image(cropped_input_face, caption="👤 Your face (input)", width=300)

                with col2:
                    st.markdown(f"**🎨 Titre :** *{match['original_painting_title']}*")
                    st.markdown(f"**👨‍🎨 Artiste :** {match['original_painting_artist']}")
                    if match.get("original_painting_wikiart_link"):
                        st.markdown(f"[🔗 Voir sur WikiArt]({match['original_painting_wikiart_link']})")
                    st.write(f"📊 Similarité : {match['similarity']}")
