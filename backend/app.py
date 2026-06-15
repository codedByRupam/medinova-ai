from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import pandas as pd
import joblib
import os


from report_analyzer import analyze_report
from chatbot import medical_chat
from translator import translate_text



# voice import safely
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


ENCODER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "feature_encoders.pkl"
)



model = joblib.load(
    MODEL_PATH
)



encoders = joblib.load(
    ENCODER_PATH
)



print("Model loaded")
print("Encoder loaded")





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

    Fever:int

    Cough:int

    Fatigue:int

    Difficulty_Breathing:int

    Age:int

    Gender:int

    Blood_Pressure:int

    Cholesterol_Level:int

    Outcome_Variable:int





class ChatRequest(BaseModel):

    message:str







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


    users[data.email]={

        "name":data.name,

        "password":data.password

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


        df = pd.DataFrame([{

            "Fever":data.Fever,

            "Cough":data.Cough,

            "Fatigue":data.Fatigue,

            "Difficulty Breathing":
            data.Difficulty_Breathing,

            "Age":data.Age,

            "Gender":data.Gender,

            "Blood Pressure":
            data.Blood_Pressure,

            "Cholesterol Level":
            data.Cholesterol_Level,

            "Outcome Variable":
            data.Outcome_Variable

        }])



        result = model.predict(df)



        print(
            "MODEL OUTPUT:",
            result
        )



        encoder = None



        if isinstance(encoders, dict):


            for key,value in encoders.items():


                if hasattr(value,"inverse_transform"):


                    encoder=value

                    print(
                        "Using encoder:",
                        key
                    )

                    break




        if encoder:


            try:


                disease = encoder.inverse_transform(
                    result
                )[0]



            except Exception as e:


                print(
                    "Encoder error:",
                    e
                )


                disease = "Unknown disease"




        else:


            disease = str(
                result[0]
            )





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



    analysis = analyze_report(path)



    return analysis










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




    question,lang = speech_to_text()



    answer = medical_chat(
        question
    )




    if lang!="en":


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