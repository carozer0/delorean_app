import streamlit as st

st.set_page_config(page_title="Ethique & Data / Ethics & Data", layout="wide")

st.title("🖼️ Une expérience éthique, artistique et inclusive / An Ethical, Artistic and Inclusive Experience")

# Ligne de séparation
st.markdown("---")

### 🇫🇷 SECTION FRANÇAISE

st.header("FR · Une approche éthique et transparente de la donnée")

# Déconstruire les biais
st.subheader("Déconstruire les biais, redonner place à la diversité")
st.markdown("""
Depuis des siècles, l’art occidental a imposé une vision unique de la beauté, centrée autour d’un idéal.
Ce regard dominant a longtemps laissé peu de place aux autres représentations, souvent reléguées à des rôles secondaires, exotiques ou stéréotypés.
""")

# Éthique
st.subheader("Une approche éthique et transparente")
st.markdown("""
L’expérience est pensée pour être fluide, mais surtout **responsable**.

- ✅ **Consentement explicite** : vous restez maître·sse de votre image.
- 🚫 **Zéro stockage** : votre photo est utilisée uniquement le temps de l’expérience, jamais conservée.
- 🔍 **Transparence totale** : vous savez comment et pourquoi votre image est utilisée.
- 🔐 **Sécurité** : l’application est hébergée via Streamlit, dans un environnement sécurisé.
- ❌ **Aucune catégorisation** : nous ne détectons ni genre, ni couleur de peau, ni origine.
  Il ne s’agit pas d’**identifier**, mais de **rapprocher visuellement**.
""")

# Dataset
st.subheader("Des données ouvertes, un dataset rééquilibré")
st.markdown("""
Pour entraîner notre modèle, nous nous appuyons sur des bases de données **publiques et accessibles**, issues de plateformes comme **Kaggle** ou de collections libres de droits, telles que **Images d’Art**.

🎯 L’objectif ? Construire un jeu de données **plus diversifié**, tout en respectant les droits d’auteur et les personnes représentées.

🧠 Nous utilisons le modèle **FairFace** uniquement pour **équilibrer** la représentation au sein du dataset, afin de garantir que **toutes les origines aient leur place** dans les œuvres proposées.
👉 Ce modèle **n’intervient jamais** dans la comparaison avec les visages utilisateurs.
""")

# Algorithme
st.subheader("Un algorithme au service de l’émotion, pas de la vérité")
st.markdown("""
La mise en relation entre votre image et une œuvre d’art repose sur un algorithme de **similarité visuelle** (_KNN_).

Il ne s’agit pas d’une science exacte, mais d’un **jeu d’échos** entre traits, textures et couleurs.
🎨 Une approche **poétique et intuitive** pour vous projeter dans l’histoire de l’art.
""")

# Ligne de séparation
st.markdown("---")

### E🇬🇧E ENGLISH SECTION

st.header("EN · An Ethical and Transparent Approach to Data")

# Unbias
st.subheader("Deconstructing Bias and Restoring Diversity")
st.markdown("""
For centuries, Western art has promoted a singular vision of beauty, centered around one ideal.
This dominant gaze has left little room for other representations, often relegated to secondary, exotic, or stereotyped roles.
""")

# Ethics
st.subheader("A Responsible and Transparent Experience")
st.markdown("""
This experience is designed to be seamless, but above all, **ethical**:

- ✅ **Explicit consent**: you remain in control of your image.
- 🚫 **Zero storage**: your photo is used only during the experience and never saved.
- 🔍 **Full transparency**: you know how and why your image is used.
- 🔐 **Secure environment**: the app is hosted via Streamlit in a safe infrastructure.
- ❌ **No categorization**: we do not detect gender, skin color, or origin.
  This is not about **identifying**, but about **visually connecting**.
""")

# Dataset
st.subheader("Open Data and a Rebalanced Dataset")
st.markdown("""
To train our model, we rely on **public and accessible datasets**, such as those from **Kaggle** or **public-domain collections** like *Images d’Art*.

🎯 Our goal? To build a **more diverse dataset** while respecting copyright and the individuals represented.

🧠 We use the **FairFace** model **only** to **balance representation** within the dataset and ensure that **all backgrounds are represented** in the artworks suggested.
👉 This model **is never used** to compare user faces.
""")

# Algorithm
st.subheader("An Algorithm in Service of Emotion, Not Truth")
st.markdown("""
The connection between your image and a work of art relies on a **visual similarity algorithm** (_KNN_).

It is not an exact science, but a **resonance** of features, textures, and colors.
🎨 A **poetic and intuitive** way to see yourself in art history.
""")
