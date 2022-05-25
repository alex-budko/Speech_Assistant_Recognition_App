import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import os # to remove created audio files

from time import ctime

r = sr.Recognizer()

# record audio function
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data

# Alex speaking function
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(audio_string) # print what app said
    os.remove(audio_file) # remove audio file

# respond function with find location and url query
def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Alex')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'how are you' in voice_data:
        speak('I am doing great')
    # search query
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    # find location query
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        # finds address of the location
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

#initial speaking
time.sleep(1)
speak('How can I help you?')

#respond to each search query
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond