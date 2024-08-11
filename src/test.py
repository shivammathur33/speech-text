# import speech_recognition as sr
# import pyttsx3
# import time

# # Initialize the recognizer 
# r = sr.Recognizer() 

# # Function to convert text to
# # speech
# def SpeakText(command):
    
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command) 
#     engine.runAndWait()
    
    
# with sr.Microphone() as source2:
#     # wait for a second to let the recognizer
#     # adjust the energy threshold based on
#     # the surrounding noise level 
#     print(time.ctime())
#     r.adjust_for_ambient_noise(source2, duration=0.2)
#     print(time.ctime())
    
#     #listens for the user's input 
#     audio2 = r.listen(source2)
    
#     # Using google to recognize audio
#     MyText = r.recognize_google(audio2)
#     MyText = MyText.lower()

#     print(MyText)
#     # SpeakText(MyText)

import speech_recognition as sr
import ollama

# print(ollama.generate(model='llama2', prompt='What is the capital of France?'))

# r = sr.Recognizer()
# with sr.Microphone() as source:                # use the default microphone as the audio source
#     audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

# try:
#     print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
# except LookupError:                            # speech is unintelligible
#     print("Could not understand audio")

# ollama.generate(model='llama3.1', prompt='Why is the sky blue?')

            