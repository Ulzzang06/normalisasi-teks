import streamlit as st
from streamlit_lottie import st_lottie
import json
import time

# --- Fungsi untuk load file Lottie dan Kamus ---
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_kamus(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# --- Fungsi Normalisasi ---
def normalisasi_teks(teks, kamus):
    kata_list = teks.lower().split()
    hasil = [kamus.get(kata, kata) for kata in kata_list]
    return " ".join(hasil)

# --- Load animasi ---
lottie_header = load_lottiefile("rocket_header.json")  # animasi atas
lottie_rocket = load_lottiefile("rocket.json")         # animasi saat proses

# --- Load kamus ---
kamus_alay = load_kamus("kamus.json")  # GUNAKAN FILE kamus.json

# --- Ganti background menjadi putih bersih ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #FFFFFF;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Tampilkan animasi header di atas judul ---
st_lottie(lottie_header, speed=1, height=150, loop=True)

# --- Judul aplikasi ---
st.markdown("<h1 style='text-align: center;'>🚀 Normalisasi Teks Tidak Baku Bahasa Indonesia 🚀</h1>", unsafe_allow_html=True)

# --- Input teks tidak baku ---
input_text = st.text_area("Masukkan teks tidak baku:")

# --- Opsi spellcheck ---
spellcheck = st.checkbox("Gunakan spellcheck (opsional)")

# --- Tombol proses normalisasi ---
if st.button("Proses Normalisasi"):
    with st.spinner("Menjalankan roket..."):
        st_lottie(lottie_rocket, speed=1, height=300)
        time.sleep(3)
        
    # --- Jalankan normalisasi dengan kamus ---
    hasil_normalisasi = normalisasi_teks(input_text, kamus_alay)

    # --- Tampilkan hasil dalam kotak keren ---
    st.success("✅ Hasil normalisasi:\n\n" + hasil_normalisasi)
