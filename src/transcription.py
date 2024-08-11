import speech_recognition as sr

def transcribe():
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        print("Listening...")
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    try:
        return r.recognize_google(audio)    # recognize speech using Google Speech Recognition
    except LookupError:                            # speech is unintelligible
        return "Could not understand audio"

# test transcribe
# print(transcribe())