import ollama


# =========================
# Netravaan AI Medical Chatbot
# Lightweight Model Version
# =========================


MODEL_NAME = "llama3.2:3b"



def medical_chat(user_message):

    try:


        prompt = f"""

You are Netravaan AI, a medical assistant.

Help users with general health information.

Your responsibilities:

- Explain symptoms in simple language
- Provide general health guidance
- Explain medical reports
- Suggest when a doctor should be consulted


Important rules:

- Do not provide final diagnosis
- Do not replace a doctor
- Avoid unsafe medical advice
- Ask questions if information is missing


User:

{user_message}


Response:

"""


        response = ollama.chat(

            model=MODEL_NAME,

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            options={

                "temperature": 0.3,

                "num_ctx": 2048

            }

        )


        return response["message"]["content"]



    except Exception as e:


        print(
            "Chatbot Error:",
            e
        )


        return (

            "Netravaan AI is unavailable. "
            "Please check if Ollama is running."

        )