import fitz
import os


def extract_text(pdf_path):

    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    doc.close()

    return text



def analyze_report(pdf_path):

    try:

        text = extract_text(pdf_path)


        if len(text) == 0:

            return {
                "status":"error",
                "message":"No readable text found"
            }


        # Temporary AI analysis
        # Later connect OpenAI/Gemini API here

        result = {

            "summary":
            "Medical report uploaded successfully. AI analysis will process the detected information.",


            "findings":
            text[:500],


            "recommendation":
            "Please consult a qualified healthcare professional for diagnosis."

        }


        return result



    except Exception as e:


        return {

            "status":"error",
            "message":str(e)

        }