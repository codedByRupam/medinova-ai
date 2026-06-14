import ollama



MODEL_NAME = "llama3.2:3b"



def medical_chat(user_message):


    try:


        prompt = f"""

You are Netravaan AI,
a medical assistant.

Answer in simple language.

Rules:

- Explain clearly
- Do not diagnose
- Give general health guidance
- Suggest doctor visit when needed


User:

{user_message}

"""


        response = ollama.chat(

            model=MODEL_NAME,

            messages=[

                {
                    "role":"user",
                    "content":prompt
                }

            ],

            options={

                "temperature":0.3,

                "num_ctx":1024

            }

        )


        return response["message"]["content"]



    except Exception as e:


        print("OLLAMA ERROR:",e)


        return "AI service unavailable"