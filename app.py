import streamlit as st
import numpy as np
import matplotlib.pyplot as plt 

# Konfigurasi tema Streamlit
st.set_page_config(
    page_title="Kalkulator Sederhana",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Tampilan judul
st.title("Kalkulator Sederhana dan Grafik Teorema Limit Sentral")

#sidebar
with st.sidebar:
    tipe = st.radio('pilih tipe',['Kalkulator Sederhana','Grafik Teorema Limit Sentral'])
if tipe == 'Kalkulator Sederhana':
    #masukkan angka pertama
    num1 = st.number_input("Masukkan Angka Pertama", value=0.0)
    # Pilihan operasi
    operation = st.selectbox("Operasi", ["+", "-", "*", "/"])
    # Masukan angka kedua
    num2 = st.number_input("Masukkan Angka Kedua", value=0.0)

# Tombol hitung
    if st.button("Hitung"):
      if operation == "+":
        result = num1 + num2
      elif operation == "-":
        result = num1 - num2
      elif operation == "*":
        result = num1 * num2
      elif operation == "/":
        if num2 != 0:
          result = num1 / num2
        else:
          result = "Tidak dapat dibagi oleh 0"
      st.success(f"Hasil: {result}")

elif tipe == 'Grafik Teorema Limit Sentral':
   perc_heads = st.number_input(label='Kemungkinan berhasil', min_value=0.0, max_value=1.0, value=.5) 
   binom_dist = np.random.binomial(1, perc_heads, 1000) 

 

list_of_means = [] 
for i in range(0, 1000): 
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean()) 

 

fig, ax = plt.subplots() 
ax = plt.hist(list_of_means) 
st.pyplot(fig) 