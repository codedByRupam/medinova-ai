import fitz

from ai_service import ask_ai



# =========================
# EXTRACT TEXT FROM PDF
# =========================

def extract_text(pdf_path):

    try:

        text = ""

        doc = fitz.open(pdf_path)


        for page in doc:

            page_text = page.get_text()

            text += page_text + "\n"



        doc.close()



        return text.strip()



    except Exception as e:


        print("PDF ERROR:", e)

        return ""





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





    # Prevent huge reports crashing local LLM

    if len(report_text) > 6000:

        report_text = report_text[:6000]





    prompt = f"""

You are Netravaan AI,
a medical report assistant.


Your job:

Explain this medical report
to a normal person.


STRICT RULES:

- Use simple English.
- No complex medical language.
- Do not diagnose diseases.
- Do not scare the user.
- Maximum 150 words.
- Use bullet points.


FORMAT EXACTLY:



🩺 Health Report Summary


📄 Report Type:

(write report type)



🔍 Key Findings:

- finding 1

- finding 2



⚠️ Possible Concerns:

- explain simply



✅ General Advice:

- simple health suggestions



📌 Disclaimer:

This AI explanation is only for information.
Consult a doctor for medical decisions.



REPORT:

{report_text}



"""




    try:


        ai_response = ask_ai(prompt)



        return {


            "analysis": ai_response


        }




    except Exception as e:


        print(
            "REPORT AI ERROR:",
            e
        )



        return {


            "analysis":

            """

🩺 Health Report Summary


⚠️ AI analysis is currently unavailable.

Please try again later.


"""

        }