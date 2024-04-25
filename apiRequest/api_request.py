from dotenv import dotenv_values

import google.generativeai as genai

persons="7"

def generate_recipe(plate):
    config = dotenv_values(".env")
    genai.configure(api_key=config["gemini_key"])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Dame los ingredientes necesarios para preparar  " + plate + " para "+persons+" personas. solo necesito la lista de ingredientes y las cantidades.")
    print(response.candidates[0].content.parts[0].text)
    return response.candidates[0].content.parts[0].text

def generateMenu(plates):
    config = dotenv_values(".env")
    genai.configure(api_key=config["gemini_key"])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Genera un menú balanceado para todo el mes sin repetir platillos. Tu respuesta debe ser un JSON donde la llave es el número de día y el valor es el nombre del plato. Puedes usar los siguientes platillos o agregar nuevos: "+plates)
    print(response.candidates[0].content.parts[0].text)
    return response.candidates[0].content.parts[0].text
