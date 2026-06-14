import fitz

from ai_service import ask_ai



# =========================
# EXTRACT TEXT FROM PDF
# =========================

def extract_text(pdf_path):

    text = ""


    doc = fitz.open(pdf_path)


    for page in doc:

        text += page.get_text()


    doc.close()


    return text.strip()





# =========================
# ANALYZE MEDICAL REPORT
# =========================

def analyze_report(pdf_path):


    report_text = extract_text(pdf_path)



    if not report_text:


        return {

            "analysis": """

🩺 Health Report Summary


⚠️ Unable to read this PDF.

Please upload a clear medical report PDF.

"""

        }





    prompt = f"""

You are Netravaan AI, a healthcare assistant.

Read the medical report below and explain it like a doctor explaining to a patient.

IMPORTANT RULES:

- Use simple words.
- Do not write a long medical article.
- Avoid complicated medical terms.
- Maximum 200 words.
- Use bullet points.
- Make it easy for normal people.

Follow this exact format:


🩺 Health Report Summary


📄 Report Type:
(identify report type)


🔍 Key Findings:
- Important result 1
- Important result 2


⚠️ Possible Concerns:
- Explain possible issues simply


✅ General Health Advice:
- Give basic suggestions


📌 Note:
This AI analysis is only for information and is not a medical diagnosis.



Medical Report:

{report_text}

"""




    ai_response = ask_ai(prompt)




    return {


        "analysis": ai_response


    }