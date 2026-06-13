import speech_recognition as sr
#import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
from langdetect import detect
from deep_translator import GoogleTranslator
import os



# =========================
# RECORD VOICE
# =========================


def record_audio():


    duration = 5

    sample_rate = 16000


    print("Listening...")



    recording = sd.rec(

        int(duration * sample_rate),

        samplerate=sample_rate,

        channels=1,

        dtype="int16"

    )



    sd.wait()



    filename = "voice_input.wav"



    write(

        filename,

        sample_rate,

        recording

    )


    return filename






# =========================
# SPEECH TO TEXT
# =========================


def speech_to_text():


    try:


        file = record_audio()



        recognizer = sr.Recognizer()



        with sr.AudioFile(file) as source:


            audio = recognizer.record(source)




        text = recognizer.recognize_google(

            audio

        )



        try:


            language = detect(text)


        except:


            language = "en"





        print(
            "Detected:",
            language
        )


        print(
            "User:",
            text
        )



        return text, language




    except Exception as e:


        print(

            "Speech Error:",

            e

        )


        return (

            "Unable to understand",

            "en"

        )







# =========================
# TRANSLATION
# =========================


def translate_text(text, target):


    try:


        if target == "en":

            return text



        translated = GoogleTranslator(

            source="auto",

            target=target

        ).translate(text)



        return translated



    except Exception as e:


        print(

            "Translation Error:",

            e

        )



        return text







# =========================
# TEXT TO SPEECH
# =========================


def text_to_speech(text):


    try:


        engine = pyttsx3.init()



        engine.setProperty(

            "rate",

            150

        )



        engine.say(

            text

        )



        engine.runAndWait()



        engine.stop()



    except Exception as e:


        print(

            "TTS Error:",

            e

        )






# =========================
# CLEAN OLD AUDIO FILE
# =========================


def cleanup_audio():


    try:


        if os.path.exists("voice_input.wav"):


            os.remove(
                "voice_input.wav"
            )


    except:


        pass