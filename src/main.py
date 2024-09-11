import streamlit as st
from audioButtonComponent import audionButtonComponent
from messageComponent import messageComponent
from sideBarComponent import sideBarComponent

audio_prompt = None
user_query = None

sideBarComponent()


@st.dialog("Dictate")
def audioRecorder():

    with st.container(height=250):
        audionButtonComponent()


# Initialise session state to store conversation history locally to display on UI
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title(":brain: Stratify")


if "audio_prompt" in st.session_state:
    audio_prompt = st.session_state.audio_prompt


chat_container = st.container(border=True, height=450)
text_input, audio_input = st.columns([0.91, 0.09], gap="medium")

with text_input:
    user_query = st.chat_input("Ask me a question")

with audio_input:
    if st.button("🎙️", help="Record audio"):
        audioRecorder()


# Textbox and streaming process
if user_query or audio_prompt:
    with chat_container:
        messageComponent(user_query or audio_prompt)
