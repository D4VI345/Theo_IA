# Our main file.

import speech_recognition as sr 

# Cria um reconhecedor
r = sr.Recognizer()

# Abrir o microfone
with sr.Microphone() as source:
    while True: 
         audio = r.listen(source) # Define microfone como fonte de audio

         print(r.recognizer_google(audio, language='pt'))
    