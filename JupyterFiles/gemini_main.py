import streamlit as st
from streamlit_option_menu import option_menu
import os
from gemini_utility import load_gemini_pro_model
working_directory = os.path.dirname(os.path.abspath(__file__))
st.set_page_config(
    page_title="Gemini AI",
    #page_icon= "🧠"
    layout="centered"
)
with st.sidebar:
    selected = option_menu("Gemini AI",
                          ["ChatBot",
                           "image Captioning",
                           "Embed text",
                           "Ask me anything"],
                           menu_icon='robot', icons=['chat-dots-fill','image-fill', 'textarea-t', 'patch-question-fill'],
                           default_index=0)

def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return user_role
    
if selected=="Chatbot":
    model = load_gemini_pro_model()
    
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])
        
    st.title("ChatBot")
    
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)
            
            
    user_prompt= st.chat_input("Ask gemini-pro") 

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        
        gemini_response = st.session_state.chat_session.send_message(user_prompt)           
        
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)