import streamlit as st
import pandas as pd
import os
import json
from google.oauth2.service_account import Credentials
import gspread

# Crear archivo JSON con las credenciales a partir del secreto
if not os.path.exists("credenciales.json"):
    creds_json = st.secrets["Credenciales"]
    with open("credenciales.json", "w") as f:
        json.dump(dict(creds_json), f)  # 👈 usar json.dump

# Conectarse a Google Sheets
credenciales = Credentials.from_service_account_file(
    'credenciales.json',
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
gc = gspread.authorize(credenciales)
sheet = gc.open("Respuestas Formulario").sheet1

st.title("📋 Formulario de Registro")

# Campos del formulario
nombre = st.text_input("Nombre completo")
edad = st.number_input("Edad", 0, 120)
correo = st.text_input("Correo electrónico")
comentario = st.text_area("Comentario")

if st.button("Enviar"):
    # Añadir fila a Google Sheets
    fila = [nombre, edad, correo, comentario]
    sheet.append_row(fila)

    st.success("✅ ¡Gracias por enviar tu respuesta!")
