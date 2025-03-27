import streamlit as st

st.set_page_config(page_title="Citations and Acknowledgments", layout="wide")

st.title("📚 Citations and Acknowledgments")

st.header("🧠 Models and Libraries Used")

st.subheader("🔍 DeepFace")
st.markdown("""
- Serengil, Sefik Ilkin and Ozpinar, Alper (2020).
  **LightFace: A Hybrid Deep Face Recognition Framework**.
  *2020 Innovations in Intelligent Systems and Applications Conference (ASYU)*, pp. 23–27.
  [DOI: 10.1109/ASYU50717.2020.9259802](https://ieeexplore.ieee.org/document/9259802)

- Serengil, Sefik Ilkin and Ozpinar, Alper (2024).
  **A Benchmark of Facial Recognition Pipelines and Co-Usability Performances of Modules**.
  *Bilisim Teknolojileri Dergisi*, vol. 17, no. 2, pp. 95–107.
  [DOI: 10.17671/gazibtd.1399077](https://dergipark.org.tr/en/pub/gazibtd/issue/84331/1399077)
""")

st.subheader("📦 YOLO – Ultralytics")
st.markdown("""
Jocher, Glenn · Chaurasia, Ayush · Qiu, Jing (2023).
**YOLO by Ultralytics**, version 8.0.0
[GitHub](https://github.com/ultralytics/ultralytics) — [Documentation](https://docs.ultralytics.com)
License: GPL-3.0
""")

st.header("🖼️ Datasets and Visual Sources")

st.markdown("""
- 🎨 **Kaggle - WikiArt Dataset**
  [https://www.kaggle.com/datasets/steubk/wikiart/data](https://www.kaggle.com/datasets/steubk/wikiart/data)

- 🖼️ **WikiArt**
  [https://www.wikiart.org/](https://www.wikiart.org/)

- 🏛️ **Images d’Art - RMN Grand Palais** *(public domain collections)*
  [https://www.images-art.fr/](https://www.images-art.fr/)

- 🌏 **Guimet National Museum of Asian Arts**
  [https://www.guimet.fr/](https://www.guimet.fr/)
""")

st.header("🙏 Acknowledgments")
st.markdown("""
We extend our sincere thanks to the researchers, developers, and institutions who make their tools, models, and artworks publicly available to support open and responsible innovation.

This project would not be possible without their work.
""")
