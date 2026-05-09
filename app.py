import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Esto busca el archivo .env y carga la llave
load_dotenv()
llave = os.getenv("GROQ_API_KEY")

st.title("⚡ Mi Asistente Seguro")

# Ahora la llave no está escrita en el código, se jala del archivo oculto
client = Groq(api_key=llave)
pregunta = st.text_input("Haz tu pregunta:")

if pregunta:
    try:
        # Usamos Llama 3, que es excelente y vuela
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": pregunta}
            ],
            model="llama-3.3-70b-versatile",
        )
        
        st.success("¡Respuesta de Llama 3 vía Groq!")
        st.write(chat_completion.choices[0].message.content)
        
    except Exception as e:
        st.error(f"Error: {e}")
