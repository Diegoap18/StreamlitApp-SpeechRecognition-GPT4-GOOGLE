'''
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
this script is to relate api open ai and the application streamlit
the proposal is be a middlewere between the open ai and application.
the calls is been done here and use the apikey generate to work.

if you no have api key the same will not work to create one please go to:
https://platform.openai.com/
and provide your api key.

Author Diego A Pereira.
'''

import openai
import os
import unidecode


def transcript_gpt(audio,key):
    '''This function is responsible to call the module whisper on openai
    and transcribe the audio and return the text'''
    audio_file = audio
    openai.api_key = key
    
    audio_f = open(audio_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_f)
    text = transcript.text

    with open('gpt_transcricao.txt', 'w') as f:
               f.writelines(text)
               print("transcript: {}".format(text))
           
    return text
    
def chatgpt_contexto(text,key):
    '''This function is responsible to call the module "text-davinci-003" on openai
    and return the text trasbribed with a context o text.'''
      
    openai.api_key = key
    texto = text
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="what is the context of the following text ? {}".format(texto),
    temperature=0,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    resposta = response["choices"][0]["text"]
    
    with open('contexto_gpt.txt', 'w') as f:
             f.writelines(resposta)
             print("response from text: {}".format(resposta))
               
def chatgpt_resumo(text,key):
    '''This function is responsible to call the module "text-davinci-003" on openai
    and return the text trasbribed with a context o text.'''
    
    openai.api_key = key
    texto = text
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="generate a summary of the following text ? {}".format(texto),
    temperature=0,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    resumo = response["choices"][0]["text"]
    
    with open('resumo_gpt.txt', 'w') as f:
             f.writelines(resumo)
             print("response from text: {}".format(resumo))   
             
if __name__ == "__main__":
    audio = 'insert the audio path here/audio.wav' #only if run this script for api use the streamlit frontend.
    key = 'insert your apikey here' #only if run this script for api use the streamlit frontend.
    texto = transcript_gpt(audio,key)
    chatgpt_contexto(texto,key)
    chatgpt_resumo(texto,key)