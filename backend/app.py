from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import pandas as pd
import joblib
import os


from report_analyzer import analyze_report
from chatbot import medical_chat
from translator import translate_text



# =========================
# VOICE
# =========================

try:

    from voice_assistant import (
        speech_to_text,
        text_to_speech
    )

    VOICE_AVAILABLE = True


except Exception:

    VOICE_AVAILABLE = False






app = FastAPI(
    title="Medinova AI"
)





# =========================
# CORS
# =========================


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_methods=["*"],

    allow_headers=["*"]

)







# =========================
# TEMP USERS
# =========================


users = {}








# =========================
# MODEL LOAD
# =========================


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)



MODEL_PATH = os.path.join(

    BASE_DIR,

    "models",

    "disease_model.pkl"

)



DISEASE_ENCODER_PATH = os.path.join(

    BASE_DIR,

    "models",

    "disease_encoder.pkl"

)





model = joblib.load(

    MODEL_PATH

)



disease_encoder = joblib.load(

    DISEASE_ENCODER_PATH

)

FEATURE_ENCODER_PATH = os.path.join(

    BASE_DIR,

    "models",

    "feature_encoders.pkl"

)


feature_encoders = joblib.load(

    FEATURE_ENCODER_PATH

)


print("Feature encoders loaded")



print("Disease model loaded")

print("Disease encoder loaded")










# =========================
# SCHEMAS
# =========================


class Register(BaseModel):

    name:str

    email:str

    password:str






class Login(BaseModel):

    email:str

    password:str






class PredictionInput(BaseModel):


    Fever:str


    Cough:str


    Fatigue:str


    Difficulty_Breathing:str


    Age:int


    Gender:str


    Blood_Pressure:str


    Cholesterol_Level:str








class ChatRequest(BaseModel):

    message:str







# =========================
# HELPER
# =========================


def yes_no(value):


    if value.lower() == "yes":

        return 1


    return 0







# =========================
# HOME
# =========================


@app.get("/")


def home():


    return {


        "message":
        "Medinova AI Backend Running"


    }










# =========================
# REGISTER
# =========================


@app.post("/register")


def register(data:Register):


    users[data.email] = {


        "name":
        data.name,


        "password":
        data.password


    }



    return {


        "message":
        "Registration successful"


    }










# =========================
# LOGIN
# =========================


@app.post("/login")


def login(data:Login):


    user = users.get(

        data.email

    )



    if not user:


        return {


            "error":
            "User not found"


        }




    if user["password"] != data.password:


        return {


            "error":
            "Wrong password"


        }




    return {


        "message":
        "Login successful",


        "name":
        user["name"]


    }









# =========================
# DISEASE PREDICTION
# =========================

@app.post("/predict")


def predict(data:PredictionInput):


    try:


        input_data = {


            "Fever":
            yes_no(data.Fever),


            "Cough":
            yes_no(data.Cough),


            "Fatigue":
            yes_no(data.Fatigue),


            "Difficulty Breathing":
            yes_no(data.Difficulty_Breathing),


            "Age":
            data.Age,


            "Gender":
            data.Gender,


            "Blood Pressure":
            data.Blood_Pressure,


            "Cholesterol Level":
            data.Cholesterol_Level,


            "Outcome Variable":
            0

        }




        df = pd.DataFrame([input_data])




        # apply saved encoders

        for column, encoder in feature_encoders.items():


            if column in df.columns:


                try:


                    df[column] = encoder.transform(

                        df[column]

                    )


                except Exception as e:


                    print(

                        "Encoder skipped:",

                        column,

                        e

                    )





        print("FINAL MODEL INPUT")

        print(df)




        result = model.predict(df)




        print(

            "MODEL OUTPUT:",

            result

        )





        disease = disease_encoder.inverse_transform(

            result

        )[0]





        return {


            "prediction":

            disease


        }







    except Exception as e:


        print(

            "Prediction error:",

            e

        )


        return {


            "error":

            "Prediction service unavailable"


        }









# =========================
# REPORT ANALYZER
# =========================


@app.post("/report")


async def report(file:UploadFile=File(...)):


    path="report.pdf"



    with open(path,"wb") as f:


        f.write(

            await file.read()

        )



    result = analyze_report(path)



    return result










# =========================
# CHAT AI
# =========================


@app.post("/chat")


def chat(data:ChatRequest):


    try:


        answer = medical_chat(

            data.message

        )



        return {


            "response":

            answer


        }




    except Exception as e:


        print(e)



        return {


            "response":

            "AI service unavailable"


        }









# =========================
# VOICE AI
# =========================


@app.get("/voice")


def voice():


    if not VOICE_AVAILABLE:


        return {


            "error":

            "Voice service unavailable"


        }




    question, lang = speech_to_text()



    answer = medical_chat(

        question

    )




    if lang != "en":


        answer = translate_text(

            answer,

            lang

        )





    text_to_speech(

        answer

    )





    return {


        "question":

        question,



        "answer":

        answer


    }