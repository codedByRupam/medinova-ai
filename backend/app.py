from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import pandas as pd
import joblib


from report_analyzer import (
    extract_text,
    analyze_report
)

from voice_assistant import (
    speech_to_text,
    text_to_speech
)


from chatbot import medical_chat


from translator import translate_text




app = FastAPI(
    title="Netravaan AI"
)



app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_methods=["*"],

    allow_headers=["*"]

)



# ------------------------
# TEMP USERS
# ------------------------

users={}



# ------------------------
# LOAD MODEL
# ------------------------


model=joblib.load(
    "../models/disease_model.pkl"
)


encoder=joblib.load(
    "../models/disease_encoder.pkl"
)



# ------------------------
# SCHEMAS
# ------------------------


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





# ------------------------
# HOME
# ------------------------


@app.get("/")

def home():

    return {

        "message":
        "Netravaan AI Running"

    }




# ------------------------
# REGISTER
# ------------------------


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






# ------------------------
# LOGIN
# ------------------------


@app.post("/login")

def login(data:Login):


    user=users.get(
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





# ------------------------
# DISEASE PREDICTION
# ------------------------


@app.post("/predict")

def predict(data:PredictionInput):


    df=pd.DataFrame([{


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



    result=model.predict(df)



    disease=encoder.inverse_transform(
        result
    )



    return {

        "prediction":
        disease[0]

    }





# ------------------------
# REPORT ANALYZER
# ------------------------



@app.post("/report")

async def report(file:UploadFile=File(...)):


    path="report.pdf"


    with open(path,"wb") as f:

        f.write(
            await file.read()
        )


    text=extract_text(
        path
    )


    analysis=analyze_report(
        text
    )


    return {

        "analysis":
        analysis

    }






# ------------------------
# VOICE AI
# ------------------------



@app.get("/voice")

def voice():


    question,lang=speech_to_text()



    answer=medical_chat(
        question
    )



    if lang!="en":

        answer=translate_text(
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