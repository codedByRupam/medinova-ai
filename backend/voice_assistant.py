from langdetect import detect
from deep_translator import GoogleTranslator


# =========================
# DETECT LANGUAGE
# =========================

def detect_language(text):

    try:
        return detect(text)

    except Exception:

        return "en"



# =========================
# TRANSLATION
# =========================

def translate_text(text, target="en"):

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
# VOICE RESPONSE
# =========================

def process_voice_text(text):


    language = detect_language(text)



    if language.startswith("hi"):


        response = translate_text(
            text,
            "en"
        )


        return {

            "original_text": text,

            "detected_language": "Hindi",

            "translated_text": response

        }



    else:


        return {


            "original_text": text,

            "detected_language": "English",

            "translated_text": text

        }





# =========================
# AI VOICE ASSISTANT REPLY
# =========================


def voice_assistant_reply(message):


    data = process_voice_text(message)



    reply = f"""

Hello, I am Medinova AI healthcare assistant.

You asked:

{data['translated_text']}

I can help you with health information,
disease prediction and medical reports.

"""


    return {


        "reply": reply,

        "language": data["detected_language"]

    }