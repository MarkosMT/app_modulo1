import streamlit as st
from openai import OpenAI

# 1. Configuración de la página (Título e ícono)
st.set_page_config(page_title="Generador de IA", page_icon="🎨")

# 2. Título y diseño
st.title("🎨 Generador de Imágenes IA")
st.write("Escribe un texto y la Inteligencia Artificial creará la imagen.")

# 3. Input para la API Key (Para que sea seguro y no la pegues en el código)
api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")

# 4. Input del usuario (El Prompt)
prompt = st.text_area("¿Qué quieres imaginar hoy?", placeholder="Ej: Un paisaje futurista de neón...")

# 5. Botón y lógica
if st.button("Generar Imagen"):
    if not api_key:
        st.error("⚠️ Por favor ingresa tu API Key en la barra lateral.")
    elif not prompt:
        st.warning("⚠️ Por favor escribe una descripción.")
    else:
        try:
            # Conexión con OpenAI
            client = OpenAI(api_key=api_key)
            
            with st.spinner('La IA está pintando tu idea... 🖌️'):
                response = client.images.generate(
                    model="dall-e-3", # O dall-e-2 si quieres gastar menos
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                
                # Obtener la URL
                image_url = response.data[0].url
                
                # Mostrar la imagen
                st.image(image_url, caption=prompt, use_column_width=True)
                st.success("¡Imagen generada con éxito!")
                
        except Exception as e:
            st.error(f"Hubo un error: {e}")
