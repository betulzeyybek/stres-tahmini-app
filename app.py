import streamlit as st
import pandas as pd
import joblib

# Modeli yükle
model = joblib.load("model.pkl")

# Özellik isimleri (modelin eğitildiği sırayla)
feature_names = ['stud_h', 'jspe', 'qcae_cog', 'qcae_aff', 'mbi_ex', 'mbi_ea']

st.set_page_config(page_title="Stres Tahmin Uygulaması", layout="centered")
st.title("🧠 Stres Tahmin Uygulaması")
st.markdown("Bu uygulama, öğrencilerin bazı özelliklerine göre stres seviyesini tahmin eder.")

# Girişler
inputs = {}
inputs['stud_h'] = st.slider("Haftalık ders çalışma saati", 0, 80, 10)
inputs['jspe'] = st.slider("Empati skoru (jspe)", 0.0, 5.0, 2.5)
inputs['qcae_cog'] = st.slider("Bilişsel empati (qcae_cog)", 0.0, 5.0, 2.5)
inputs['qcae_aff'] = st.slider("Duygusal empati (qcae_aff)", 0.0, 5.0, 2.5)
inputs['mbi_ex'] = st.slider("Tükenmişlik (mbi_ex)", 0.0, 5.0, 2.5)
inputs['mbi_ea'] = st.slider("Kişisel başarı algısı (mbi_ea)", 0.0, 5.0, 2.5)

# Tahmin butonu
if st.button("Stres Seviyesini Tahmin Et"):
    input_df = pd.DataFrame([inputs])[feature_names]
    input_df.columns = input_df.columns.astype(str)  # XGBoost hata engelleme

    prediction = model.predict(input_df)[0]

    if prediction == 0:
        st.success("Tahmin: Düşük-Orta Stres 😌")
    else:
        st.error("Tahmin: Yüksek Stres 😮")
