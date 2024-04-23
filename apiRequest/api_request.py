from dotenv import dotenv_values

import google.generativeai as genai

def generate_recipe(plate):
    config = dotenv_values(".env")
    genai.configure(api_key=config["gemini_key"])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Dame los ingredientes necesarios para hacer  " + plate + ". No necesito las proporciones ni como usarlos, solo la lista de ingredientes.")
    print(response.candidates[0].content.parts[0].text)
    return response.candidates[0].content.parts[0].text

export = generate_recipe