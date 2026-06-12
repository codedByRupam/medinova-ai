import fitz
import ollama




# =========================
# PDF TEXT EXTRACTION
# =========================


def extract_pdf_text(file_path):


    text = ""



    try:


        document = fitz.open(
            file_path
        )



        for page in document:


            text += page.get_text()



        document.close()



        return text



    except Exception as e:


        print(
            "PDF Error:",
            e
        )


        return "Unable to read PDF"







# backward compatibility
# (if old code calls extract_text)

def extract_text(file_path):


    return extract_pdf_text(
        file_path
    )









# =========================
# AI REPORT ANALYSIS
# =========================


def analyze_report(report_text):



    prompt = f"""

You are Netravaan AI medical assistant.

Analyze this medical report carefully.

Medical Report:

{report_text}



Provide response in this format:


1. Report Summary

2. Important Findings

3. Possible Health Concerns

4. General Health Suggestions


Rules:

- Do not give final diagnosis.
- Explain in simple language.
- Mention doctor consultation when needed.
- Do not create fear.


"""




    try:



        response = ollama.chat(


            model="llama3",


            messages=[

                {

                "role":"user",

                "content":prompt

                }

            ]

        )



        return response["message"]["content"]





    except Exception as e:



        return (

            "AI Analysis Error: "

            + str(e)

        )