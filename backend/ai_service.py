import ollama



MODEL_NAME = "llama3.2:3b"



def ask_ai(prompt):

    try:


        response = ollama.chat(

            model=MODEL_NAME,

            messages=[

                {

                    "role":"user",

                    "content":prompt

                }

            ],

            options={


                "temperature":0.2,


                "num_ctx":1024


            }


        )


        return response["message"]["content"]



    except Exception as e:


        print("OLLAMA ERROR:",e)


        return "AI service unavailable"