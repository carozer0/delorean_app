import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# 🌌 Style
st.markdown(
    """
    <style>
    .stAppx {
        background-color:  #173679 ;
    }
    .stTitle {
        background-color:  #ACB1D6 ;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎨 En-tête
col1, col2 = st.columns([1, 1])

with col1:
    st.title("DeLorean Art 🎨")
    st.markdown("#### Dive into history and discover yourself in its artistic works.")

with col2:
    image = Image.open("img/DeloreanV.jpg")
    st.image(image, use_container_width=True)

BASE_URI = st.secrets.get('local_api_uri')  # ou cloud_api_uri
BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
url = BASE_URI + 'upload_image'

# 📤 Upload
uploaded_file = st.file_uploader("Who's ready to hop in the DeLorean?", type=["jpg", "jpeg", "png", "jfif"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Ready for time travel", width=300)

    category = st.selectbox("Select Category :", (
        "full", "modern_abstract", "diverse", "cubism",
        "art_asiatique", "realism_impressionism", "renaissance_baroque",
        "romanticism_art_nouveau", "styles_recents"
    ),index=0)

    matches = st.selectbox("Pick matches :", ("3", "5", "10"),index=2)
    model = st.selectbox("Pick Model :", ("512", "ghost"),index=0)

    if st.button("🔍 Fire up the DeLorean! ⚡🕒🚗"):
        with st.spinner("The flux capacitor is fluxing..."):
            files = {"img": uploaded_file.getvalue()}
            response = requests.post(
                url,
                files={"img": files["img"]},
                data={"matches": matches, "model": model, "category": category}
            )

        if response.status_code == 200:
            data = response.json()
            st.success("Great Scott! Nom de Zeus!")

            neighbors = data["neighbors"]
            input_coords = data.get("input_photo_coordinates", [])
            cropped_input_face = None

            # 🧠 Crop visage utilisateur
            if input_coords and len(input_coords) == 4:
                x1, y1, x2, y2 = map(int, input_coords)
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(image.width, x2), min(image.height, y2)

                if x2 > x1 and y2 > y1:
                    cropped_input_face = image.crop((x1, y1, x2, y2))

            st.markdown("🧑‍🎨 Here are your matches!")

            for i, match in enumerate(neighbors, start=1):
                st.markdown(f"---\n### 🖼️ Match #{i}")
                col1, col2, col3 = st.columns([1, 1, 2])

                with col1:
                    face_data = match.get("face_coordinates", [])
                    image_url = match.get("original_painting_image_url")

                    if image_url:
                        try:
                            response_img = requests.get(image_url, timeout=5)

                            if response_img.status_code == 200:
                                full_img = Image.open(BytesIO(response_img.content)).convert("RGB")
                                st.image(full_img, caption="🖼️ Full painting", use_container_width=True)

                                # Si coordonnées de visage disponibles
                                if face_data:
                                    try:
                                        x1, y1, x2, y2, w_img, h_img = map(int, face_data[0])
                                        resized_img = full_img.resize((w_img, h_img), Image.Resampling.LANCZOS)

                                        x1 = max(0, min(x1, w_img))
                                        x2 = max(0, min(x2, w_img))
                                        y1 = max(0, min(y1, h_img))
                                        y2 = max(0, min(y2, h_img))

                                        if x2 > x1 and y2 > y1:
                                            cropped_face = resized_img.crop((x1, y1, x2, y2))
                                            st.image(cropped_face, caption="🎨 Face from painting")
                                        else:
                                            st.warning("⚠️ Coordonnées invalides après clamp")
                                    except Exception as e:
                                        st.warning(f"Erreur découpe visage : {e}")
                            else:
                                st.warning(f"⚠️ Image introuvable (code {response_img.status_code})")
                        except Exception as e:
                            st.warning(f"Erreur image WikiArt : {e}")

                with col2:
                    if cropped_input_face:
                        st.image(cropped_input_face, caption="👤 Your face (input)")

                with col3:
                    st.markdown(f"**🎨 Titre :** *{match['original_painting_title']}*")
                    st.markdown(f"**👨‍🎨 Artiste :** {match['original_painting_artist']}")

                    wikiart_link = match.get("original_painting_wikiart_link")
                    if wikiart_link:
                        try:
                            response = requests.head(wikiart_link, timeout=5)
                            if response.status_code == 200:
                                st.markdown(f"[🔗 Voir sur WikiArt]({wikiart_link})")
                        except requests.RequestException:
                            pass  # Ne rien afficher si le lien ne fonctionne pas ou plante

                    st.write(f"📊 Distance : {match['similarity']}")
        else:
            st.error("❌ Erreur lors de la communication avec l’API.")
