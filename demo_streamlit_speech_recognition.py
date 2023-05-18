'''
this is the main code here we have the structure of streamlit and the calls for apis
google and chatGPT4 the objective is make a compare between chatgpt and google speech analytics free.

to use api chatgpt you have some free credits i use this credits to build this application
you may need the same for it go to https://platform.openai.com/ and create your account.
for google just install the requirements for google speech_recognition and will work.

thanks by share my content just credit this content in future

Author  Diego A Pereira.
'''

import streamlit as st
import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import re
from frequencia_highlights_text import highlight_important_words
from frequencia_highlights_text import text_highlights
from frequencia_highlights_text import text_highlights_html
from tma_silence import silence_calculation
from tma_silence import calculation_tma_silence
from gptranscribe import *


def transcribe_audio(file):
    ''' this function is responsible to make the transcription audio we have
     google here making the transcriptions.'''
     
    # selectiong the recognizer
    r = sr.Recognizer()
    
    with sr.AudioFile(file) as source:
        audio = r.record(source)  # reading the audio

    # trying recognize the api Google Speech Recognition
    try:
        print('Google Speech Recognition: ' + r.recognize_google(audio, language='pt-BR'))# change for English for work if is not a portuguese your natural language
        texto = r.recognize_google(audio, language='pt-BR') # change for English for work if is not a portuguese your natural language
    except sr.UnknownValueError:
        print('Google Speech Recognition NÃO ENTENDEU o audio')
        texto = ''
    except sr.RequestError as e:
        print('Erro ao solicitar resultados do serviço Google Speech Recognition; {0}'.format(e))
        texto = ''
    return texto    


if  "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def callback():
    '''this function to a callback to session on streamlit'''
    st.session_state.button_clicked = True

def main():
    ''' this is a main code responsible to call all functions and build the streamlit body'''
    st.set_page_config(page_title="Speech to Text App", page_icon=":microphone:", layout="wide")
    st.title("Speech to Text")

    key_gpt = st.text_input("Please Insert the ChatGPT-3 Key to Start.")
    print(key_gpt)
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
    if audio_file is not None:
        st.text("Audio pronto para iniciar a transcrição.")
        st.audio(audio_file, start_time=0)       
               
        button_clicked = st.button("transcrever", key="transcrever", on_click=callback)
        if button_clicked:            
            with st.spinner('Realizando a transcrição'):
                
                try:
                    print("Transcribe GPT")
                    texto_retorno = transcript_gpt(audio_file.name,key_gpt)
                    chatgpt_contexto(texto_retorno,key_gpt)
                    chatgpt_resumo(texto_retorno,key_gpt)
                    print("Transcribe GPT completed")
                except:
                    st.write("Por favor verifique a Key ou o audio")
                    print("Por favor verifique a Key ou o audio")
                
                print("Transcribe Google")
                text = transcribe_audio(audio_file)
                print("Transcribe Google completed")
            
            m_silence = silence_calculation(audio_file.name)
            tma_total, silence_total = calculation_tma_silence(audio_file.name, m_silence)
            st.subheader(" ")
            st.subheader("TMA e Tempo de Silêncio 🕓")
            col1, col2 = st.columns(2)
            col1.metric("TMA 🚩 ", tma_total)
            col2.metric("Tempo De Silêncio ⚡", silence_total)
            st.subheader(" ")    
            
            col3, col4 = st.columns(2)

            with col3:
                st.subheader("Transcrição GoogleCloud📃")
                with st.expander("Transcrição"):
                    texto_Final = text_highlights(text)
                    st.markdown("{}".format(texto_Final), unsafe_allow_html=False)
                    important_words = highlight_important_words(text)
                    st.write("Palavras com:(maior frequencia):", important_words)
            with col4:
               st.subheader("Transcrição ChatGPT-3 📃")
               with st.expander("Transcrição"):
                    with open('gpt_transcricao.txt') as f:
                              texto = f.read()
                    texto_Final = text_highlights_html(str(texto))
                    st.markdown("<p>{}</p>".format(texto), unsafe_allow_html=True)
                    important_words = highlight_important_words(str(texto))
                    st.write("Palavras com:(maior frequencia):", important_words)
                    
            col5, col6 = st.columns(2)
            
            with col5:
                st.subheader("Resumo da Ligação GPT-3")
                with st.expander("Resumo:"):
                    with open('resumo_gpt.txt', encoding='latin-1') as f:
                              texto = f.read()
                    texto_Final = text_highlights_html(str(texto))
                    st.markdown("<p>{}</p>".format(texto), unsafe_allow_html=True)
                    important_words = highlight_important_words(str(texto))
                    st.write("Palavras em Destaque:", important_words)
                    
            with col6:
               st.subheader("Contexto da Ligação GPT-3")
               with st.expander("Contexto"):
                    with open('contexto_gpt.txt', encoding='latin-1') as f:
                              texto = f.read()
                    texto_Final = text_highlights_html(str(texto))
                    st.markdown("<p>{}</p>".format(texto), unsafe_allow_html=True)
                    important_words = highlight_important_words(str(texto))
                    st.write("Palavras em Destaque:", important_words)
   
if __name__ == "__main__":
    main()