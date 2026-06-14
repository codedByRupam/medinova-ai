import fitz
from ai_service import ask_ai
import json


def extract_text(pdf_path):

    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    doc.close()

    return text.strip()



def analyze_report(pdf_path):

    try:

        report_text = extract_text(pdf_path)


        if not report_text:

            return {
                "summary":
                "Unable to read this report.",

                "findings": [],

                "concerns": [],

                "advice": []
            }



        prompt = f"""

You are Netravaan AI medical assistant.

Analyze this medical report.

Return ONLY valid JSON.

Format:

{{
"summary":"short simple explanation",

"findings":[
"finding 1",
"finding 2"
],

"concerns":[
"concern 1"
],

"advice":[
"health advice 1",
"health advice 2"
]

}}

Rules:

- Keep summary under 3 sentences
- Use simple patient friendly language
- Do not diagnose
- Avoid medical jargon


REPORT:

{report_text}

"""



        response = ask_ai(prompt)



        print("AI RESPONSE:")
        print(response)



        try:

            data=json.loads(response)


        except:


            data={

                "summary":response,

                "findings":[],

                "concerns":[],

                "advice":[]

            }



        return data



    except Exception as e:


        print("REPORT ERROR:",e)


        return {


        "summary":
        "Unable to analyze report right now.",


        "findings":[],

        "concerns":[],

        "advice":[]

        }