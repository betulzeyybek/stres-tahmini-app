import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Modeli yükle
model = joblib.load("model.pkl")

st.set_page_config(page_title="Stres Tahmin Uygulaması", layout="centered")
st.title("🧠 Stres Tahmin Uygulaması")
st.markdown("Bu uygulama, öğrencilerin bazı özelliklerine göre stres seviyesini tahmin eder.")

# Girişler
stud_h = st.slider("Haftalık ders çalışma saati", 0, 80, 10)
jspe = st.slider("Empati skoru (jspe)", 0.0, 5.0, 2.5)
qcae_cog = st.slider("Bilişsel empati (qcae_cog)", 0.0, 5.0, 2.5)
qcae_aff = st.slider("Duygusal empati (qcae_aff)", 0.0, 5.0, 2.5)
mbi_ex = st.slider("Tükenmişlik (mbi_ex)", 0.0, 5.0, 2.5)
mbi_ea = st.slider("Kişisel başarı algısı (mbi_ea)", 0.0, 5.0, 2.5)

# Tahmin butonu
if st.button("Stres Seviyesini Tahmin Et"):
    # Özellikleri doğru sırayla ve doğru isimle veriyoruz
    input_data = pd.DataFrame([[
        stud_h, jspe, qcae_cog, qcae_aff, mbi_ex, mbi_ea
    ]], columns=['stud_h', 'jspe', 'qcae_cog', 'qcae_aff', 'mbi_ex', 'mbi_ea'])

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("Tahmin: Düşük-Orta Stres 😌")
    else:
        st.error("Tahmin: Yüksek Stres 😮")
