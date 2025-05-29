import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv 
import os 

load_dotenv()
key = os.getenv("API_KEY") 
print(key)

client = OpenAI(api_key= key)
error= False 

try: 
    client.models.list()
except Exception as e: 
    error= True


def get_response(text): 
    prompt = f"""
    A partir del texto que te entrega el usuario da respuesta siguiendo el metodod CoT 
    aqui esta el texto del usuario: 
    \"\"\"{text}\"\"\"

    """
    chatBot = client.chat.completions.create(
        model="gpt-4.1-mini", 
        messages=[
            {"role": "system", "content": "You are an expert in child nutrition "},
            {"role": "user", "content": prompt}
        ]
    )
    response_chat_bot= chatBot.choices[0].message.content.strip()
    return response_chat_bot

st.image("Logo-ces.png", width=300)
st.title("ChatBot Institucional")

if(error): 
    st.image("a.png")
    st.markdown("Estoy fuera de servicio")
    st.stop()
else: 
    st.markdown("##### Hola, soy tu asistente personal")
    st.markdown("¿En que puedo ayudarte?")

    user_input= st.text_input("Escribe tu consulta", key="input_user")
    if st.button("Enviar") and user_input: 
        st.write(f"** yo ** {user_input}")
        try:
            response_gpt= get_response(user_input)
            st.write(f"**Bot:** {response_gpt}")
        except Exception as e: 
            st.error(str(e))

