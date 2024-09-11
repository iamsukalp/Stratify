import streamlit as st
from st_audiorec import st_audiorec
from openai import OpenAI
import os

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def audionButtonComponent():

    if os.path.exists("audio.wav"):
        os.remove("audio.wav")

    if "audio_prompt" not in st.session_state:
        st.session_state.audio_prompt = None

    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        st.audio(wav_audio_data, format="audio/wav")
        with open("audio.wav", mode="bx") as f:
            f.write(wav_audio_data)

        audio_file = open("audio.wav", "rb")

        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=(audio_file),
        )

        print(transcript)

        st.session_state.audio_prompt = transcript.text
        st.rerun()
